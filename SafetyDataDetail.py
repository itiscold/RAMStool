import codecs
import datetime

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView, QTableWidget, QTableWidgetItem
from SafetyData import Ui_SafetyDataPage
import numpy as np

TIME_NAME_LIST = ['6:00-9:00','9:00-12:00','12:00-15:00',
                               '15:00-18:00','18:00-21:00','21:00-24:00',]

def out_date_by_day(year,day):
    '''
    根据输入的年份和天数计算对应的日期
    '''
    first_day=datetime.datetime(year,1,1)
    add_day=datetime.timedelta(days=day-1)
    return datetime.datetime.strftime(first_day+add_day,"%m.%d")


def get_interval_station_name_id(interval_file_name):
    f = codecs.open(interval_file_name, 'rb', 'utf-8')
    lines = f.readlines()
    f.close()
    interval_nums = len(lines)
    interval_id_map = {}  # dict,记录区间与区间id的对应关系，key:入站id_出站id value:id
    stationId2names = {}  # stationId2names数组记录车站id与车站名称的对应关系,id从1开始算
    names2stationId = {}  # names2stationId数组记录车站名称与车站id的对应关系
    id_interval_map = {}  # 记录interval_id 与 区间的关系，value:入站_id_出站id
    names = set()  # names容器记录所有存在的车站名称(不支持索引)
    for i in range(1, len(lines)):  # 记录车站名称和id信息,并生成连接图graph
        tmp = lines[i].strip().split('\t')
        inStationId = int(tmp[1], 10)
        outStationId = int(tmp[2], 10)
        interval_id = int(tmp[0], 10)
        interval_id_map[str(inStationId) + '_' + str(outStationId)] = interval_id
        interval_id_map[str(outStationId) + '_' + str(inStationId)] = interval_id + interval_nums - 1
        id_interval_map[interval_id] = str(inStationId) + '_' + str(outStationId)
        id_interval_map[interval_id + interval_nums - 1] = str(outStationId) + '_' + str(inStationId)

        if tmp[5] not in names:  # 记录新车站信息
            names.add(tmp[5])
            stationId2names[inStationId] = tmp[5]  # 记录车站名称与车站id的彼此对应关系
            names2stationId[tmp[5]] = inStationId

        if tmp[6] not in names:
            names.add(tmp[6])
            stationId2names[outStationId] = tmp[6]
            names2stationId[tmp[6]] = outStationId

    return [interval_id_map, id_interval_map, stationId2names, names2stationId]


def get_day_time_trisk_data(day_str, time_str, station_name, interval_name): # 核心模块提供
    day_index = 15
    time_index = TIME_NAME_LIST.index(time_str)
    risk_index = day_index * 6 + time_index

    station_risk = np.load("station_risk_all.npy")
    interval_risk = np.load("interval_risk_all.npy")
    [interval_id_map, id_interval_map, stationId2names, names2stationId] = \
        get_interval_station_name_id("config\intervals.txt")
    station_pos = []
    if len(station_name) == 0:
        station_pos = range(station_risk.shape[0])
    else:
        station_pos.append(names2stationId[station_name] - 1)

    station_name_list = [stationId2names[i + 1] for i in station_pos]
    interval_name_list = []
    interval_pos = []
    for i in range(interval_risk.shape[0]):
        index = i + 1
        station_id_list = id_interval_map[index].split('_')
        name = stationId2names[int(station_id_list[0])] + '_' + \
            stationId2names[int(station_id_list[1])]
        if len(interval_name) == 0:
            interval_name_list.append(name)
            interval_pos.append(i)
        else:
            if interval_name == name:
                interval_pos.append(i)
                interval_name_list.append(name)
    first_col = station_name_list + interval_name_list + ['合计']
    show_data = np.append(station_risk[station_pos,risk_index], interval_risk[interval_pos,risk_index])
    show_data = np.append(show_data, np.sum(show_data))
    show_data = np.array([show_data])
    show_data= show_data.reshape(-1,1)
    return [first_col, show_data]


def get_day_trisk_data(day_str, station_name, interval_name):
    day = 15
    risk_pos = [i for i in range(day * 6, (day + 1) * 6)]
    station_risk = np.load("station_risk_all.npy")
    interval_risk = np.load("interval_risk_all.npy")
    [interval_id_map, id_interval_map, stationId2names, names2stationId] = \
        get_interval_station_name_id("config\intervals.txt")
    station_pos = []
    if len(station_name) == 0:
        station_pos = [i for i in range(station_risk.shape[0])]
    else:
        station_pos.append(names2stationId[station_name] - 1)

    station_name_list = [stationId2names[i + 1] for i in station_pos]
    interval_name_list = []
    interval_pos = []
    for i in range(interval_risk.shape[0]):
        index = i + 1
        station_id_list = id_interval_map[index].split('_')
        name = stationId2names[int(station_id_list[0])] + '_' + \
               stationId2names[int(station_id_list[1])]
        if len(interval_name) == 0:
            interval_name_list.append(name)
            interval_pos.append(i)
        else:
            if interval_name == name:
                interval_pos.append(i)
                interval_name_list.append(name)

    first_col = station_name_list + interval_name_list
    station_risk_show = station_risk[station_pos,:]
    station_risk_show = station_risk_show[:, risk_pos]

    interval_risk_show = interval_risk[interval_pos,:]
    interval_risk_show = interval_risk_show[:, risk_pos]
    if len(station_pos) == 0:
        station_risk_show = np.array([station_risk_show]).T
    if len(interval_pos) == 0:
        interval_risk_show = np.array([interval_risk_show]).T
    show_data = np.vstack((station_risk_show, interval_risk_show))
    col_sum = np.array([np.sum(show_data, axis=1)]).T
    show_data = np.hstack((show_data, col_sum))
    return [first_col, show_data]


def get_s_i_trisk_data(station_name, interval_name):
    station_risk = np.load("station_risk_all.npy")
    interval_risk = np.load("interval_risk_all.npy")
    [interval_id_map, id_interval_map, stationId2names, names2stationId] = \
        get_interval_station_name_id("config\intervals.txt")
    if len(station_name) != 0:
        s_index = (names2stationId[station_name] - 1)
        show_data = station_risk[s_index]
    else:
        for i in range(interval_risk.shape[0]):
            index = i + 1
            station_id_list = id_interval_map[index].split('_')
            name = stationId2names[int(station_id_list[0])] + '_' + \
                   stationId2names[int(station_id_list[1])]
            if interval_name == name:
                interval_index = i
                break
        show_data = interval_risk[interval_index]

    first_col = [out_date_by_day(2017,i) for i in range(1, 366)]
    show_data = np.reshape(show_data, [365,-1])
    col_sum = np.array([np.sum(show_data, axis=1)]).T
    show_data = np.hstack((show_data, col_sum))
    return [first_col, show_data]


def get_time_trisk_data(time_str, station_name, interval_name):
    time_index = TIME_NAME_LIST.index(time_str)
    time_pos = [(i * 6 + time_index) for i in range(0,365)]
    station_risk = np.load("station_risk_all.npy")
    interval_risk = np.load("interval_risk_all.npy")
    [interval_id_map, id_interval_map, stationId2names, names2stationId] = \
        get_interval_station_name_id("config\intervals.txt")
    station_pos = []
    if len(station_name) == 0:
        station_pos = range(station_risk.shape[0])
    else:
        station_pos.append(names2stationId[station_name] - 1)

    station_name_list = [stationId2names[i + 1] for i in station_pos]
    interval_name_list = []
    interval_pos = []
    for i in range(interval_risk.shape[0]):
        index = i + 1
        station_id_list = id_interval_map[index].split('_')
        name = stationId2names[int(station_id_list[0])] + '_' + \
               stationId2names[int(station_id_list[1])]
        if len(interval_name) == 0:
            interval_name_list.append(name)
            interval_pos.append(i)
        else:
            if interval_name == name:
                interval_pos.append(i)
                interval_name_list.append(name)

    first_col = [out_date_by_day(2017, i) for i in range(1, 366)]
    # show_data = station_risk[:,time_pos].T
    station_risk_show = station_risk[station_pos, :]
    station_risk_show = station_risk_show[:, time_pos]
    interval_risk_show = interval_risk[interval_pos, :]
    interval_risk_show = interval_risk_show[:, time_pos]
    if len(station_pos) == 0:
        station_risk_show = np.array([station_risk_show]).T
    if len(interval_pos) == 0:
        interval_risk_show = np.array([interval_risk_show]).T
    show_data = np.vstack((station_risk_show, interval_risk_show)).T

    # col_sum = np.array([np.sum(show_data, axis=1)]).T
    # show_data = np.hstack((show_data, col_sum))
    return [['日期']+station_name_list+interval_name_list, first_col, show_data]


class SafetyDataDetail(Ui_SafetyDataPage):
    def __init__(self, p):
        super().setupUi(p)
        self.my_w = p
        self.button_search.clicked.connect(self.begin_search)
        # self.begin_search()

    def begin_search(self):
        print("search")
        day = self.lineEdit_date.text().strip()
        t = self.lineEdit_time.text().strip()
        station_name = self.lineEdit_station.text().strip()
        interval_name = self.lineEdit_interval.text().strip()
        if len(day) != 0: # 日期不为0
            print("day != 0")
            if len(t) != 0:  # 第一种：日期和时刻都有
                print("time != 0")
                table_title = ['车站/区间','风险值']
                [table_first_col,table_context] = get_day_time_trisk_data(day, t, station_name, interval_name)
                print(table_context.shape[0])
                self.print_table(table_title, table_first_col, table_context)
            else:  #第二种：只有日期
                print("time == 0")
                table_title = ['车站/区间','6:00-9:00','9:00-12:00','12:00-15:00',
                               '15:00-18:00','18:00-21:00','21:00-24:00','合计']
                table_title = table_title
                [table_first_col, table_context] = get_day_trisk_data(day, station_name, interval_name)
                self.print_table(table_title, table_first_col, table_context)
        else:  # 日期是0
            print("day = 0")
            if len(t) != 0:   # 第三种：时刻有
                print("time != 0")
                table_title = []
                [table_title, table_first_col, table_context] = get_time_trisk_data(t, station_name, interval_name)
                self.print_table(table_title, table_first_col, table_context)
            else: # 第四种:只有区间和车站
                print("time == 0")
                # station_index = 11
                # interval_index = 10
                table_title = ['日期','6:00-9:00','9:00-12:00','12:00-15:00',
                               '15:00-18:00','18:00-21:00','21:00-24:00','合计']
                [table_first_col, table_context] = get_s_i_trisk_data(station_name,interval_name)
                self.print_table(table_title, table_first_col, table_context)

    def print_table(self, table_title, first_col, table_context):
        # 设置表头以及整个表格的缩放
        rows = table_context.shape[0]
        cols = table_context.shape[1]
        print(rows)
        print(cols)
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols + 1)
        self.table.setHorizontalHeaderLabels(table_title)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        QTableWidget.resizeColumnsToContents(self.table)
        QTableWidget.resizeRowsToContents(self.table)
        self.table.setWordWrap(True)
        # 添加数据
        for i in range(rows):
            x = QTableWidgetItem(first_col[i])
            x.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.table.setItem(i,0,x)
            for j in range(1, cols + 1):
                y = QTableWidgetItem(str(round(table_context[i][j - 1],4)))
                # print(str(table_context[i][j - 1]))
                y.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.table.setItem(i, j, y)





