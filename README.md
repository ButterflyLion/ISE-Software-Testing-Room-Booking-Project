# ISE-Software-Testing-Room-Booking-Project
Room Booking Project for Software Testing module for CS4442. Built using flask on an oracle database.
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
Download the container from <a href = "https://hub.docker.com/r/gvenzl/oracle-xe">this link.</a>.<br>
Initiate the docker instance using following command (execute in terminal):<br>
docker run -d -p 1522:1521 -e ORACLE_PASSWORD=root --name room-booking-project gvenzl/oracle-xe<br>
This initialises a new docker container.
</p>
</details>

<details><summary><b>Connect container to database</b></summary>
<p>
1. Open DBeaver.<br>
2. Establish a connection with the database using credentials of SYSTEM. For this go to Database -> New Database Connection. Select Oracle, next and fill in the following details:<br>
Host: localhost, Port: 1522, Database: XEPDB1, Username: SYS, Role: SYSDBA, Password: root.
</p>
</details>

<details><summary><b>Create the schema and add sample data</b></summary>
<p>
1. Create a new schema and name it RBS (for Room Booking System) and set the password as rbs.<br>
2. Create a new script and paste the SQL code from SetUpDatabase.txt into it to create the schema.<br>
3. Create another script and paste the SQL code from AddDataToDatabase.txt into it to insert sample data into the database.<br>
</p>
</details>

<details><summary><b>Install necessary modules</b></summary>
<p>
1. Open your command prompt.<br>
2. Run the command 'pip install flask', and allow the module to install.<br>
3. Run the command 'pip install oracle', and allow the module to install.<br>
</p>
</details>

<details><summary><b>Launch the app</b></summary>
<p>
Open the repository folder in your IDE and run 'main.py'.<br>
Paste the following link in your browser: 'http://127.0.0.1:5000'.
</p>
</details>

## Team Members: Pardis Norouzi, Tamara Orosz & Conor Glynn
### About Our Project:
### How to Run Our Project and its Automated Tests:
### Brief Outline of Features/Tests:
### Percentage Contribution by each Group Member with a Brief Description:
