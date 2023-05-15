# ISE-Software-Testing-Room-Booking-Project
Project for Software Testing module for CS4442. Built using flask on an oracle database.

# Setup Guide
<details><summary><b>Installing software</b></summary>
<p>
1. <a href = "https://dbeaver.io">DBeaver</a><br>
2. <a href = "https://www.docker.com/products/docker-desktop/">Docker</a><br>
3. <a href = "https://www.python.org/downloads/">Python</a>
</p>
</details>

<details><summary><b>Set up the database in docker</b></summary>
<p>
Download the container from <a href = "https://hub.docker.com/r/gvenzl/oracle-xe">this link</a>.<br>
Initiate the docker instance using following command (execute in terminal):<br>
docker run -d -p 1521:1521 -e ORACLE_PASSWORD=root --name room-booking-project gvenzl/oracle-xe<br>
This initialises a new docker container.
</p>
</details>

<details><summary><b>Connect container to database</b></summary>
<p>
1. Open DBeaver.<br>
2. Establish a connection with the database using credentials of SYSTEM. For this go to Database -> New Database Connection. Select Oracle, click next, and fill in the following details:<br>
Host: localhost, Port: 1521, Database: XEPDB1, Username: SYS, Role: SYSDBA, Password: root.
</p>
</details>

<details><summary><b>Create the schema and add sample data</b></summary>
<p>
1. Create a new schema and name it RBS (for Room Booking System) and set the password as rbs.<br>
2. Create a new script and paste the SQL code from SetUpDatabase.sql (located in the sqlScripts folder) into it and run the script to create the schema.<br>
3. Create another script and paste the SQL code from AddDataToDatabase.sql into it to insert sample data into the database.<br>
</p>
</details>

<details><summary><b>Install necessary modules</b></summary>
<p>
1. Open your command prompt.<br>
2. Set up a virtual environment and activate it.<br>
3. Run the following with 'pip install ...', and allow the modules to install:<br>
   flask, oracle, oracledb, splinter, mock, ...<br>
4. Download chromedriver from https://chromedriver.chromium.org/ and edit the executable_path in functional_test.py to the path to chromedriver on your machine.<br>
</p>
</details>

<details><summary><b>Launch the app</b></summary>
<p>
1. Open the repository folder in your IDE and run 'main.py'.<br>
2. Paste the following link into Google Chrome: 'http://127.0.0.1:5000'.
</p>
</details>

### About Our Project:
The goal of this project was to design, build and test a room booking system.
Our web based application allows individuals associated with ISE (Immerisve Software Engineering course at the University of Limerick) to book its rooms for personal use.

#### Individuals in the system:
1. Roles they play in ISE: Admin of the system, Students, Teaching Assistants (referred to as TAs), Teaching Staff (referred to as faculty) and Staff.
2. Each person logs in to the system with their university provided email address and their password.
3. They can book rooms for themselves and on behalf of a group of people.
4. They can view their previous bookings.
#### Rooms:
1. There are six types of 'rooms' available for booking: study desk, computer lab desk, conference room, meeting room, classroom and TA space.
2. Every room has a specified minimum and maximum capacity of people it can be booked for. The system will show suitable rooms for the number of people an individual wishes to book for.
#### Time table:
1. The rooms can be booked every day of the week, regardless of weekends or public holidays.
2. The building is open from 8am to 9pm, which means the rooms can be booked from 8am to 9pm every day.
3. One booking refers to a one hour slot which is picked by the individual from the available times in the system.

### How to Run Our Project and its Tests:
All the tests for this project are located in the 'tests' folder of this repository.<br>
1. 'integrationTests' folder contains tests which can be run manually. The test files within this folder aim to cover integration testing and functional testing. They use a python module called 'splinter' which automates the testing of web application ineractions. To run the tests, first you'll need to run main.py and while that's running, you can run each python file separately. The code should exit with code=0 if the automated tests passed, i.e. the webpage functions as intended. It might even print out messages that confirm something about how the system reacted.
2. 'mockTests' folder contains ...
3. 'Integration_Test.py' ...
4. 'System_Test.py' ...
5. 'Unit_Tests.py' ...
6. ''

### Brief Outline of Features/Tests:
### Percentage Contribution by each Group Member with a Brief Description:

## Team Members: Pardis Norouzi, Tamara Orosz & Conor Glynn