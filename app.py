from flask import Flask
from flask_mysqldb import MySQL
from routes import register_routes

app = Flask(__name__)
app.secret_key = 'your-secret-key'
app.config.from_pyfile('config.py')

mysql = MySQL(app)
register_routes(app, mysql)

if __name__ == '__main__':
    app.run(debug=True)
