# blog.py - controller

# imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g

import sqlite3

DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'cm\xe2\x00e\xe8\x9b\t&u]1\x16n:*\xfe\xbc\t\x90*{\xcfM'


app = Flask(__name__)

app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'INVALID Credentials. Please Keep Trying.'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error), status_code


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/logout')
def logout():
    session.pop('logged in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)