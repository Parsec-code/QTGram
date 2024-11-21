from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt6.QtWidgets import QAbstractItemView
import sys
import backend
from New_except import *


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        uic.loadUi('GUI/Menu.ui', self)
        self.Authorization.clicked.connect(self.switch_form)
        self.Support.clicked.connect(self.show_sup)

    def switch_form(self):
        self.w = Form()
        self.close()
        self.w.show()

    def show_sup(self):
        self.label.setText('<a style="color:MediumPurple;" href="https://yoomoney.ru/transfer/a2w"> Юмани</a>: '
                           '4100118897844920')
        self.label.setOpenExternalLinks(True)


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/Form.ui', self)
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        self.log_in.setFocus()
        self.verify.clicked.connect(self._reg)
        self.log_in.clicked.connect(self._log_in)
        self.Login.returnPressed.connect(self.Password.setFocus)
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.Password.returnPressed.connect(self._log_in)

    def _reg(self):
        try:
            lo = self.Login.text()
            pa = self.Password.text()
            print(lo, pa)
            if lo == '' or pa == '':
                raise Empty('empty box')
            else:
                u_id = backend.reg(lo, pa)
                self.switch_game(u_id)
        except Empty:
            pass

    def _log_in(self):
        try:
            lo = self.Login.text()
            pa = self.Password.text()
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
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        uic.loadUi('GUI/Game.ui', self)
        self.id_label.setText(f"{u_id}")
        self.point_counter.display(backend.initialize(self.id_label.text()))
        self.input_line.returnPressed.connect(self.compare)
        self.back.clicked.connect(self.back_f)
        self.stop_btn.clicked.connect(self.stop_f)
        self.statistics.clicked.connect(self.show_stat)

    def changelabel(self):
        word = backend.set_word()
        self.input_line.clear()
        self.label.setText(word)

    def compare(self):
        self.label.show()
        if self.label.text() != 'Начать!':
            x, y = self.input_line.text(), self.label.text().strip()
            if x == y:
                current = self.point_counter.value()
                new = backend.score_change(current)
                self.point_counter.display(new)

        self.changelabel()

    def back_f(self):
        self.save()
        self.w = Menu()
        self.close()
        self.w.show()

    def stop_f(self):
        self.label.hide()
        self.save()

    def show_stat(self):
        self.save()
        self.w1 = Stats()
        self.w1.show()

    def save(self):
        backend.save_res(self.point_counter.value(), self.id_label.text())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Stats(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/Stats.ui', self)
        self.setWindowIcon(QtGui.QIcon('GUI/icon.png'))
        self.back.clicked.connect(self.back_f)
        """db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable("stats")
        model.select()
        self.table.setModel(model)"""
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
        self.table.setModel(model)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        # backend.stat()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Stats()
    w.show()
    sys.exit(app.exec())
