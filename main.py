from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 499)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.zapros = QtWidgets.QPushButton(self.centralwidget)
        self.zapros.setGeometry(QtCore.QRect(650, 10, 141, 51))
        self.zapros.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.zapros.setObjectName("zapros")
        self.vsego_matchey = QtWidgets.QLabel(self.centralwidget)
        self.vsego_matchey.setGeometry(QtCore.QRect(10, 80, 601, 51))
        self.vsego_matchey.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.vsego_matchey.setIndent(5)
        self.vsego_matchey.setObjectName("vsego_matchey")
        self.vsego_pobed = QtWidgets.QLabel(self.centralwidget)
        self.vsego_pobed.setGeometry(QtCore.QRect(10, 150, 601, 51))
        self.vsego_pobed.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.vsego_pobed.setIndent(5)
        self.vsego_pobed.setObjectName("vsego_pobed")
        self.procent_pobed = QtWidgets.QLabel(self.centralwidget)
        self.procent_pobed.setGeometry(QtCore.QRect(10, 220, 601, 51))
        self.procent_pobed.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.procent_pobed.setIndent(5)
        self.procent_pobed.setObjectName("procent_pobed")
        self.bomb_plated = QtWidgets.QLabel(self.centralwidget)
        self.bomb_plated.setGeometry(QtCore.QRect(10, 290, 601, 51))
        self.bomb_plated.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.bomb_plated.setIndent(5)
        self.bomb_plated.setObjectName("bomb_plated")
        self.bomb_defused = QtWidgets.QLabel(self.centralwidget)
        self.bomb_defused.setGeometry(QtCore.QRect(10, 360, 601, 51))
        self.bomb_defused.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.bomb_defused.setIndent(5)
        self.bomb_defused.setObjectName("bomb_defused")
        self.vsego_matchey_2 = QtWidgets.QLabel(self.centralwidget)
        self.vsego_matchey_2.setGeometry(QtCore.QRect(660, 80, 131, 51))
        self.vsego_matchey_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.vsego_matchey_2.setText("")
        self.vsego_matchey_2.setIndent(5)
        self.vsego_matchey_2.setObjectName("vsego_matchey_2")
        self.vsego_pobed_2 = QtWidgets.QLabel(self.centralwidget)
        self.vsego_pobed_2.setGeometry(QtCore.QRect(660, 150, 131, 51))
        self.vsego_pobed_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.vsego_pobed_2.setText("")
        self.vsego_pobed_2.setIndent(5)
        self.vsego_pobed_2.setObjectName("vsego_pobed_2")
        self.procent_pobed_2 = QtWidgets.QLabel(self.centralwidget)
        self.procent_pobed_2.setGeometry(QtCore.QRect(660, 220, 131, 51))
        self.procent_pobed_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.procent_pobed_2.setText("")
        self.procent_pobed_2.setIndent(5)
        self.procent_pobed_2.setObjectName("procent_pobed_2")
        self.bomb_plated_2 = QtWidgets.QLabel(self.centralwidget)
        self.bomb_plated_2.setGeometry(QtCore.QRect(660, 290, 131, 51))
        self.bomb_plated_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.bomb_plated_2.setText("")
        self.bomb_plated_2.setIndent(5)
        self.bomb_plated_2.setObjectName("bomb_plated_2")
        self.bomb_defused_2 = QtWidgets.QLabel(self.centralwidget)
        self.bomb_defused_2.setGeometry(QtCore.QRect(660, 360, 131, 51))
        self.bomb_defused_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.bomb_defused_2.setText("")
        self.bomb_defused_2.setIndent(5)
        self.bomb_defused_2.setObjectName("bomb_defused_2")
        self.data_time = QtWidgets.QLabel(self.centralwidget)
        self.data_time.setGeometry(QtCore.QRect(10, 430, 601, 51))
        self.data_time.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.data_time.setText("")
        self.data_time.setIndent(5)
        self.data_time.setObjectName("data_time")
        self.pole_zaprosa = QtWidgets.QLineEdit(self.centralwidget)
        self.pole_zaprosa.setGeometry(QtCore.QRect(10, 10, 621, 51))
        self.pole_zaprosa.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pole_zaprosa.setObjectName("pole_zaprosa")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.poisk()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zapros.setText(_translate("MainWindow", "Поиск"))
        self.vsego_matchey.setText(_translate("MainWindow", "Всего матчей сыграно"))
        self.vsego_pobed.setText(_translate("MainWindow", "Всего матчей выиграно:"))
        self.procent_pobed.setText(_translate("MainWindow", "Процент побед:"))
        self.bomb_plated.setText(_translate("MainWindow", "Всего заложено бомб:"))
        self.bomb_defused.setText(_translate("MainWindow", "Всего разминировано бомб:"))

    def go(self):
        ssulka = self.pole_zaprosa.text()
        acc_id = ssulka[36:]
        try:
            requests_main = requests.get(f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=A8F344C924ADF251D79C33006F51ABF0&steamid={acc_id}')
            requests_stats = requests_main.json()
            stat = requests_stats['playerstats']['stats']
            self.vsego_matchey_2.setText(str(stat[128]['value']))
            self.vsego_pobed_2.setText(str(stat[127]['value']))
            self.procent_pobed_2.setText(str(round(stat[127]['value']/stat[128]['value'],2))[2:])
            self.bomb_plated_2.setText(str(stat[3]['value']))
            self.bomb_defused_2.setText(str(stat[4]['value']))
        except:
            self.pole_zaprosa.setText('')
            self.data_time.setText('Ошибка.Проверьте правильность ссылки!')


    def poisk(self):
        self.zapros.clicked.connect(lambda: self.go())




if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())