from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog, QHeaderView, QAbstractItemView, QTableWidget, QTableWidgetItem
from mainWin import Ui_MainWin
import numpy as np
from SafetyDetail import SafetyDetail
from SafetyDataDetail import SafetyDataDetail


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def get_file(self):
        file_name, s = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)")
        return file_name

    def open_detail_page(self):
        self.detail_page = QtWidgets.QWidget()
        self.detail_ui = SafetyDetail(self.detail_page)
        self.detail_page.show()

    def open_table_page(self):
        self.table_page = QtWidgets.QWidget()
        self.table_ui = SafetyDataDetail(self.table_page)
        self.table_page.show()


class MainWindowUI(Ui_MainWin):
    def __init__(self, w):
        super().setupUi(w)
        self.my_window = w
        self.pushButton_5.clicked.connect(self.choose_file)
        self.button_improve.clicked.connect(self.improve_safety)
        self.button_rams.clicked.connect(self.rams_eva)
        self.button_analyse.clicked.connect(self.show_safety)
        self.pushButton_table.clicked.connect(self.show_table)

    def choose_file(self):
        file_name = self.my_window.get_file()
        self.lineName.setText(file_name)

    def improve_safety(self):
        self.label_improve_pic.setPixmap(QPixmap("E:\\files\\RAMStool\\picture\\improveres.png"))

    def rams_eva(self):
        weight = float(self.trisk_w.text())
        single_risk = 600000
        tran_risk = 45394.98
        a = 0.9594
        r = 0.9594
        m = 5.13
        trisk_rank = np.array([0, 0, 40, 2150])
        trisk_rank_name = np.array(['一级','二级','三级','四级'])
        all_risk = single_risk + weight * tran_risk
        self.trisk.setText(str(tran_risk))
        self.allrisk.setText(str(all_risk))
        self.singrisk.setText(str(single_risk))
        self.a_res.setText(str(a))
        self.r_res.setText(str(r))
        self.m_res.setText(str(m))
        self.trisk_rank.setHorizontalHeaderLabels(['等级', '个数'])
        self.trisk_rank.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.trisk_rank.setEditTriggers(QAbstractItemView.NoEditTriggers)
        QTableWidget.resizeColumnsToContents(self.trisk_rank)
        QTableWidget.resizeRowsToContents(self.trisk_rank)
        for i in np.arange(4):
            # 为每个表格内添加数据
            # print(trisk_rank_name[i])
            x = QTableWidgetItem(trisk_rank_name[i])
            x.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.trisk_rank.setItem(i, 0, x)
            y = QTableWidgetItem(str(trisk_rank[i]))
            y.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.trisk_rank.setItem(i, 1, y)

    def show_safety(self):
        # self.my_window.open_detail_page()
        self.detail_page = QtWidgets.QWidget()
        self.detail_ui = SafetyDetail(self.detail_page)
        self.detail_page.show()

    def show_table(self):
        # self.my_window.open_table_page()
        self.table_page = QtWidgets.QWidget()
        self.table_ui = SafetyDataDetail(self.table_page)
        self.table_page.show()


if __name__ == "__main__":
    import sys
    #from PyQt5.QtGui import QIcon
    app=QtWidgets.QApplication(sys.argv)
    # widget= QtWidgets.QWidget()
    widget = MyWindow()
    ui = MainWindowUI(widget)
    # safety_data_detail_page = QtWidgets.QWidget()
    # safety_data_detail_page_ui = SafetyDataDetail(safety_data_detail_page)
    widget.show()
    sys.exit(app.exec_())