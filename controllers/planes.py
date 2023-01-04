from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from models.model import db
from models.plane import Plane

planes_controller = Blueprint('planes_controller', __name__)

@planes_controller.route("/planes", methods=['GET'])
def index():
    if 'login' in session:
        planes = Plane.query.all()
        return render_template("planes/index.html", page_title='View Planes', planes=planes)
    return redirect(url_for('login'))

@planes_controller.route("/planes/add")
def add():
    if 'login' in session:
        return render_template("planes/add.html", page_title='Add Plane')
    return redirect(url_for('login'))

@planes_controller.route("/planes/<int:plane_id>", methods=['GET'])
def show(plane_id):
    if 'login' in session:
        plane = Plane.query.get_or_404(plane_id)
        return render_template("planes/show.html", page_title='Plane Details', plane=plane)
    return redirect(url_for('login'))

@planes_controller.route("/planes/save", methods=['POST'])
def save():
    if 'login' in session:
        form_data = request.form.to_dict()
        del form_data['csrf_token']
        plane = Plane(**form_data)
        db.session.add(plane)
        db.session.commit()
        flash('Plane saved')
        return redirect(url_for('index'))
    return redirect(url_for('login'))