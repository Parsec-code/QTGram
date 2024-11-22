import requests
from PyQt6.QtWidgets import *
import sys
import backend
import os.path
import sqlite3
from frontQT import *

if not os.path.isfile('russian.txt'):
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

    text = response.content.decode('cp1251')

    with open('russian.txt', 'wb') as ru:
        ru.read(12)
        ru.write(text.encode('utf-8'))


def create_users():
    conn = sqlite3.connect('db.sqlite', check_same_thread=False)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
        )
        ''')
    conn.commit()
    cur.close()
    conn.close()


def create_stats():
    conn = sqlite3.connect('db.sqlite', check_same_thread=False)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS stats (
        stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER NOT NULL DEFAULT(0),
        user_id INTEGER REFERENCES users(user_id) NOT NULL
        )
        ''')
    conn.commit()
    cur.close()
    conn.close()


def main():
    create_users()
    create_stats()


if __name__ == '__main__':
    main()
    app = QApplication(sys.argv)
    w = Menu()
    sys.excepthook = except_hook
    w.show()
    sys.exit(app.exec())
