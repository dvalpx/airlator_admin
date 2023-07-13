import os
from flask import Flask, render_template, session, redirect, url_for, request, session, flash, jsonify
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect
from controllers.planes import planes_controller
from models.model import db
from models.plane import Plane
from models.plane_images import PlaneImages

app = Flask(__name__)
config_default = 'config_prod'

if app.config['DEBUG']:
    config_default = 'config_local'

app.config.from_object(config_default)
app.register_blueprint(planes_controller)
db.init_app(app)
csrf = CSRFProtect(app)

@app.route("/")
def index():
    if 'login' in session:
        return render_template("index.html", page_title='Dashboard')
    return redirect(url_for('login'))

@app.route("/planes/<int:plane_id>/upload-image", methods=['POST'])
def upload_image():
    image = request.files['plane_image']
    filename = secure_filename(image.filename)
    image.save(os.path.join('plane_images/', filename))
    return redirect(url_for('planes'))

@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # Just for local testing purposes - will be replaced
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
