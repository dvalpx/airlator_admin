from models.model import db

class PlaneImages(db.Model):
    __tablename__ = 'planes_images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=True)
    license_type = db.Column(db.String(100), nullable=True)
    author = db.Column(db.String(50), nullable=True)
    original_location = db.Column(db.Text, nullable=True)