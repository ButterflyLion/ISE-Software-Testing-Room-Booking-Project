import datetime
from flask import Flask , session, redirect, url_for, request, render_template
import oracledb
import hashlib

# Replace with your actual Oracle database credentials
user = 'SYS'
password = 'root'
port = 1522
service_name = 'XEPDB1'
conn_string = "localhost:{port}/{service_name}".format(
    port=port, service_name=service_name)
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

# This is for login Sessions
app.secret_key = 'RBS-Secret' 

data = []
id = []

@app.route('/homepage')
def home():
    return render_template('homepage.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def login():

    if 'username' in session:
        # User is already logged in, redirect to index page
        return redirect(url_for('index'))

    err = False

    if request.method == 'POST':
        username = request.form['username']
        passh = hashlib.md5(request.form['password'].encode()).hexdigest()
        
        #Connecting to database
        con = oracledb.connect(user=user, password=password, dsn=conn_string)

        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM RBS.USERS \
                           WHERE LOWER(RBS.USER.email) = LOWER(:email)", {"email": username})
            result = cursor.fetchone()

            if result:
                if passh == result[0]:
                    # Username and password are valid, so set user as logged in
                    session['username'] = username
                    session['userrole'] = result[5]
                    session['userid'] = result[1]
                    return redirect(url_for('index'))
                else:
                    err = 'Invalid username or password'
            
        
     #   return render_template('login.html',err=err) # redundant
    
    return render_template('login.html',err=err)


if __name__ == '__main__':
    app.run()