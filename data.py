#import sqlite
import os
import sqlite3
from sqlite3 import Error

# connecting with the database and making the error handler


def sqliteConnect():
    try:
        cur = sqlite3.connect('/sqlite/cs205/testing.db')
        return cur
    except Error:
        print(Error)

# defining the insert table for Loser table


def insertLoser(cur, titles):
    cursorObject = cur.cursor()
    cursorObject.execute('''INSERT INTO losers(loser_id, name, twitter_handle, occupation) VALUES(?,?,?,?)''', titles)
    cur.commit()

#defining the insert table for Insult table
def insertInsult(cur, titles):
    cursorObject = cur.cursor()
    cursorObject.execute('''INSERT INTO Insults(insult_id, tweet, data, insult, loser_id) VALUES(?,?,?,?,?)''', titles)
    cur.commit()

# This will flush the tables and read and import csv data through the bash


def flushDb(cur):
    with open('testing.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    stmt = cur.cursor()
    stmt.executescript(sql_script)
    cur.commit()
    os.system("sqlite3 /sqlite/cs205/testing.db \".mode csv\" \".import Losers.csv Losers\"")
    os.system("sqlite3 /sqlite/cs205/testing.db \".mode csv\" \".import Insults.csv Insults\"")
