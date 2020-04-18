# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SafetyPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SafetyPage(object):
    def setupUi(self, SafetyPage):
        SafetyPage.setObjectName("SafetyPage")
        SafetyPage.resize(658, 600)
        self.gridLayout_3 = QtWidgets.QGridLayout(SafetyPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(SafetyPage)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(SafetyPage)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.time_risk = QtWidgets.QLabel(SafetyPage)
        self.time_risk.setMinimumSize(QtCore.QSize(320, 240))
        self.time_risk.setText("")
        self.time_risk.setObjectName("time_risk")
        self.gridLayout.addWidget(self.time_risk, 1, 0, 1, 1)
        self.day_risk = QtWidgets.QLabel(SafetyPage)
        self.day_risk.setMinimumSize(QtCore.QSize(320, 240))
        self.day_risk.setText("")
        self.day_risk.setObjectName("day_risk")
        self.gridLayout.addWidget(self.day_risk, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(SafetyPage)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(SafetyPage)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.station_risk = QtWidgets.QLabel(SafetyPage)
        self.station_risk.setMinimumSize(QtCore.QSize(320, 240))
        self.station_risk.setText("")
        self.station_risk.setObjectName("station_risk")
        self.gridLayout.addWidget(self.station_risk, 3, 0, 1, 1)
        self.interval_risk = QtWidgets.QLabel(SafetyPage)
        self.interval_risk.setMinimumSize(QtCore.QSize(320, 240))
        self.interval_risk.setText("")
        self.interval_risk.setObjectName("interval_risk")
        self.gridLayout.addWidget(self.interval_risk, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.retranslateUi(SafetyPage)
        QtCore.QMetaObject.connectSlotsByName(SafetyPage)

    def retranslateUi(self, SafetyPage):
        _translate = QtCore.QCoreApplication.translate
        SafetyPage.setWindowTitle(_translate("SafetyPage", "安全性分析"))
        self.label_3.setText(_translate("SafetyPage", "总风险最高的时间段（五个）"))
        self.label_4.setText(_translate("SafetyPage", "风险最高的日期（五天）"))
        self.label_5.setText(_translate("SafetyPage", "总最高的车站（五个）"))
        self.label_7.setText(_translate("SafetyPage", "总风险最高的区间（五个）"))

