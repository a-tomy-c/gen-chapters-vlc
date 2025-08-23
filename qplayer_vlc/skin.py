# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin.ui'
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
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_SkinPlayer(object):
    def setupUi(self, SkinPlayer):
        if not SkinPlayer.objectName():
            SkinPlayer.setObjectName(u"SkinPlayer")
        SkinPlayer.resize(491, 312)
        SkinPlayer.setStyleSheet(u"QLabel {\n"
"	font: 8pt \"Lucida Console\";\n"
"}\n"
"QPushButton {\n"
"	\n"
"	font: 8pt \"Consolas\";\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(SkinPlayer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fm_video = QFrame(SkinPlayer)
        self.fm_video.setObjectName(u"fm_video")
        self.fm_video.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_video.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.fm_video)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vly_video = QVBoxLayout()
        self.vly_video.setObjectName(u"vly_video")

        self.verticalLayout_4.addLayout(self.vly_video)


        self.verticalLayout.addWidget(self.fm_video)

        self.fm_botones = QFrame(SkinPlayer)
        self.fm_botones.setObjectName(u"fm_botones")
        self.fm_botones.setMinimumSize(QSize(0, 18))
        self.fm_botones.setMaximumSize(QSize(16777215, 18))
        self.fm_botones.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_botones.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.fm_botones)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_play = QPushButton(self.fm_botones)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(26, 18))
        self.btn_play.setMaximumSize(QSize(26, 18))
        self.btn_play.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_play)

        self.stw = QStackedWidget(self.fm_botones)
        self.stw.setObjectName(u"stw")
        self.pag_1 = QWidget()
        self.pag_1.setObjectName(u"pag_1")
        self.horizontalLayout_2 = QHBoxLayout(self.pag_1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sld_time = QSlider(self.pag_1)
        self.sld_time.setObjectName(u"sld_time")
        self.sld_time.setMinimumSize(QSize(0, 16))
        self.sld_time.setMaximumSize(QSize(16777215, 16))
        self.sld_time.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_time)

        self.lb_time = QLabel(self.pag_1)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setMinimumSize(QSize(60, 20))
        self.lb_time.setMaximumSize(QSize(60, 20))
        self.lb_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_time)

        self.sld_vol = QSlider(self.pag_1)
        self.sld_vol.setObjectName(u"sld_vol")
        self.sld_vol.setMinimumSize(QSize(60, 16))
        self.sld_vol.setMaximumSize(QSize(60, 16))
        self.sld_vol.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_vol)

        self.lb_vol = QLabel(self.pag_1)
        self.lb_vol.setObjectName(u"lb_vol")
        self.lb_vol.setMinimumSize(QSize(24, 20))
        self.lb_vol.setMaximumSize(QSize(24, 20))
        self.lb_vol.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_vol)

        self.btn_stop = QPushButton(self.pag_1)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(26, 18))
        self.btn_stop.setMaximumSize(QSize(26, 18))
        self.btn_stop.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_stop)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.stw.addWidget(self.pag_1)
        self.pag_2 = QWidget()
        self.pag_2.setObjectName(u"pag_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pag_2.sizePolicy().hasHeightForWidth())
        self.pag_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.pag_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_timestamp = QLabel(self.pag_2)
        self.lb_timestamp.setObjectName(u"lb_timestamp")
        self.lb_timestamp.setMinimumSize(QSize(90, 20))
        self.lb_timestamp.setMaximumSize(QSize(90, 20))
        self.lb_timestamp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lb_timestamp)

        self.btn_left = QPushButton(self.pag_2)
        self.btn_left.setObjectName(u"btn_left")
        self.btn_left.setMinimumSize(QSize(26, 18))
        self.btn_left.setMaximumSize(QSize(26, 18))
        self.btn_left.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_left)

        self.btn_right = QPushButton(self.pag_2)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setMinimumSize(QSize(26, 18))
        self.btn_right.setMaximumSize(QSize(26, 18))
        self.btn_right.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_right)

        self.btn_rw = QPushButton(self.pag_2)
        self.btn_rw.setObjectName(u"btn_rw")
        self.btn_rw.setMinimumSize(QSize(26, 18))
        self.btn_rw.setMaximumSize(QSize(26, 18))
        self.btn_rw.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_rw)

        self.btn_ff = QPushButton(self.pag_2)
        self.btn_ff.setObjectName(u"btn_ff")
        self.btn_ff.setMinimumSize(QSize(26, 18))
        self.btn_ff.setMaximumSize(QSize(26, 18))
        self.btn_ff.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_ff)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.lb_timestamp_res = QLabel(self.pag_2)
        self.lb_timestamp_res.setObjectName(u"lb_timestamp_res")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_timestamp_res.sizePolicy().hasHeightForWidth())
        self.lb_timestamp_res.setSizePolicy(sizePolicy1)
        self.lb_timestamp_res.setMinimumSize(QSize(90, 20))
        self.lb_timestamp_res.setMaximumSize(QSize(90, 20))
        self.lb_timestamp_res.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_timestamp_res)

        self.btn_c = QPushButton(self.pag_2)
        self.btn_c.setObjectName(u"btn_c")
        self.btn_c.setMinimumSize(QSize(26, 18))
        self.btn_c.setMaximumSize(QSize(26, 18))
        self.btn_c.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_c)

        self.stw.addWidget(self.pag_2)

        self.horizontalLayout_3.addWidget(self.stw)

        self.btn_toggle = QPushButton(self.fm_botones)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(26, 18))
        self.btn_toggle.setMaximumSize(QSize(26, 18))
        self.btn_toggle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_toggle)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.fm_botones)

        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SkinPlayer)

        self.stw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SkinPlayer)
    # setupUi

    def retranslateUi(self, SkinPlayer):
        SkinPlayer.setWindowTitle(QCoreApplication.translate("SkinPlayer", u"Form", None))
        self.btn_play.setText(QCoreApplication.translate("SkinPlayer", u"P", None))
        self.lb_time.setText(QCoreApplication.translate("SkinPlayer", u"00:00:00", None))
        self.lb_vol.setText(QCoreApplication.translate("SkinPlayer", u"100", None))
        self.btn_stop.setText(QCoreApplication.translate("SkinPlayer", u"S", None))
        self.lb_timestamp.setText(QCoreApplication.translate("SkinPlayer", u"00:00:00.000", None))
        self.btn_left.setText(QCoreApplication.translate("SkinPlayer", u"<", None))
        self.btn_right.setText(QCoreApplication.translate("SkinPlayer", u">", None))
        self.btn_rw.setText(QCoreApplication.translate("SkinPlayer", u"R", None))
        self.btn_ff.setText(QCoreApplication.translate("SkinPlayer", u"F", None))
        self.lb_timestamp_res.setText(QCoreApplication.translate("SkinPlayer", u"00:00:00.000", None))
        self.btn_c.setText(QCoreApplication.translate("SkinPlayer", u"C", None))
        self.btn_toggle.setText(QCoreApplication.translate("SkinPlayer", u"T", None))
    # retranslateUi

