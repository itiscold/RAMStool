# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SafetyData.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SafetyDataPage(object):
    def setupUi(self, SafetyDataPage):
        SafetyDataPage.setObjectName("SafetyDataPage")
        SafetyDataPage.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(SafetyDataPage)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(SafetyDataPage)
        self.label_10.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_time = QtWidgets.QLineEdit(SafetyDataPage)
        self.lineEdit_time.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.gridLayout_2.addWidget(self.lineEdit_time, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(SafetyDataPage)
        self.label_11.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_interval = QtWidgets.QLineEdit(SafetyDataPage)
        self.lineEdit_interval.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_interval.setObjectName("lineEdit_interval")
        self.gridLayout_2.addWidget(self.lineEdit_interval, 3, 1, 1, 1)
        self.button_search = QtWidgets.QPushButton(SafetyDataPage)
        self.button_search.setMaximumSize(QtCore.QSize(150, 16777215))
        self.button_search.setObjectName("button_search")
        self.gridLayout_2.addWidget(self.button_search, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(SafetyDataPage)
        self.label_12.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.lineEdit_station = QtWidgets.QLineEdit(SafetyDataPage)
        self.lineEdit_station.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_station.setObjectName("lineEdit_station")
        self.gridLayout_2.addWidget(self.lineEdit_station, 2, 1, 1, 1)
        self.lineEdit_date = QtWidgets.QLineEdit(SafetyDataPage)
        self.lineEdit_date.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.gridLayout_2.addWidget(self.lineEdit_date, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(SafetyDataPage)
        self.label_9.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(SafetyDataPage)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 5, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(SafetyDataPage)
        self.table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.horizontalHeader().setMinimumSectionSize(80)
        self.table.verticalHeader().setDefaultSectionSize(40)
        self.table.verticalHeader().setMinimumSectionSize(40)
        self.gridLayout.addWidget(self.table, 0, 1, 1, 1)

        self.retranslateUi(SafetyDataPage)
        QtCore.QMetaObject.connectSlotsByName(SafetyDataPage)

    def retranslateUi(self, SafetyDataPage):
        _translate = QtCore.QCoreApplication.translate
        SafetyDataPage.setWindowTitle(_translate("SafetyDataPage", "数据查询"))
        self.label_10.setText(_translate("SafetyDataPage", "时间段"))
        self.label_11.setText(_translate("SafetyDataPage", "车站"))
        self.button_search.setText(_translate("SafetyDataPage", "查看"))
        self.label_12.setText(_translate("SafetyDataPage", "区间"))
        self.label_9.setText(_translate("SafetyDataPage", "日期"))
        self.pushButton.setText(_translate("SafetyDataPage", "下载"))

