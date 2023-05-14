import oracledb

def test_retrieve_users():
    # Set up the connection details
    user = 'SYSTEM'
    password = 'root'
    port = 1521
    service_name = 'XEPDB1'
    conn_string = "localhost:{port}/{service_name}".format(
        port=port, service_name=service_name)

    # Establish the connection to the database
    try:
        con = oracledb.connect(user=user, password=password, dsn=conn_string)
        print("Connection established successfully")
    except oracledb.DatabaseError as e:
        print("Error while connecting to the database:", e)


    # Define a query to retrieve some data from the database
    query = "SELECT * FROM USERS"

    # Execute the query and retrieve the results
    try:
        cursor = con.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print("Data retrieved successfully")
    except oracledb.DatabaseError as e:
        print("Error while executing the query:", e)

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    con.close()


def test_user_login():
    # Retrieve the connection object from the first test case
    user = 'SYSTEM'
    password = 'root'
    port = 1521
    service_name = 'XEPDB1'
    conn_string = "localhost:{port}/{service_name}".format(
        port=port, service_name=service_name)

    try:
        con = oracledb.connect(user=user, password=password, dsn=conn_string)
        print("Connection established successfully")
    except oracledb.DatabaseError as e:
        print("Error while connecting to the database:", e)
    

    # Define the test users' credentials
    valid_user = {'username' : '1@studentmail.ul.ie', 'password': '827ccb0eea8a706c4c34a16891f84e7b'}
    invalid_user = {'username': 'testuser', 'password': 'wrongpass'}

    # Retrieve the test user's data from the database
    query = "SELECT * FROM RBS.USERS WHERE email = :username AND password = :pass"
    result = None
    try:
        cursor = con.cursor()
        cursor.execute(query, {'username':valid_user['username'], 'pass':valid_user['password']})
        result = cursor.fetchone()

    except oracledb.DatabaseError as e:
        print("Error while executing the query:", e)

    # Verify that the retrieved results match the test user's credentials
    assert result != None, "Test user not found in the database"
    assert result[3] == valid_user['username'], "Incorrect username retrieved from the database"
    assert result[4] == valid_user['password'], "Incorrect password retrieved from the database"
    

    # Close the cursor and connection
    cursor.close()
    con.close()

def test_available_rooms():
    
    # Retrieve the connection object from the first test case
    user = 'SYSTEM'
    password = 'root'
    port = 1521
    service_name = 'XEPDB1'
    conn_string = "localhost:{port}/{service_name}".format(
        port=port, service_name=service_name)

    try:
        con = oracledb.connect(user=user, password=password, dsn=conn_string)
        print("Connection established successfully")
    except oracledb.DatabaseError as e:
        print("Error while connecting to the database:", e)
    
    # Define the test rooms' credentials
    valid_room = {'username' : '1@studentmail.ul.ie', 'password': '827ccb0eea8a706c4c34a16891f84e7b'}
    invalid_room = {'username': 'testuser', 'password': 'wrongpass'}

    # Define the test rooms from the database
    query = "SELECT * FROM RBS.ROOMS"
    result = None
    try:
        cursor = con.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    except oracledb.DatabaseError as e:
        print("Error while executing the query:", e)
    
    


    
    