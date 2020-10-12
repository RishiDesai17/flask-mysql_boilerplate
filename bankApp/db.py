from flask import current_app, g
from flask.cli import with_appcontext
import pymysql

def get_db():
    if "connection" not in g:
        try:
            g.connection = pymysql.connect(host="localhost", user="root", passwd="", database="bank")
            print("Connected to the MySQL Database")
        except Exception as ex:
            print(ex)

    return g.connection

def init_db():
    connection = get_db()

    try:
        cursor = connection.cursor()
        queries = []
        
        with current_app.open_resource("schema.sql") as sql_file:
            queries = sql_file.read().decode("utf8").split(";")
            queries.pop()
        
        for query in queries:
            print(query)
            cursor.execute(query + ';')
        
        connection.commit()
        cursor.close()
    
    except Exception as ex:
        print(ex)

def close_db():
    connection = g.pop("connection", None)

    if connection is not None:
        connection.close()

def init_app(app):
    init_db()
    app.teardown_appcontext(close_db)