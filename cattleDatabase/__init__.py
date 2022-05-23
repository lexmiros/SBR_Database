from flask import Flask, render_template, url_for, flash, redirect
import pymysql

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfjkhnfdgjijasdfjk' 

#Database connection information
host_db='localhost' 
user_db='adminflask'
password_db='adminflask'
database_db='project_db_4'
charset_db='utf8mb4'
cursorclass_db =pymysql.cursors.DictCursor

#conn = pymysql.connect(host='localhost', user='adminflask', password='adminflask', database='project_db_3', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

from cattleDatabase import delete_routes, insert_routes, update_routes, view_routes

