from flask import Flask, redirect, url_for, request
from flask import render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'codetrade'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)

@app.route('/')
def hello():
    return "hello"

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['nm']
        password = request.form['pass']
        #To check if account exists
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account WHERE username = %s AND password = %s',(username,password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for('success', name = username))
        else:
            error = "Invalid login Details"
    return render_template('login.html', error = error)

@app.route('/register',methods = ['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        username = request.form['nm']
        password = request.form['pass']
        print (name ,',',age,',',username,',',password)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO account(Name,age,username,password) VALUES (%s,%s,%s,%s)",(name,age,username,password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template('register.html') 
if __name__ == '__main__':
   app.run()