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
   flask, oracle, oracledb, splinter, mock, selenium.<br>
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
1. 'Unit_Tests.py' : To run unit tests, first you need to have the following installed:
- Python (version 3.6 or later)
- Flask (install using pip install flask)
Navigate to the project directory in the terminal and run the following command to execute the unit tests: Python -m unittest Unit_Tests.py
The code should exit with :
Ran 29 tests in 3.068s
OK

2. 'integrationTests' : It contains tests which can be run manually. The test files within this folder aim to cover integration testing and functional testing. They use a python module called 'splinter' which automates the testing of web application ineractions. To run the tests, first you'll need to run main.py and while that's running, you can run each python file separately. The code should exit with code=0 if the automated tests passed, i.e. the webpage functions as intended. It might even print out messages that confirm something about how the system reacted.

- 2.'Integration_Test.py' : Try to install the required dependencies by running pip install -r requirements.txt and then navigate to the project directory.
Run the following command to execute the integration tests : pytest Integration_Test.py
The code should exit with :
Integration_Test.py ...                                                              [100%]

==================================== 3 passed in 0.29s ====================================


3. 'System_Test.py' : 
Before running the tests, ensure that you have the following dependencies installed:
- Pytest libarary
- Selenium library
- Chrome WebDriver (compatible with your Chrome browser version)
Navigate to the project's root directory and execute the tests by running the following command: pytest System_Test.py
The code should exit with :
.                                                                                                 [100%]
============================================= 4 passed in 140.54s (0:02:20) ==============================================


4. 'mockTests' folder contains two files: mockDB.py and mockDB_test.py. These are incomplete tests that were written but not finished due to them being lower in priority than the other tests we were writing. However, we decided to include them too, even if they're incomplete.


### Brief Outline of Features/Tests:
1. In Unit Testing, we organize our tests into separate classes, each representing a specific function of the application. These classes contain various methods that test different scenarios, including valid and invalid cases.<br> 
Here is the list of the classes:<br>
- TestLogin<br>
- TestNumberOfGuests<br>
- TestAvailableRooms<br>
- TestAvailableDate<br>
- TestAvailableHours<br>
- TestBooking<br>
- TestSubmitBooking<br>

2. integrationTests : This aims to combine functional and integration testing. Functional testing tests that the application works as per the user's expectations. These are user stories which have been implemented. The 'splinter' module allows us to automate the user's interaction with the frontend, i.e. the webpages. We also consider these integration tests since they test that multiple components work together. We test that the data entered is used to determine what choices are shown to the user, e.g. if a user wants to book a room for themselves, they won't be given the option to book a conference room. 

2. Integration_Test.py : 
The tests include retrieving users, user login validation, and retrieving available rooms. The tests ensure the proper functioning of the database connection and data retrieval.

3. System_Test.py : This repository contains automated tests written in Python using the Selenium library. These tests aim to validate the functionality of a web application by simulating user interactions and verifying expected outcomes. The test cases included in this repository cover various scenarios and functionalities of the web application.<br>
Here is the list of the classes:<br>
- TestHappyPath1Student<br>
- TestHappyPath2Student<br>
- TestBookingSameRoomTimeAndDate<br>
- TestBookingMoreThanTwiceADay<br>

4. Coverage tests involves testing to see how good our tests are. The main premise of it is to check how many lines of code is being tested in the main.py file and dividing that by the number of lines of code that is in that main.py file. According to <a href = "https://learn.microsoft.com/en-us/answers/questions/778016/test-coverage-definition-unit-testing">Microsoft</a>: "Optimal Test Coverage Rate: Keeping it between 70 - 80%" while "Overkill Test Coverage Rate: Keeping it between 80 - 100%".


Results of our Coverage Tests:

Module	   statements	   missing	   excluded	   coverage<br><br>

Unit_Tests.py&nbsp;&nbsp;&nbsp;&nbsp;324&nbsp;&nbsp;&nbsp;&nbsp;136&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;58%<br>
main.py&nbsp;&nbsp;&nbsp;&nbsp;228&nbsp;&nbsp;&nbsp;&nbsp;57&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;75%<br>
Total&nbsp;&nbsp;&nbsp;&nbsp;552&nbsp;&nbsp;&nbsp;&nbsp;193&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;65%<br>

The line to focus on is the coverage of the main.py. This is because this line describes how many lines of the source code is being tested by the Unit_Tests.py file. As we can see, we have a coverage of 75% which is in the optimal range.

### Percentage Contribution by each Group Member with a Brief Description:
As a team we decided on the database schema together and wrote the requirements together.<br>
- Pardis: 50%<br>
- Tamara: 35%<br>
I set up the database, wrote the executable sql script to create the tables and wrote the sample data to fill the tables with. I also started the flask application and the layout of the current website. I documented these steps in the Setup Guide. Next I attempted to mock a database but this proved more challenging than expected so I did integration testing instead and left mocking until last. I never did get around to completely finish the mocking as there were connection errors.<br>
- Conor: 15%<br>

## Team Members: Pardis Norouzi, Tamara Orosz & Conor Glynn
