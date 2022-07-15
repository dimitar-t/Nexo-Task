from urllib.parse import _ResultMixinStr
from flask import Flask
import mysql.connector
import os


app = Flask(__name__)
db = mysql.connector.connect(
    host="mysql",
    user="nexo",
    password=open(os.environ.get("MYSQL_PASSWORD")).read(),
    database="nexo-db",
    port="3306"
)


@app.route("/")
def index():
    return "Hello, Nexo!"

@app.route("/db")
def get_db():
    if db.is_connected():
        return "Successfully connected to MySQL database"
    else:
        return "There is a problem with the MySQL connection"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
