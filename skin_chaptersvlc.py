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
    QSpacerItem, QSplitter, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_SkinChapters(object):
    def setupUi(self, SkinChapters):
        if not SkinChapters.objectName():
            SkinChapters.setObjectName(u"SkinChapters")
        SkinChapters.resize(700, 567)
        self.verticalLayout_7 = QVBoxLayout(SkinChapters)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.split_chapters = QSplitter(SkinChapters)
        self.split_chapters.setObjectName(u"split_chapters")
        self.split_chapters.setLineWidth(0)
        self.split_chapters.setOrientation(Qt.Orientation.Horizontal)
        self.split_player = QSplitter(self.split_chapters)
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
        self.split_chapters.addWidget(self.split_player)
        self.frame = QFrame(self.split_chapters)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(120, 0))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pag1 = QWidget()
        self.pag1.setObjectName(u"pag1")
        self.verticalLayout_8 = QVBoxLayout(self.pag1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.list_chapters = QListWidget(self.pag1)
        self.list_chapters.setObjectName(u"list_chapters")
        self.list_chapters.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout_8.addWidget(self.list_chapters)

        self.stackedWidget.addWidget(self.pag1)
        self.pag2 = QWidget()
        self.pag2.setObjectName(u"pag2")
        self.verticalLayout_10 = QVBoxLayout(self.pag2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.list_star = QListWidget(self.pag2)
        self.list_star.setObjectName(u"list_star")
        self.list_star.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.list_star.setFrameShape(QFrame.Shape.NoFrame)
        self.list_star.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_10.addWidget(self.list_star)

        self.stackedWidget.addWidget(self.pag2)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.split_chapters.addWidget(self.frame)

        self.verticalLayout_7.addWidget(self.split_chapters)


        self.retranslateUi(SkinChapters)

        self.stackedWidget.setCurrentIndex(0)


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
    # retranslateUi

