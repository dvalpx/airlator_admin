from models.model import db

class Plane(db.Model):
    __tablename__ = 'planes'

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(50), nullable=True)
    model = db.Column(db.String(50), nullable=True)
    length = db.Column(db.String(50), nullable=True)
    wingspan = db.Column(db.String(50), nullable=True)
    height = db.Column(db.String(50), nullable=True)
    wing_area = db.Column(db.String(50), nullable=True)
    maximum_take_off_weight = db.Column(db.String(50), nullable=True)
    maximum_landing_weight = db.Column(db.String(50), nullable=True)
    maximum_zero_fuel_weight = db.Column(db.String(50), nullable=True)
    maximum_payload = db.Column(db.String(50), nullable=True)
    standard_fuel_capacity = db.Column(db.String(50), nullable=True)
    max_stock_of_fuel = db.Column(db.String(50), nullable=True)
    maximum_range = db.Column(db.String(50), nullable=True)
    cruise_speed = db.Column(db.String(50), nullable=True)
    maximum_speed = db.Column(db.String(50), nullable=True)
    maximum_operating_altitude = db.Column(db.String(50), nullable=True)
    take_off_field_length = db.Column(db.String(50), nullable=True)
    landing_field_length = db.Column(db.String(50), nullable=True)
    engines = db.Column(db.Text, nullable=True)
    fuel_efficiency = db.Column(db.String(50), nullable=True)
    fuel_flow_rate = db.Column(db.String(50), nullable=True)
    passengers_1_class = db.Column(db.String(50), nullable=True)
    passengers_2_class = db.Column(db.String(50), nullable=True)
    passengers_3_class = db.Column(db.String(50), nullable=True)
    cabin_width = db.Column(db.String(50), nullable=True)
    cabin_height = db.Column(db.String(50), nullable=True)
    additional_fields = db.Column(db.Text, nullable=True)