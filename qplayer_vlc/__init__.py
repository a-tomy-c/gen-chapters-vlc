from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Signal
from qplayer_vlc.skin import Ui_SkinPlayer
import vlc
import platform
from pathlib import Path


class QPlayer(QWidget, Ui_SkinPlayer):
    # Señales para comunicación thread-safe
    media_playing = Signal()
    media_stopped = Signal()
    media_paused = Signal()
    media_ended = Signal()
    def __init__(self, *args, **kw):
        super(QPlayer, self).__init__(*args, **kw)
        self.setupUi(self)
        self.media_loaded = False  # Bandera para saber si hay video cargado
        self.__configQPlayer()
        
    def __configQPlayer(self):
        self.video_widget = QWidget()
        self.video_widget.setStyleSheet('background-color:black;')
        self.vly_video.addWidget(self.video_widget)

        system = platform.system().lower()
        if system == "linux":
            vlc_args = self.get_linux_args()
        elif system == "windows":
            vlc_args = self.get_windows_args()
        elif system == "darwin":  # macOS
            vlc_args = self.get_macos_args()
        else:
            vlc_args = ['--no-video-title-show', '--quiet']

        self.instance = vlc.Instance(vlc_args)
        self.player = self.instance.media_player_new()
        # self.player.set_hwnd(int(self.video_widget.winId()))
        # self.player.set_xwindow(self.video_widget.winId())

        if system == "linux":
                # En Linux usamos XWindow
            self.player.set_xwindow(self.video_widget.winId())
        elif system == "windows":
            # En Windows usamos HWND
            self.player.set_hwnd(self.video_widget.winId())
        elif system == "darwin":
            # En macOS usamos NSView
                self.player.set_nsobject(int(self.video_widget.winId()))

        # Configurar eventos de VLC
        self.event_manager = self.player.event_manager()
        self.event_manager.event_attach(vlc.EventType.MediaPlayerMediaChanged, self.on_media_changed)
        self.event_manager.event_attach(vlc.EventType.MediaPlayerPlaying, self.on_playing)
        self.event_manager.event_attach(vlc.EventType.MediaPlayerPaused, self.on_paused)
        self.event_manager.event_attach(vlc.EventType.MediaPlayerStopped, self.on_stopped)
        self.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.on_end_reached)

        self.sld_time.setMaximum(1000)
        self.sld_vol.setMaximum(100)
        self.btn_play.clicked.connect(self.playPause)
        self.btn_stop.clicked.connect(self.stop)
        self.sld_time.sliderMoved.connect(self.setPosition)
        self.sld_vol.sliderMoved.connect(self.setVolume)
        self.btn_toggle.clicked.connect(self.toggleCtrl)
        self.btn_ff.clicked.connect(self.goForward)
        self.btn_rw.clicked.connect(self.goRewind)
        self.btn_left.clicked.connect(self._posPrev)
        self.btn_right.clicked.connect(self._posNext)
        self.btn_c.clicked.connect(self.saveCapture)

        # Timer optimizado - solo se inicia cuando es necesario
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updatePos)
        
        # Conectar señales para thread-safe operations
        self.media_playing.connect(self._on_playing_safe)
        self.media_stopped.connect(self._on_stopped_safe)
        self.media_paused.connect(self._on_paused_safe)
        self.media_ended.connect(self._on_ended_safe)

        self.VIDEOPATH = None

    def get_linux_args(self):
        """Argumentos optimizados para Linux"""
        return [
            '--no-video-title-show',
            '--no-snapshot-preview',
            '--avcodec-hw=none',      # Evita problemas de hardware
            '--vout=xcb_x11',         # Output de video para X11
            '--aout=pulse',           # Audio para PulseAudio
            '--quiet'
        ]
    
    def get_windows_args(self):
        """Argumentos optimizados para Windows"""
        return [
            '--no-video-title-show',
            '--no-snapshot-preview',
            '--vout=directx',         # DirectX para Windows
            '--aout=directsound',     # DirectSound para audio
            '--avcodec-hw=d3d11va',   # Aceleración hardware en Windows
            '--quiet'
        ]
    
    def get_macos_args(self):
        """Argumentos optimizados para macOS"""
        return [
            '--no-video-title-show',
            '--no-snapshot-preview',
            '--vout=macosx',          # Output nativo de macOS
            '--aout=auhal',           # Audio nativo de macOS
            '--quiet'
        ]

    def set_video(self, file: str):
        """Cargar video y marcar que hay media disponible"""
        media = self.instance.media_new(file)
        self.player.set_media(media)
        self.media_loaded = True
        self.VIDEOPATH = file

    def on_media_changed(self, event):
        """Callback cuando cambia el media"""
        self.media_loaded = True

    def on_playing(self, event):
        """Callback cuando empieza la reproducción - emite señal thread-safe"""
        self.media_playing.emit()

    def on_paused(self, event):
        """Callback cuando se pausa - emite señal thread-safe"""
        self.media_paused.emit()

    def on_stopped(self, event):
        """Callback cuando se detiene - emite señal thread-safe"""
        self.media_stopped.emit()

    def on_end_reached(self, event):
        """Callback cuando termina el video - emite señal thread-safe"""
        self.media_ended.emit()

    # Métodos thread-safe que se ejecutan en el hilo principal
    def _on_playing_safe(self):
        """Manejo thread-safe del evento playing"""
        if not self.timer.isActive():
            self.timer.start(100)

    def _on_paused_safe(self):
        """Manejo thread-safe del evento paused"""
        print("Video pausado (thread-safe)")
        # Mantenemos el timer activo para mostrar la posición

    def _on_stopped_safe(self):
        """Manejo thread-safe del evento stopped"""
        # "Parando timer (thread-safe)"
        self.timer.stop()
        self.sld_time.setValue(0)
        self._resetTimeLabels()

    def _on_ended_safe(self):
        """Manejo thread-safe del evento ended"""
        # "Video terminado - parando timer (thread-safe)"
        self.timer.stop()

    def _resetTimeLabels(self):
        """Resetear las etiquetas de tiempo"""
        self.lb_time.setText("00:00:00")
        self.lb_timestamp.setText("00:00:00.000")
        self.lb_timestamp_res.setText("00:00:00.000")

    def playPause(self):
        if not self.media_loaded:
            return
            
        if self.player.is_playing():
            self.player.pause()
        else:
            self.player.play()

    def stop(self):
        self.player.stop()
        # on_stopped callback se encargará de parar el timer

    def setPosition(self, pos):
        if not self.media_loaded:
            return
        self.player.set_position(pos/1e3)
        # print(self.get_time(), self.get_current_time())
        self.update_labels()

    def updatePos(self):
        """Actualizar posición - solo se llama cuando el timer está activo"""
        if not self.media_loaded or self.player.get_length() <= 0:
            return

        # Actualizar slider
        pos: float = self.player.get_position() * 1000
        self.sld_time.setValue(int(pos))
        # print('pos:: ', pos)

        # Actualizar tiempos
        current_time: int = self.player.get_time()
        total_time: int = self.player.get_length()
        # print("cur", current_time, type(current_time), "tot", total_time)

        if current_time >= 0 and total_time > 0 and current_time<=total_time:
            current_str = self.ms_hms(current_time)
            self.lb_time.setText(current_str)
            self.lb_timestamp.setText(self.ms_hmsz(current_time))
            res = total_time - current_time
            self.lb_timestamp_res.setText(self.ms_hmsz(res))
            # print("::: ", current_str, " RES: ", res)

        # Verificar si terminó (redundante con on_end_reached, pero por seguridad)
        if current_time == total_time and total_time > 0:
            self.timer.stop()
        # 4:paused, 6:ended 
        std = self.player.get_state()
        if std == 4 or std == 6: # estados vlc 4517
            self.timer.stop()

    def _mseg_hmsz(self, milliseconds: float | str) -> tuple:
        '''retorna tupla[int] = h, m, s, z'''
        h, r = divmod(float(milliseconds), 3.6e6)
        m, r = divmod(r, 6e4)
        s, z = divmod(r, 1e3)
        return int(h), int(m), int(s), int(z)
        
    def ms_hms(self, msec: int) -> str:
        timestamp = '00:00:00'
        if msec:
            h, m, s, z = self._mseg_hmsz(msec)
            timestamp = f'{h:02d}:{m:02d}:{s:02d}'
        return timestamp

    def ms_hmsz(self, msec: int) -> str:
        timestamp = '00:00:00.000'
        if msec:
            h, m, s, z = self._mseg_hmsz(msec)
            timestamp = f'{h:02d}:{m:02d}:{s:02d}.{z:03d}'
        return timestamp

    def setVolume(self, num: int):
        self.player.audio_set_volume(num)
        self.sld_vol.setValue(int(num))
        self.lb_vol.setText(str(num))

    def toggleCtrl(self):
        index: int = 0 if self.stw.currentIndex() == 1 else 1
        self.stw.setCurrentIndex(index)

    def goForward(self):
        self._pos_assign(3000)

    def goRewind(self):
        self._pos_assign(-3000)

    def _posNext(self):
        self._pos_assign(100)

    def _posPrev(self):
        self._pos_assign(-100)

    def _pos_assign(self, pos:int=1):
        if not self.media_loaded:
            return
        # self.setPosition(self.sld_time.value() + pos)
        now_msec = self.player.get_time()
        time = 0 if now_msec < pos else now_msec + pos
        self.player.set_time(time)

        if self.player.get_state() == vlc.State.Playing:
            self.player.pause()

        self.update_labels()

    def saveCapture(self):
        if not self.media_loaded:
            # "No hay video para capturar"
            return
            
        current_time: int = self.player.get_time()
        if current_time < 0:
            return
            
        path = Path(self.VIDEOPATH).parent.as_posix()
        name = self.ms_hmsz(current_time).replace(':', '.')
        success = self.player.video_take_snapshot(0, f'{path}/{name}.jpg', 0, 0)
        if success == 0:
            print(f"Capturado -> {name}.jpg")
        else:
            print("Error al capturar frame")
        
        new_path = f'{path}/{name}.jpg'
        return new_path

    def get_position(self) -> float:
        return self.player.get_position()
    
    def get_current_time(self) -> str:
        return self.ms_hmsz(self.get_time())
    
    def get_time(self) -> int:
        return self.player.get_time()
    
    def get_elapsed_time(self) -> int:
        total_time:int = self.get_length()
        current_time = self.get_time()
        res = total_time - current_time
        return self.ms_hmsz(res)

    def get_length(self) -> int:
        return self.player.get_length()
    
    def get_timestamps(self) -> list:
        return [self.get_current_time(), self.get_elapsed_time()]
    
    def get_video(self) -> str:
        return self.VIDEOPATH

    def update_labels(self):
        # Actualizar tiempos
        current_time: int = self.player.get_time()
        total_time: int = self.player.get_length()
        # print("cur", current_time, "tot", total_time)

        if current_time >= 0 and total_time > 0:
            current_str = self.ms_hms(current_time)
            self.lb_time.setText(current_str)
            self.lb_timestamp.setText(self.ms_hmsz(current_time))
            res = total_time - current_time
            self.lb_timestamp_res.setText(self.ms_hmsz(res))
        
    def set_time(self, ms:int):
        self.player.set_time(ms)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vi1 = 'D:/SiSTEM/dance.mp4'
    wg = QPlayer()
    wg.setVolume(72)
    wg.show()
    wg.setVideo(vi1)
    sys.exit(app.exec())