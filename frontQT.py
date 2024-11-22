from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt6.QtWidgets import QAbstractItemView
import sys
import backend
from New_except import *
from GUI.Menu import Ui_Welcome
from GUI.Form import Ui_Authorization
from GUI.Game import Ui_Game
from GUI.Stats import Ui_Stats


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Welcome()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        self.ui.Authorization.clicked.connect(self.switch_form)
        self.ui.Support.clicked.connect(self.show_sup)

    def switch_form(self):
        self.w = Form()
        self.close()
        self.w.show()

    def show_sup(self):
        self.ui.label.setText('<a style="color:MediumPurple;" href="https://yoomoney.ru/transfer/a2w"> Юмани</a>: '
                              '4100118897844920')
        self.ui.label.setOpenExternalLinks(True)


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        self.ui.log_in.setFocus()
        self.ui.verify.clicked.connect(self._reg)
        self.ui.log_in.clicked.connect(self._log_in)
        self.ui.Login.returnPressed.connect(self.ui.Password.setFocus)
        self.ui.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.Password.returnPressed.connect(self._log_in)

    def _reg(self):
        try:
            lo = self.ui.Login.text()
            pa = self.ui.Password.text()
            if lo == '' or pa == '':
                raise Empty('empty box')
            else:
                u_id = backend.reg(lo, pa)
                self.switch_game(u_id)
        except Empty:
            pass

    def _log_in(self):
        try:
            lo = self.ui.Login.text()
            pa = self.ui.Password.text()
            if lo == '' or pa == '':
                raise Empty('empty box')
            else:
                u_id = backend.log(lo, pa)
                self.switch_game(u_id)
        except Empty:
            pass

    def switch_game(self, u_id):
        self.close()
        self.w2 = Game(u_id)
        self.w2.show()


class Game(QMainWindow):
    def __init__(self, u_id):
        super().__init__()
        self.ui = Ui_Game()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        self.ui.id_label.setText(f"{u_id}")
        self.ui.point_counter.display(backend.initialize(self.ui.id_label.text()))
        self.ui.input_line.returnPressed.connect(self.compare)
        self.ui.back.clicked.connect(self.back_f)
        self.ui.stop_btn.clicked.connect(self.stop_f)
        self.ui.statistics.clicked.connect(self.show_stat)

    def changelabel(self):
        word = backend.set_word()
        self.ui.input_line.clear()
        self.ui.label.setText(word)

    def compare(self):
        self.ui.label.show()
        if self.ui.label.text() != 'Начать!':
            x, y = self.ui.input_line.text(), self.ui.label.text().strip()
            if x == y:
                current = self.ui.point_counter.value()
                new = backend.score_change(current)
                self.ui.point_counter.display(new)

        self.changelabel()

    def back_f(self):
        self.save()
        self.w = Menu()
        self.close()
        self.w.show()

    def stop_f(self):
        self.ui.label.hide()
        self.save()

    def show_stat(self):
        self.save()
        self.w1 = Stats()
        self.w1.show()

    def save(self):
        backend.save_res(self.ui.point_counter.value(), self.ui.id_label.text())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Stats(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Stats()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        self.ui.back.clicked.connect(self.back_f)
        self.statistics()

    def back_f(self):
        self.close()

    def statistics(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable("stats")
        model.select()
        self.ui.table.setModel(model)
        self.ui.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Stats()
    w.show()
    sys.exit(app.exec())
