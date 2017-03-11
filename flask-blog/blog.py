# blog.py - controller

# imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from functools import  wraps

import sqlite3

DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'cm\xe2\x00e\xe8\x9b\t&u]1\x16n:*\xfe\xbc\t\x90*{\xcfM'


app = Flask(__name__)

app.config.from_object(__name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))
    return wrap


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
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute('SELECT  * from posts')
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html', posts=posts)


@app.route('/logout')
def logout():
    session.pop('logged in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All Fields are required. Please correct and try again")
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute('insert into posts (title, post) VALUES (?, ?)',
        [request.form['title'], request.form['post']])
        g.db.commit()
        g.db.close()
        flash('New Entry was successfully posted!')
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)