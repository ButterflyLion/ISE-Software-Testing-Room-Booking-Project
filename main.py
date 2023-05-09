import datetime
from flask import Flask , session, redirect, url_for, request, render_template
import oracledb

# Replace with your actual Oracle database credentials
user = 'SYS'
password = 'root'
port = 1522
service_name = 'XEPDB1'
conn_string = "localhost:{port}/{service_name}".format(
    port=port, service_name=service_name)
app = Flask(__name__)
data = []
id = []

@app.route('/')
def home():
    return 'hello world'
    #return render_template('home.html')


if __name__ == '__main__':
    app.run()
