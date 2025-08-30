import os
from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QIcon, QPixmap
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
        self.ui.frame_player.setMinimumHeight(250)
        self.setAcceptDrops(True)
        self.ui.tex_info.setReadOnly(True)
        self.player.timer.timeout.connect(self._update_time_labels)
        self.ui.bt_rw.clicked.connect(self.backward_1s)
        self.ui.bt_ff.clicked.connect(self.forward_1s)
        self.ui.bt_capture.clicked.connect(self.capture_frame)
        self.ui.bt_previous.clicked.connect(self.previous_frame)
        self.ui.bt_next.clicked.connect(self.next_frame)
        self.ui.bt_star.clicked.connect(self.add_star)
        self.ui.bt_toggle.clicked.connect(self.toggle_page)
        # self.ui.bt_make.clicked.connect(self.make_one_chapter)
        self.ui.list_chapters.itemClicked.connect(self._item_entered)
        self.player.sld_time.sliderMoved.connect(self._update_time_labels)
        self.ui.list_star.itemClicked.connect(self._item_entered)
        self.ui.bt_make.clicked.connect(self.add_one_chapter)

        self.STAR = {}
        self.CHAPTERS = {}
        self.ui.list_chapters.setIconSize(QSize(180,180))
        self.ui.list_chapters.setSpacing(0)

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

    def backward_1s(self):
        self.player._pos_assign(-1000)
        self._update_pos()

    def forward_1s(self):
        self.player._pos_assign(1000)
        self._update_pos()

    def capture_frame(self):
        return self.player.saveCapture()

    def next_frame(self):
        self.player._pos_assign(50)
        self._update_pos()

    def previous_frame(self):
        self.player._pos_assign(-50)
        self._update_pos()

    # def update_labels(self):
    #     timestamp, elapsed_timestamp = self.player.get_timestamps()
    #     self.ui.lb_time_a.setText(timestamp)
    #     self.ui.lb_time_a.setText(elapsed_timestamp)

    def _update_pos(self):
        self.player.updatePos()
        self._update_time_labels()

    def add_star(self):
        self._mk_timestamp(self.STAR, self.ui.list_star)
        self.ui.stackedWidget.setCurrentIndex(1)

    def refresh_items(self, msecs:list):
        self.ui.list_chapters.clear()
        self.ui.list_chapters.addItems(msecs)

    def toggle_page(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.bt_toggle.setText('Chapters')
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.bt_toggle.setText('Stars')

    def make_one_chapter(self):
        self._mk_timestamp(self.CHAPTERS, self.ui.list_chapters)
        self.ui.stackedWidget.setCurrentIndex(0)

    def _mk_timestamp(self, d_timestamps:dict, widget_list):
        msec = self.player.get_time()
        d_timestamps[str(msec)] = self.player.ms_hmsz(msec)
        li = [f'{v}\n{k}' for k, v in d_timestamps.items()]

        widget_list.clear()
        widget_list.addItems(li)

    def _item_entered(self, item):
        data = item.text()
        print(data)
        if '\n' in data:
            ms, _ts = data.split('\n')
            print('ts:', _ts, ms)
            self.player.set_time(int(ms))

    def load_image_icon(self, image_path:str):
        if not os.path.exists(image_path):
            return QIcon()
        try:
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                return QIcon()
            scaled_pixmap = pixmap.scaled(
                180, 180,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            return QIcon(scaled_pixmap)
        except Exception as _:
            return QIcon()
        
    def add_item_to_list(self, text:str, image:str):
        item = QListWidgetItem(text)
        icon = self.load_image_icon(image_path=image)
        # if icon.isNull():
        #     item.setIcon(icon)
        #     print('asigna icono nulo')
        item.setIcon(icon)
        self.ui.list_chapters.addItem(item)

    def _add_one_chapter(self, path:str):
        # d_timestamps = self.CHAPTERS
        msec = self.player.get_time()
        # d_timestamps[str(msec)] = self.player.ms_hmsz(msec)
        # li = [f'{v}\n{k}' for k, v in d_timestamps.items()]
        ts = self.player.ms_hmsz(msec)
        texto = f'{msec}\n{ts}'
        # name = f'{ts.replace(":",".")}.jpg'
        name = path
        # name = '/home/tomy/Descargas/vi-1/00.23.05.834.jpg'
        self.add_item_to_list(text=texto, image=name)
        print('name_img: ', name)

        if self.timer:
            self.timer.stop()
        print('chapter ya creado....')

    def add_one_chapter(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        path = self.capture_frame()

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda :self._add_one_chapter(path))
        self.timer.start(600)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mc = MakeChapters()
    mc.show()

    file = '/home/tomy/Descargas/vi-1/so11-test.mp4'
    mc.player.set_video(file)
    sys.exit(app.exec())