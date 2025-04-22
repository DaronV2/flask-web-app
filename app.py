import os
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# Configuration MySQL
app.config['MYSQL_DATABASE_USER'] = 'dev'
app.config['MYSQL_DATABASE_PASSWORD'] = 'developer'
app.config['MYSQL_DATABASE_DB'] = 'employes_db'
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

@app.route("/")
def main():
    return "Salut !"

@app.route('/jemappelle/<name>')
def hello(name):
    return f'Salut, {name} ! Comment va ?'

@app.route('/lecture_db')
def read():
    cursor.execute("SELECT nom FROM employes")
    row = cursor.fetchone()
    result = []
    while row is not None:
      result.append(row[0])
      row = cursor.fetchone()

    return ", ".join(result)

if __name__ == "__main__":
    app.run()
