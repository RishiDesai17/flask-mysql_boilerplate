from flask import Flask
import pymysql

app = Flask(__name__)

try:
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bank")
    print("Connected to MySQL Database")

except Exception as ex:
    print(ex)

if __name__ == '__main__':
   app.run(debug=True)