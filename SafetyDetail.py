from PyQt5.QtGui import QPixmap
from SafetyPage import Ui_SafetyPage


class SafetyDetail(Ui_SafetyPage):
    def __init__(self, s):
        super().setupUi(s)
        self.my_window = s
        time_risk_pic = QPixmap("E:\\files\\RAMStool\\picture\\time.png")
        print(self.time_risk.width())
        print(self.time_risk.height())

        # time_risk_fixpic = time_risk_pic.scaled(self.time_risk.width(), self.time_risk.height(),
        #                                         aspectRatioMode=Qt.KeepAspectRatio)
        day_risk_pic = QPixmap("E:\\files\\RAMStool\\picture\\date.png")
        station_risk_pic = QPixmap("E:\\files\\RAMStool\\picture\\station.png")
        interval_risk_pic = QPixmap("E:\\files\\RAMStool\\picture\\interval.png")
        # self.time_risk.setScaledContents(True)
        self.time_risk.setPixmap(time_risk_pic)
        self.day_risk.setPixmap(day_risk_pic)
        self.station_risk.setPixmap(station_risk_pic)
        self.interval_risk.setPixmap(interval_risk_pic)


