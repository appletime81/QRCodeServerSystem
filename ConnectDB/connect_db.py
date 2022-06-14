import pymysql


# connect to the database
def connect_db():
    db = pymysql.connect(
        host="192.168.0.10",
        user="apple",
        password="816357492nano",
        database="factoryfileinfo",
    )
    return db
