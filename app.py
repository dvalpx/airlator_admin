from flask import Flask, render_template, session, redirect, url_for, request, session, flash
# from functions import db

app = Flask(__name__)

app.secret_key = 'h@1nc34/1_&-jhax32Zesh'

@app.route("/")
def index():
    if 'login' in session:
        return render_template("index.html")
    return redirect(url_for('login'))

@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        if request.form['password'] == '123456':
            session['login'] = True
            return redirect(url_for('index'))
        flash('Wrong username or password')
        return redirect(url_for('login'))
    if 'login' in session:
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route("/logout")
def logout():
    if 'login' in session:
        session.pop('login', None)
        return redirect(url_for('login'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()