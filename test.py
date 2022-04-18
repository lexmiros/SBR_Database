from flask import Flask, render_template, url_for, flash, redirect
from forms import BinAddForm, BuggiesAddForm, CattleAddForm, FarmAddForm, MotorbikeAddForm, PaddockAddFrom, QuadbikeAddForm, StaffAddFrom
import pymysql


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = pymysql.connect(host='localhost',
                             user='adminflask',
                             password='adminflask',
                             database='project_db_2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

conn.row_factory = dict_factory
c = conn.cursor()
c.execute("SELECT MAX(VehicleID), Model FROM vehicles;")
posts = c.fetchall()
for post in posts:
    print(post["MAX(VehicleID)"])

