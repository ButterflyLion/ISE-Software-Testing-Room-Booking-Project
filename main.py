import datetime
from flask import Flask , session, redirect, url_for, request, render_template
#import oracledb

# Replace with your actual Oracle database credentials
user = 'SYS'
password = 'root'
port = 1522
service_name = 'XEPDB1'
server = 'NAS'
conn_string = "server:{port}/{service_name}".format(
    port=port, service_name=service_name)
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
data = []
id = []

@app.route('/homepage')
def home():
    return render_template('homepage.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()