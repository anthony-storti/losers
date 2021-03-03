#import sqlite
import os
import subprocess
import sqlite3
from sqlite3 import Error

# connecting with the database and making the error handler


def sqliteConnect():
    try:
        cur = sqlite3.connect('data.db')
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

def initDb():
    os.system("sqlite3 data.db \".read create.sql\" \".mode csv\" \".import Losers.csv Losers\" \".import Insults.csv Insults\"")


def fetch(cur, userInput, table="null", column="null", id="null"):
    cursor = cur.cursor()
    if table == "null":
        script = "SELECT tweet FROM Insults i, Losers l Where l.loser_id = i.loser_id  AND l.name = " +"\""+userInput+"\""
        cursor.execute(script)
        row = cursor.fetchone()
        if not (row is None):
            return row[0]
        else:
            return "Result not found!"

    script = "SELECT "+column+" FROM "+table+" WHERE "+id+" = "+"\""+userInput+"\""
    cursor.execute(script)
    row = cursor.fetchone()
    if not (row is None):
        return row[0]
    else:
        return "Result not found!"


def fetchAllQueries(cur):
    cursor = cur.cursor()
    script = "SELECT * FROM Insults"
    script1 = "SELECT * FROM Losers"
    cursor.execute(script)
    insultTable = cursor.fetchall()
    cursor.execute(script1)
    loserTable = cursor.fetchall()
    if not (insultTable is None and loserTable is None):
        return insultTable, loserTable
    else:
        return "Result not found!"

def dropTables(cur):
    cur.commit()
    cur.close()
    subprocess.call("rm data.db")


