# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_chaptersvlc.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_SkinChapters(object):
    def setupUi(self, SkinChapters):
        if not SkinChapters.objectName():
            SkinChapters.setObjectName(u"SkinChapters")
        SkinChapters.resize(868, 561)
        self.verticalLayout_15 = QVBoxLayout(SkinChapters)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.split_center = QSplitter(SkinChapters)
        self.split_center.setObjectName(u"split_center")
        self.split_center.setOrientation(Qt.Orientation.Horizontal)
        self.split_player = QSplitter(self.split_center)
        self.split_player.setObjectName(u"split_player")
        self.split_player.setLineWidth(0)
        self.split_player.setOrientation(Qt.Orientation.Vertical)
        self.frame_3 = QFrame(self.split_player)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_top = QFrame(self.frame_3)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 54))
        self.frame_top.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_top.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_time_a = QLabel(self.frame_top)
        self.lb_time_a.setObjectName(u"lb_time_a")
        self.lb_time_a.setMinimumSize(QSize(130, 0))
        font = QFont()
        font.setPointSize(16)
        self.lb_time_a.setFont(font)
        self.lb_time_a.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_time_a)

        self.bt_ff = QPushButton(self.frame_top)
        self.bt_ff.setObjectName(u"bt_ff")
        self.bt_ff.setMaximumSize(QSize(50, 26))

        self.horizontalLayout.addWidget(self.bt_ff)

        self.bt_rw = QPushButton(self.frame_top)
        self.bt_rw.setObjectName(u"bt_rw")
        self.bt_rw.setMaximumSize(QSize(50, 26))

        self.horizontalLayout.addWidget(self.bt_rw)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lb_time_b = QLabel(self.frame_top)
        self.lb_time_b.setObjectName(u"lb_time_b")
        self.lb_time_b.setMinimumSize(QSize(130, 0))
        self.lb_time_b.setFont(font)
        self.lb_time_b.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_time_b)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_toggle = QPushButton(self.frame_top)
        self.bt_toggle.setObjectName(u"bt_toggle")
        self.bt_toggle.setMaximumSize(QSize(40, 26))

        self.horizontalLayout_2.addWidget(self.bt_toggle)

        self.bt_capture = QPushButton(self.frame_top)
        self.bt_capture.setObjectName(u"bt_capture")
        self.bt_capture.setMaximumSize(QSize(40, 26))

        self.horizontalLayout_2.addWidget(self.bt_capture)

        self.bt_star = QPushButton(self.frame_top)
        self.bt_star.setObjectName(u"bt_star")
        self.bt_star.setMaximumSize(QSize(40, 26))

        self.horizontalLayout_2.addWidget(self.bt_star)

        self.bt_previous = QPushButton(self.frame_top)
        self.bt_previous.setObjectName(u"bt_previous")
        self.bt_previous.setMaximumSize(QSize(40, 26))

        self.horizontalLayout_2.addWidget(self.bt_previous)

        self.bt_next = QPushButton(self.frame_top)
        self.bt_next.setObjectName(u"bt_next")
        self.bt_next.setMaximumSize(QSize(40, 26))

        self.horizontalLayout_2.addWidget(self.bt_next)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_make = QPushButton(self.frame_top)
        self.bt_make.setObjectName(u"bt_make")
        self.bt_make.setMaximumSize(QSize(60, 26))

        self.horizontalLayout_2.addWidget(self.bt_make)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_5.addWidget(self.frame_top)

        self.frame_player = QFrame(self.frame_3)
        self.frame_player.setObjectName(u"frame_player")
        self.frame_player.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_player.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_player.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame_player)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.vly_player = QVBoxLayout()
        self.vly_player.setObjectName(u"vly_player")

        self.verticalLayout_9.addLayout(self.vly_player)


        self.verticalLayout_5.addWidget(self.frame_player)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.split_player.addWidget(self.frame_3)
        self.frame_info = QFrame(self.split_player)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_info.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_info.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_info)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tex_info = QTextEdit(self.frame_info)
        self.tex_info.setObjectName(u"tex_info")

        self.verticalLayout_3.addWidget(self.tex_info)

        self.split_player.addWidget(self.frame_info)
        self.split_center.addWidget(self.split_player)
        self.fm_right = QFrame(self.split_center)
        self.fm_right.setObjectName(u"fm_right")
        self.fm_right.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_right.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.fm_right)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.split_lists = QSplitter(self.fm_right)
        self.split_lists.setObjectName(u"split_lists")
        self.split_lists.setOrientation(Qt.Orientation.Horizontal)
        self.fm_chapters = QFrame(self.split_lists)
        self.fm_chapters.setObjectName(u"fm_chapters")
        self.fm_chapters.setMinimumSize(QSize(120, 0))
        self.fm_chapters.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_chapters.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_chapters.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.fm_chapters)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sw_chapters = QStackedWidget(self.fm_chapters)
        self.sw_chapters.setObjectName(u"sw_chapters")
        self.pag1_chapter = QWidget()
        self.pag1_chapter.setObjectName(u"pag1_chapter")
        self.verticalLayout_8 = QVBoxLayout(self.pag1_chapter)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.list_chapters_icons = QListWidget(self.pag1_chapter)
        self.list_chapters_icons.setObjectName(u"list_chapters_icons")
        self.list_chapters_icons.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout_8.addWidget(self.list_chapters_icons)

        self.sw_chapters.addWidget(self.pag1_chapter)
        self.pag2_chapter = QWidget()
        self.pag2_chapter.setObjectName(u"pag2_chapter")
        self.verticalLayout_10 = QVBoxLayout(self.pag2_chapter)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.list_star = QListWidget(self.pag2_chapter)
        self.list_star.setObjectName(u"list_star")
        self.list_star.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.list_star.setFrameShape(QFrame.Shape.NoFrame)
        self.list_star.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_10.addWidget(self.list_star)

        self.sw_chapters.addWidget(self.pag2_chapter)

        self.verticalLayout_4.addWidget(self.sw_chapters)

        self.split_lists.addWidget(self.fm_chapters)
        self.fm_star = QFrame(self.split_lists)
        self.fm_star.setObjectName(u"fm_star")
        self.fm_star.setMinimumSize(QSize(120, 0))
        self.fm_star.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_star.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_star.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.fm_star)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sw_star = QStackedWidget(self.fm_star)
        self.sw_star.setObjectName(u"sw_star")
        self.pag1_star = QWidget()
        self.pag1_star.setObjectName(u"pag1_star")
        self.verticalLayout_11 = QVBoxLayout(self.pag1_star)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.list_chapters = QListWidget(self.pag1_star)
        self.list_chapters.setObjectName(u"list_chapters")
        self.list_chapters.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout_11.addWidget(self.list_chapters)

        self.sw_star.addWidget(self.pag1_star)
        self.pag2_star = QWidget()
        self.pag2_star.setObjectName(u"pag2_star")
        self.verticalLayout_12 = QVBoxLayout(self.pag2_star)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.list_star_icons = QListWidget(self.pag2_star)
        self.list_star_icons.setObjectName(u"list_star_icons")
        self.list_star_icons.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.list_star_icons.setFrameShape(QFrame.Shape.NoFrame)
        self.list_star_icons.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_12.addWidget(self.list_star_icons)

        self.sw_star.addWidget(self.pag2_star)

        self.verticalLayout_7.addWidget(self.sw_star)

        self.split_lists.addWidget(self.fm_star)

        self.verticalLayout_13.addWidget(self.split_lists)

        self.split_center.addWidget(self.fm_right)

        self.verticalLayout_14.addWidget(self.split_center)

        self.fm_bts_bot = QFrame(SkinChapters)
        self.fm_bts_bot.setObjectName(u"fm_bts_bot")
        self.fm_bts_bot.setMinimumSize(QSize(0, 26))
        self.fm_bts_bot.setMaximumSize(QSize(16777215, 26))
        self.fm_bts_bot.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_bts_bot.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.fm_bts_bot)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_make_chapters = QPushButton(self.fm_bts_bot)
        self.bt_make_chapters.setObjectName(u"bt_make_chapters")
        self.bt_make_chapters.setMinimumSize(QSize(0, 26))
        self.bt_make_chapters.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_3.addWidget(self.bt_make_chapters)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.bt_delete_star = QPushButton(self.fm_bts_bot)
        self.bt_delete_star.setObjectName(u"bt_delete_star")
        self.bt_delete_star.setMinimumSize(QSize(0, 26))
        self.bt_delete_star.setMaximumSize(QSize(70, 26))

        self.horizontalLayout_3.addWidget(self.bt_delete_star)

        self.bt_reload_chapters = QPushButton(self.fm_bts_bot)
        self.bt_reload_chapters.setObjectName(u"bt_reload_chapters")
        self.bt_reload_chapters.setMinimumSize(QSize(60, 26))
        self.bt_reload_chapters.setMaximumSize(QSize(60, 26))

        self.horizontalLayout_3.addWidget(self.bt_reload_chapters)

        self.bt_info = QPushButton(self.fm_bts_bot)
        self.bt_info.setObjectName(u"bt_info")
        self.bt_info.setMinimumSize(QSize(45, 26))
        self.bt_info.setMaximumSize(QSize(45, 26))

        self.horizontalLayout_3.addWidget(self.bt_info)

        self.slider_chapters = QSlider(self.fm_bts_bot)
        self.slider_chapters.setObjectName(u"slider_chapters")
        self.slider_chapters.setMinimumSize(QSize(80, 0))
        self.slider_chapters.setMaximumSize(QSize(80, 16777215))
        self.slider_chapters.setMinimum(80)
        self.slider_chapters.setMaximum(250)
        self.slider_chapters.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_chapters)

        self.lb_slider_chapters = QLabel(self.fm_bts_bot)
        self.lb_slider_chapters.setObjectName(u"lb_slider_chapters")
        self.lb_slider_chapters.setMinimumSize(QSize(50, 26))
        self.lb_slider_chapters.setMaximumSize(QSize(50, 26))
        font1 = QFont()
        font1.setPointSize(14)
        self.lb_slider_chapters.setFont(font1)
        self.lb_slider_chapters.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_slider_chapters)

        self.slider_stars = QSlider(self.fm_bts_bot)
        self.slider_stars.setObjectName(u"slider_stars")
        self.slider_stars.setMinimumSize(QSize(80, 0))
        self.slider_stars.setMaximumSize(QSize(80, 16777215))
        self.slider_stars.setMinimum(80)
        self.slider_stars.setMaximum(250)
        self.slider_stars.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_stars)

        self.lb_slider_stars = QLabel(self.fm_bts_bot)
        self.lb_slider_stars.setObjectName(u"lb_slider_stars")
        self.lb_slider_stars.setMinimumSize(QSize(50, 26))
        self.lb_slider_stars.setMaximumSize(QSize(50, 26))
        self.lb_slider_stars.setFont(font1)
        self.lb_slider_stars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_slider_stars)

        self.bt_toggle2 = QPushButton(self.fm_bts_bot)
        self.bt_toggle2.setObjectName(u"bt_toggle2")
        self.bt_toggle2.setMaximumSize(QSize(40, 26))

        self.horizontalLayout_3.addWidget(self.bt_toggle2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.fm_bts_bot)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


        self.retranslateUi(SkinChapters)

        self.sw_chapters.setCurrentIndex(0)
        self.sw_star.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SkinChapters)
    # setupUi

    def retranslateUi(self, SkinChapters):
        SkinChapters.setWindowTitle(QCoreApplication.translate("SkinChapters", u"Form", None))
        self.lb_time_a.setText(QCoreApplication.translate("SkinChapters", u"00:00:00.000", None))
        self.bt_ff.setText(QCoreApplication.translate("SkinChapters", u"FF", None))
        self.bt_rw.setText(QCoreApplication.translate("SkinChapters", u"RW", None))
        self.lb_time_b.setText(QCoreApplication.translate("SkinChapters", u"00:00:00.000", None))
        self.bt_toggle.setText(QCoreApplication.translate("SkinChapters", u"TG", None))
        self.bt_capture.setText(QCoreApplication.translate("SkinChapters", u"CAP", None))
        self.bt_star.setText(QCoreApplication.translate("SkinChapters", u"STAR", None))
        self.bt_previous.setText(QCoreApplication.translate("SkinChapters", u"<", None))
        self.bt_next.setText(QCoreApplication.translate("SkinChapters", u">", None))
        self.bt_make.setText(QCoreApplication.translate("SkinChapters", u"MAKE", None))
        self.bt_make_chapters.setText(QCoreApplication.translate("SkinChapters", u"MAKE CHAPTERS", None))
        self.bt_delete_star.setText(QCoreApplication.translate("SkinChapters", u"DEL STAR", None))
        self.bt_reload_chapters.setText(QCoreApplication.translate("SkinChapters", u"RELOAD", None))
        self.bt_info.setText(QCoreApplication.translate("SkinChapters", u"INFO", None))
        self.lb_slider_chapters.setText(QCoreApplication.translate("SkinChapters", u"158", None))
        self.lb_slider_stars.setText(QCoreApplication.translate("SkinChapters", u"158", None))
        self.bt_toggle2.setText(QCoreApplication.translate("SkinChapters", u"TG2", None))
    # retranslateUi

