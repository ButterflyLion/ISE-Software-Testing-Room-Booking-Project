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
        NoGuests = False
        Room_id = False
        ASlots = {}
        SelectedDate = False
        SSlot = False
        ARooms = False

        con = oracledb.connect(user=user, password=password, dsn=conn_string)
        cur = con.cursor()
        
        stage = request.form.get('s', 'main') #is s is posted, set stage to that otherwise set it to main.
        print(request.form)

        if request.method == 'POST':


            NoGuests = check_number(request.form.get('guests', False))
            Room_id = check_number(request.form.get('roomid', False))
            SelectedDate = request.form.get('sdate', False)
            SSlot = check_number(request.form.get('shour', False))
            date_to_check = False
            AvSlots = False
            


            if stage in ['rooms','dates','hours','confirm','submit']:
                 
                if NoGuests is not False:             
                    Rooms = get_rooms_accessible_to_role(NoGuests)
                    if Rooms['err'] == False:
                        data = Rooms['data']
                        ARooms = Rooms['rooms']
                    else:
                        err = Rooms['err']
                else:
                    err = 'Invalid guests'                       
               
            if err == False and (stage in ['dates','hours','confirm','submit']):
                room_ids = Rooms['room_ids']
                Room_id = check_number(Room_id)
                if Room_id and Room_id in room_ids:
                    Dates = get_all_available_time_slots(Room_id)
                    slotsarray = Dates['slots']
                else:
                    err = 'Invalid Room Selected or room not available to user'
                

            
            if err == False and stage in ['hours','confirm','submit']:
                if SelectedDate:
                    try:
                        date_to_check = datetime.datetime.strptime(SelectedDate , "%m/%d/%Y").date()
                    except ValueError:
                        err = 'Date is invalid'
                        SelectedDate = False

                    if err == False and date_to_check: 
                        if date_to_check in slotsarray:
                            # If the date exists, get the available slots for that date
                            slots_for_date = slotsarray[date_to_check]
                            #print(f"Available time slots for {date_to_check}: {slots_for_date}")

                            cur.execute('SELECT * FROM RBS.TIMESLOT')
                            time_slots = cur.fetchall()                    
                            for row in time_slots:
                                if row[0] in slots_for_date:
                                    ASlots[row[0]] = {"slot_id": row[0], "start": row[1].strftime('%H:%M'),"end": row[2].strftime('%H:%M')}
                        else:
                            err = 'No available timeslots for this date'
                else:
                    err = 'No date was selected'

            if err == False and stage in ['confirm','submit']:

                if SSlot and SSlot in ASlots:

                        print('confirm')

                else:
                    err = "Invalid Slot!"

                print('here')


            if err == False and stage == 'submit':

                cur.execute("SELECT MAX(booking_id) FROM RBS.BOOKING")
                result = cur.fetchone()
                print(result)
                last_booking_id = result[0]

                # If there is no previous booking in the table, set the booking_id to 1
                if last_booking_id is None:
                    booking_id = 1
                else:
                    # Otherwise, increment the last booking_id value by 1 to generate the new booking_id
                    booking_id = last_booking_id + 1

                print(booking_id)

                try: 
                    cur.execute("INSERT INTO RBS.BOOKING(booking_id, user_id, room, b_day, time_slot, num_people, b_status) VALUES (:0, :1, :2,:3,:4,:5,:6)", 
                                (booking_id, session['userid'], Room_id, date_to_check, SSlot, NoGuests, 1))     
                    con.commit()

                except Exception as e:
                    print("Error inserting data:", e)
                    err = e
                    con.rollback()

                # Close the cursor and connection as we are redirecting the page here already

                print(NoGuests)

                print(ARooms)
                print(ARooms[Room_id])

                print(SelectedDate)

                print(ASlots)
                print(ASlots[SSlot])

                cur.close()
                con.close()
                print('submit')
                return redirect(url_for('index'))


        # Close the cursor and connection
        cur.close()
        con.close()
        return render_template('index.html',stage=stage,err=err,data=data,NoGuests=NoGuests,Room_id=Room_id,ASlots=ASlots,SelectedDate=SelectedDate,ARooms=ARooms,SSlot=SSlot)
        

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
            else:
                err = 'Invalid username or password'
            
        
        return render_template('login.html',err=err) # redundant
    
    return render_template('login.html',err=err)


def check_number(number=False):
    if number and str(number).isdigit():
        try:
            input_int = int(number)
        except ValueError: 
            input_int = number

        return input_int
    else:
        return False




def get_all_available_time_slots(Room_id = False):

    ret = {'data': [], 'slots' : [], 'err': False}
    
    Room_id = check_number(Room_id)


    con = oracledb.connect(user=user, password=password, dsn=conn_string)
    cur = con.cursor()

    # Set the date range to check for bookings
    start_date = datetime.date.today() # First day of current month
    end_date = start_date.replace(month=start_date.month+1) - datetime.timedelta(days=1)  # Last day of current month
    print(start_date)
    print(end_date)

    cur.execute('SELECT TIME_SLOT_ID FROM RBS.TIMESLOT')
    time_slots = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT b_day, time_slot FROM RBS.booking WHERE b_day BETWEEN :start_date AND :end_date AND room = :Room_id",
                    {'start_date': start_date, 'end_date': end_date,"Room_id":Room_id})
    bookings = cur.fetchall()

    available_time_slots = {}
    
    # Loop through each date within the date range
    for day in range((end_date - start_date).days + 1):
        date = start_date + datetime.timedelta(days=day)

        # Initialize the available time slots for the current date
        available_time_slots[date] = time_slots.copy()

        # Loop through each time slot
        for time_slot in time_slots:
            # Check if there are any bookings for the current date and time slot
            if (date, time_slot) in bookings:
                # If there is a booking, remove the time slot from the available time slots for the current date
                available_time_slots[date].remove(time_slot)

    # Print the available time slots for each date

    ret['slots'] = available_time_slots



    cur.close()
    con.close()

    return ret

def get_rooms_accessible_to_role(NoGuests = False):

    ret = {'data': [], 'room_ids' : [], 'err': False, 'rooms' :{}}

    NoGuests = check_number(NoGuests)

    if NoGuests > 0 :

        con = oracledb.connect(user=user, password=password, dsn=conn_string)
        cur = con.cursor()

        cur.execute("SELECT room_type_id FROM RBS.RoomUserRole WHERE user_role_id = :userroleid", {'userroleid': session['userroleid']})
        RoomTypesAllowed = [row[0] for row in cur.fetchall()] #getting Rooms allowed for this user


        query = "SELECT ROOM.*, ROOMTYPE.r_type FROM RBS.ROOM \
                LEFT JOIN RBS.ROOMTYPE ON RBS.ROOM.room_type = RBS.ROOMTYPE.room_type_id \
                WHERE ROOM.room_type IN ({}) AND ROOM.mincapacity <= :NoGuests AND ROOM.maxcapacity >= :NoGuests".format(','.join([':{}'.format(i+1) for i in range(len(RoomTypesAllowed))]))
        params = {'NoGuests': NoGuests}
        params.update({str(i+1): val for i, val in enumerate(RoomTypesAllowed)}) #converting an array of roomtypeids and passing them one by one
        cur.execute(query, params)

        rows = cur.fetchall()
        if rows:
            data = []
            room_ids = []
            for row in rows:
                room ={
                    "room_id": row[0],
                    "description": row[4],
                    "min": row[2],
                    "max": row[3]
                }
                data.append(room)
                room_ids.append(row[0])
                ret['rooms'][row[0]]=room

            ret['data']=data
            ret['room_ids']=room_ids
            

        else:
            ret['err'] = 'No Rooms found!'
        
        cur.close()
        con.close()

    else:
        ret['err'] = 'Invalid guests'
        

    return ret



if __name__ == '__main__':
    app.run()



