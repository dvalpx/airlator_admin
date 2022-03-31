import pymysql

def mysqlconn():
    return pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        db = 'airsim'
    )

def get_airports():
    conn = mysqlconn()
    airports = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT name FROM airports")
        airports = cursor.fetchall()
    conn.close()
    return airports

def get_planes():
    conn = mysqlconn()
    planes = []
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM planes")
        planes = cursor.fetchall()
    conn.close()
    return planes

def get_plane(plane_id):
    conn = mysqlconn()
    plane = None
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM planes WHERE id = %s", (plane_id,))
        plane = cursor.fetchone()
    conn.close()
    return plane

def save_plane(plane):
    conn = mysqlconn()
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO planes(
                manufacturer,
                model,
                length,
                wingspan, 
                height,
                wing_area,
                maximum_take_off_weight,
                maximum_landing_weight,
                maximum_zero_fuel_weight,
                maximum_payload,
                standard_fuel_capacity,
                max_stock_of_fuel,
                maximum_range,
                cruise_speed,
                maximum_speed,
                maximum_operating_altitude,
                take_off_field_length,
                landing_field_length,
                engines,
                fuel_efficiency,
                fuel_flow_rate,
                passengers_1_class,
                passengers_2_class,
                passengers_3_class,
                cabin_width,
                cabin_height,
                additional_fields) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                plane['manufacturer'],
                plane['model'],
                plane['length'],
                plane['wingspan'], 
                plane['height'],
                plane['wing_area'],
                plane['maximum_take_off_weight'],
                plane['maximum_landing_weight'],
                plane['maximum_zero_fuel_weight'],
                plane['maximum_payload'],
                plane['standard_fuel_capacity'],
                plane['max_stock_of_fuel'],
                plane['maximum_range'],
                plane['cruise_speed'],
                plane['maximum_speed'],
                plane['maximum_operating_altitude'],
                plane['take_off_field_length'],
                plane['landing_field_length'],
                plane['engines'],
                plane['fuel_efficiency'],
                plane['fuel_flow_rate'],
                plane['passengers_1_class'],
                plane['passengers_2_class'],
                plane['passengers_3_class'],
                plane['cabin_width'],
                plane['cabin_height'],
                plane['additional_fields']
            )
        )
    conn.commit()
    conn.close()
    return True
