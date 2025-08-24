from PySide6.QtWidgets import QWidget
from skin_chaptersvlc import Ui_SkinChapters
from qplayer_vlc import QPlayer


class MakeChapters(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SkinChapters()
        self.ui.setupUi(self)
        self.__init_mk_chapters()

    def __init_mk_chapters(self):
        self.player = QPlayer()
        self.ui.vly_player.addWidget(self.player)
        self.ui.frame_player.setMinimumHeight(220)
        self.setAcceptDrops(True)
        self.ui.tex_info.setReadOnly(True)
        self.player.timer.timeout.connect(self._update_time_label)
        self.ui.bt_rw.clicked.connect(self.backward_1s)
        self.ui.bt_ff.clicked.connect(self.forward_1s)
        self.ui.bt_capture.clicked.connect(self.capture_frame)
        self.ui.bt_previous.clicked.connect(self.previous_frame)
        self.ui.bt_next.clicked.connect(self.next_frame)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            filepath = urls[0].toLocalFile()
            self.player.set_video(filepath)
        event.acceptProposedAction()

    def _update_time_label(self):
        time_a, time_b = self.player.get_timestamps()
        self.ui.lb_time_a.setText(time_a)
        self.ui.lb_time_b.setText(time_b)

    def backward_1s(self):
        self.player._pos_assign(-1000)
        self.player.updatePos()

    def forward_1s(self):
        # dur = self.player.get_length()
        # val = self.player.sld_time.value()
        # mx = self.player.sld_time.maximum()
        # print(dur, f'{val} - {mx}')
        self.player._pos_assign(1000)
        self.player.updatePos()

    def capture_frame(self):
        self.player.saveCapture()

    def next_frame(self):
        self.player._pos_assign(50)
        self.player.updatePos()

    def previous_frame(self):
        self.player._pos_assign(-50)
        self.player.updatePos()



if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mc = MakeChapters()
    mc.show()
    sys.exit(app.exec())