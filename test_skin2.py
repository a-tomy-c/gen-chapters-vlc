import os
from PySide6.QtWidgets import QWidget, QListWidgetItem, QListWidget
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QIcon, QPixmap, QShortcut, QKeySequence
from skin_chaptersvlc import Ui_SkinChapters
from qplayer_vlc import QPlayer
from rw_files import RWFiles


class MakeChapters(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SkinChapters()
        self.ui.setupUi(self)
        self.__init_mk_chapters()

    def __init_mk_chapters(self):
        self.player = QPlayer()
        self.ui.vly_player.addWidget(self.player)
        self._reload_configs_skin()

    def _reload_configs_skin(self):
        rw = RWFiles()
        d = rw.read_yaml(path_file='configs_mkchapters.yaml')

        self.ui.frame_player.setMinimumHeight(d.get('player-min-h'))
        self._size_icon_chapters_init(value=d.get('list-chapters')['icon-size'])
        self._size_icon_stars_init(value=d.get('list-stars')['icon-size'])
        self.player.setVolume(d.get('volume-init'))
        self.setAcceptDrops(True)
        self.ui.tex_info.setReadOnly(True)
        self.player.timer.timeout.connect(self._update_time_labels)

        self.ui.slider_chapters.sliderMoved.connect(self._set_value_lb_chapter)
        self.ui.slider_chapters.sliderReleased.connect(self._set_size_icon_chapters)
        self.ui.bt_rw.clicked.connect(self.backward_1s)
        self.ui.bt_ff.clicked.connect(self.forward_1s)
        self.ui.bt_capture.clicked.connect(self.capture_frame)
        self.ui.bt_previous.clicked.connect(self.previous_frame)
        self.ui.bt_next.clicked.connect(self.next_frame)
        self.ui.bt_star.clicked.connect(self._add_star)
        self.ui.bt_toggle.clicked.connect(self.toggle_chapters)
        self.ui.bt_toggle2.clicked.connect(self.toggle_lists)
        self.ui.bt_make.clicked.connect(self.make_one_chapter)
        self.ui.bt_info.clicked.connect(self.clear_chapters)

        self.STAR = {}
        self.CHAPTERS = {}
        self.CAPTURE_PATH = ''
        self._set_shortcut()

    def _set_size_icon_chapters(self):
        value = self.ui.slider_chapters.value()
        self.ui.list_chapters_icons.setIconSize(QSize(value, value))

    def _set_size_icon_stars(self):
        value = self.ui.slider_stars.value()
        self.ui.list_star_icons.setIconSize(QSize(value, value))

    def _size_icon_chapters_init(self, value:int):
        self.ui.slider_chapters.setValue(value)
        self.ui.list_chapters_icons.setIconSize(QSize(value, value))
        self._set_value_lb_chapter(value)

    def _size_icon_stars_init(self, value:int):
        self.ui.slider_stars.setValue(value)
        self.ui.list_star_icons.setIconSize(QSize(value, value))
        self._set_value_lb_star(value)
        self.ui.list_chapters.setIconSize(QSize(value, value))

    def _set_value_lb_chapter(self, value:int):
        self.ui.lb_slider_chapters.setText(str(value))

    def _set_value_lb_star(self, value:int):
        self.ui.lb_slider_stars.setText(str(value))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            filepath = urls[0].toLocalFile()
            self.player.set_video(filepath)
        event.acceptProposedAction()

    def _update_time_labels(self):
        time_a, time_b = self.player.get_timestamps()
        self.ui.lb_time_a.setText(time_a)
        self.ui.lb_time_b.setText(time_b)

    def _update_pos(self):
        self.player.updatePos()
        self._update_time_labels()

    def backward_1s(self):
        self.player._pos_assign(-1000)
        self._update_pos()

    def forward_1s(self):
        self.player._pos_assign(1000)
        self._update_pos()

    def capture_frame(self) -> dict:
        '''{msg, path}'''
        return self.player.saveCapture()
    
    def next_frame(self):
        self.player._pos_assign(50)
        self._update_pos()

    def previous_frame(self):
        self.player._pos_assign(-50)
        self._update_pos()

    def _toggle_page(self, swidget):
        index = 1 if swidget.currentIndex()==0 else 0
        swidget.setCurrentIndex(index)

    def toggle_chapters(self):
        self._toggle_page(self.ui.sw_chapters)

    def _mk_timestamp(self, d_timestamp:dict, wlist):
        msec = self.player.get_time()
        d_timestamp[str(msec)] = self.player.ms_hmsz(msec)
        li = [f'{v}\n{k}' for k, v in d_timestamp.items()]
        wlist.clear()
        wlist.addItems(li)

    # def make_one_chapter(self):
    #     self._mk_timestamp(self.CHAPTERS, self.ui.list_chapters_icons)
    #     self.ui.sw_chapters.setCurrentIndex(0)

    def append_txt(self, line:str):
        d = self._read_config_yaml()
        path_chapters = d.get('path-chapters')
        rw = RWFiles()
        rw.append_txt(path_chapters, line)

    def _read_config_yaml(self) -> dict:
        rw = RWFiles()
        return rw.read_yaml(path_file='configs_mkchapters.yaml')
    
    def _load_image_icon(self, image_path:str):
        if not os.path.exists(image_path):
            return QIcon()
        try:
            d = self._read_config_yaml()
            size = d.get('list-chapters')['icon-size']
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                return QIcon()
            scaled_pixmap = pixmap.scaled(
                size, size,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            return QIcon(scaled_pixmap)
        except Exception as _:
            return QIcon()
    
    def add_itemlist_chapter(self, msec:int, ts:str, image:str):
        text = f'{msec}\n{ts}'
        item = QListWidgetItem(text)
        icon = self._load_image_icon(image_path=image)
        item.setIcon(icon)
        data = {
            'msec':msec,
            'ts':ts,
            'image':image
        }
        item.setData(Qt.UserRole, data)
        self.ui.list_chapters_icons.addItem(item)
        item2 = QListWidgetItem(text)
        item2.setData(Qt.UserRole, data)
        item2.setIcon(icon)
        self.ui.list_chapters.addItem(item2)

    def _gen_data(self):
        msec = self.player.get_time()
        ts = self.player.ms_hmsz(msec)
    
    def _write_line_txt_chapter(self, path_image:str):
        msec = self.player.get_time()
        ts = self.player.ms_hmsz(msec)
        self.add_itemlist_chapter(msec=msec, ts=ts, image=path_image)
        if self.timer:
            self.timer.stop()
        sep = '\n|-'
        line = f'-- CHAPTER:{sep}{msec}{sep}{ts}{sep}{path_image}\n\n'
        self.append_txt(line=line)

    def make_one_chapter(self):
        self.ui.sw_chapters.setCurrentIndex(0)
        self.ui.sw_star.setCurrentIndex(0)
        data = self.capture_frame()
        path = data.get('path', None)
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda:self._write_line_txt_chapter(path))
        self.timer.start(1000)

    def _set_shortcut(self):
        d = {
            Qt.Key_Delete:self._delete_item_chapter
        }
        for k, v in d.items():
            QShortcut(QKeySequence(k), self, v, context=Qt.ApplicationShortcut)

    def _delete_item_chapter(self):
        row = self.ui.list_chapters_icons.currentRow()
        self.ui.list_chapters_icons.takeItem(row)

    # STAR
    def _add_star(self):
        self._mk_timestamp(self.STAR, self.ui.list_star_icons)
        self.ui.sw_star.setCurrentIndex(0)
    # STAR
    def toggle_lists(self):
        index_ch = 1 if self.ui.sw_chapters.currentIndex()==0 else 0
        index_st = 1 if index_ch==0 else 0
        self.ui.sw_chapters.setCurrentIndex(index_ch)
        self.ui.sw_star.setCurrentIndex(index_st)

    def clear_chapters(self):
        self.msg('mi-texto\n')

    def msg(self, text:str, fg='gray'):
        br = '<br>' if text.endswith('\n') else ''
        if br:
            text = text.strip('\n')
        html = f'<span style=color:{fg};>{text}</span>{br}'
        self.ui.tex_info.insertHtml(html)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mc = MakeChapters()
    mc.show()

    file = '/home/tomy/Descargas/vi-1/so11-test.mp4'
    mc.player.set_video(file)
    sys.exit(app.exec())
