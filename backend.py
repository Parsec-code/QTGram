import sqlite3
from hashlib import sha256
from New_except import *
import random
import http.client
import ssl
import json


def reg(lo, pa):
    conn = sqlite3.connect('db.sqlite', check_same_thread=False)
    cur = conn.cursor()
    password = sha256(pa.encode()).hexdigest()
    sql = 'SELECT EXISTS (SELECT 1 FROM users WHERE username = ?)'
    cur.execute(sql, (lo,))
    if cur.fetchone()[0]:
        raise Exist("Username already exists")
    else:
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                    (lo, password))
        u_id = cur.execute('SELECT user_id FROM users WHERE username=? AND password=?', (lo, password)).fetchone()[0]
        score = 0
        cur.execute('INSERT INTO stats (user_id, score) VALUES (?, ?)', (u_id, score,))
        res = cur.execute("SELECT user_id FROM users WHERE username=? AND password=?", (lo, password)).fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return res


def log(lo, pa):
    conn = sqlite3.connect('db.sqlite', check_same_thread=False)
    cur = conn.cursor()
    password = sha256(pa.encode()).hexdigest()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (lo, password))
    user = cur.fetchone()
    if user:
        res = cur.execute("SELECT user_id FROM users WHERE username=? AND password=?", (lo, password)).fetchone()[0]
        cur.close()
        conn.close()
        return res
    else:
        cur.close()
        conn.close()
        raise Invalid("Invalid username or password.")


def set_word():
    # Требует оптимизации и создании статичного списка
    with open('russian.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        res = random.choice(lines)
    return res


def score_change(current):
    res = current + 1
    return res


def initialize(user_id):
    conn = sqlite3.connect('db.sqlite', check_same_thread=False)
    cur = conn.cursor()
    res = cur.execute("SELECT score FROM stats WHERE user_id=?", (user_id,)).fetchone()[0]
    user = cur.fetchone()
    cur.close()
    conn.close()
    return res


def save_res(score, user_id):
    conn = sqlite3.connect('db.sqlite', check_same_thread=False)
    cur = conn.cursor()
    cur.execute("UPDATE stats SET score=? WHERE user_id=?", (score, user_id,))
    conn.commit()
    cur.close()
    conn.close()


def stat():
    conn = sqlite3.connect('db.sqlite', check_same_thread=False)
    cur = conn.cursor()
    res = cur.execute("SELECT user_id, score FROM stats LIMIT 11")
    cur.close()
    conn.close()
    return res
