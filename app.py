import os
from flask import Flask, render_template, session, redirect, url_for, request, session, flash, jsonify
from werkzeug.utils import secure_filename
from models.model import db
from models.plane import Plane
from models.plane_images import PlaneImages

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/airsim"
db.init_app(app)

if app.config['DEBUG']:
    app.config.from_object('config_local')
else:
    app.config.from_object('config_prod')

@app.route("/")
def index():
    if 'login' in session:
        return render_template("index.html", page_title='Dashboard')
    return redirect(url_for('login'))

@app.route("/planes/add")
def add_plane():
    if 'login' in session:
        return render_template("planes/add.html", page_title='Add Plane')
    return redirect(url_for('login'))

@app.route("/planes", methods=['GET'])
def planes():
    if 'login' in session:
        planes = Plane.query.all()
        return render_template("planes/index.html", page_title='View Planes', planes=planes)
    return redirect(url_for('login'))

@app.route("/planes/<int:plane_id>", methods=['GET'])
def show_plane(plane_id):
    if 'login' in session:
        plane = Plane.query.get_or_404(plane_id)
        return render_template("planes/show.html", page_title='Plane Details', plane=plane)
    return redirect(url_for('login'))

@app.route("/planes/save", methods=['POST'])
def save_plane():
    if 'login' in session:
        form_data = request.form
        plane = Plane(**form_data)
        db.session.add(plane)
        db.session.commit()
        flash('Plane saved')
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route("/planes/upload-image", methods=['POST'])
def upload_image():
    image = request.files['plane_image']
    filename = secure_filename(image.filename)
    image.save(os.path.join('plane_images/', filename))
    return redirect(url_for('planes'))

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