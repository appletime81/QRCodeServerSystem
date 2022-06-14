from connect_db import connect_db


# query data from the database
def query_data(sql):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data