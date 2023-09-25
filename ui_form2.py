# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 1000)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 810, 990, 52))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(148, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 50))
        font = QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(138, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 50))
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(158, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 50))
        self.pushButton_3.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer_4 = QSpacerItem(208, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 150, 1001, 602))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.graphicsView = QGraphicsView(self.layoutWidget1)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(800, 600))

        self.horizontalLayout_2.addWidget(self.graphicsView)

        self.horizontalSpacer_6 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 911, 970, 52))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(568, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 50))
        self.pushButton_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.horizontalSpacer_8 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 50))
        self.pushButton_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.horizontalSpacer_9 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(4, 50, 991, 53))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 50))
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)

        self.textEdit = QTextEdit(self.widget1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(400, 51))
        self.textEdit.setMaximumSize(QSize(400, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.textEdit.setFont(font1)

        self.horizontalLayout_4.addWidget(self.textEdit)

        self.toolButton = QToolButton(self.widget1)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(100, 50))
        font2 = QFont()
        font2.setFamily(u"Adobe \u5b8b\u4f53 Std L")
        font2.setPointSize(18)
        self.toolButton.setFont(font2)

        self.horizontalLayout_4.addWidget(self.toolButton)

        self.horizontalSpacer_11 = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6298\u7ebf\u56fe", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6563\u70b9\u56fe", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5706\u997c\u56fe", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8def\u5f84", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
    # retranslateUi
