from PyQt5.uic.properties import QtWidgets

import main_win


class ExampleApp(QtWidgets.QMainWindow, main_win.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
