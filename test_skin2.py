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
        print('value chp: ', d.get('list-chapters')['icon-size'])

        self.ui.slider_chapters.sliderMoved.connect(self._set_value_lb_chapter)
        self.ui.slider_chapters.sliderReleased.connect(self._set_size_icon_chapters)


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

    def _set_value_lb_chapter(self, value:int):
        self.ui.lb_slider_chapters.setText(str(value))

    def _set_value_lb_star(self, value:int):
        self.ui.lb_slider_stars.setText(str(value))






if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mc = MakeChapters()
    mc.show()

    # file = '/home/tomy/Descargas/vi-1/so11-test.mp4'
    # mc.player.set_video(file)
    sys.exit(app.exec())