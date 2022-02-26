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