import datetime
from flask import Flask , session, redirect, url_for, request, render_template
import oracledb
import hashlib

# Replace with your actual Oracle database credentials
user = 'SYSTEM'
password = 'root'
port = 1521
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

@app.route('/index', methods=['GET', 'POST'])
def index():

    if 'username' not in session:
        # User is not logged in, redirect to login page
        return redirect(url_for('login'))
    else:

        err = False
        data = []


        con = oracledb.connect(user=user, password=password, dsn=conn_string)
        cur = con.cursor()
        
        stage = request.form.get('s', 'main') #is s is posted, set stage to that otherwise set it to main.
        print(stage) 
        print(request.form)

        if stage == 'main':
            session['BGuets'] = ''
            session['BRoom'] = ''
            session['BDate'] = ''
            session['BHour'] = ''





        if request.method == 'POST':

            if stage == 'rooms':
                NoGuests = request.form.get('guests', '0')
                print(NoGuests)
                cur.execute("SELECT room_type_id FROM RBS.RoomUserRole WHERE user_role_id = :userroleid", {'userroleid': session['userroleid']})
                RoomTypesAllowed = [row[0] for row in cur.fetchall()] #getting Rooms allowed for this user
                RoomTypesAllowedString = format(','.join(str(i) for i in RoomTypesAllowed));
                print(RoomTypesAllowedString)

                query = "SELECT ROOM.*, ROOMTYPE.r_type FROM RBS.ROOM \
                        LEFT JOIN RBS.ROOMTYPE ON RBS.ROOM.room_type = RBS.ROOMTYPE.room_type_id \
                        WHERE ROOM.room_type IN ({}) AND ROOM.mincapacity <= :NoGuests AND ROOM.maxcapacity >= :NoGuests".format(','.join([':{}'.format(i+1) for i in range(len(RoomTypesAllowed))]))
                params = {'NoGuests': NoGuests}
                params.update({str(i+1): val for i, val in enumerate(RoomTypesAllowed)})
                cur.execute(query, params)
                for row in cur:
                    data.append({"description": row[4], "min": row[2],
                    "max": row[3]})
       
                

                print('post is rooms')
            elif stage == 'dates':
                print('post is dates')
            elif stage == 'hours':
                print('post is hours')
            elif stage == 'confirm':
                print('post is guest')


        # Close the cursor and connection
        cur.close()
        con.close()
        return render_template('index.html',stage=stage,data=data)
        

@app.route('/', methods=['GET', 'POST'])
def main():
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
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
            cursor.execute("SELECT RBS.USERS.*, RBS.ROLE.u_role FROM RBS.USERS \
                           LEFT JOIN RBS.Role ON RBS.USERS.role_id = RBS.Role.role_id \
                           WHERE LOWER(RBS.USERS.email) = LOWER(:email)", {"email": username})
            result = cursor.fetchone()
            print(result)

            if result:
                if passh == result[4]:
                    # Username and password are valid, so set user as logged in
                    session['username'] = username
                    session['firstname'] = result[1]
                    session['lastname'] = result[2]
                    session['userrole'] = result[7]
                    session['userroleid'] = result[6]
                    session['userid'] = result[0]
                    return redirect(url_for('index'))
                else:
                    err = 'Invalid username or password'
            
        
     #   return render_template('login.html',err=err) # redundant
    
    return render_template('login.html',err=err)


if __name__ == '__main__':
    app.run()