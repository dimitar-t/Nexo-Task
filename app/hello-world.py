from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

if (os.environ.get("ENVIRONMENT") == "local"):
    mysql_password = open(os.environ.get("MYSQL_PASSWORD")).read()
else:
    mysql_password = os.environ.get("MYSQL_PASSWORD")

db = mysql.connector.connect(
    host="mysql",
    database="nexo-db",
    user="nexo",
    password=mysql_password
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
