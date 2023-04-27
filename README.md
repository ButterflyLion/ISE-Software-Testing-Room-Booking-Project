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
Download the container from <a href = "https://hub.docker.com/r/gvenzl/oracle-xe">this link</a>.<br>
Initiate the docker instance using following command (execute in terminal):<br>
docker run -d -p 1522:1521 -e ORACLE_PASSWORD=root --name room-booking-project gvenzl/oracle-xe
This initialises a new docker container.
</p>
</details>

<details><summary><b>Connect container to database</b></summary>
<p>
1. Open DBeaver.
2. Establish a connection with the database using credentials of SYSTEM. For this go to Database -> New Database Connection. Select Oracle, next and fill in the following details:
Host: localhost, Port: 1522, Database: XEPDB1, Username: SYS, Role: SYSDBA, Password: root.
</p>
</details>

<details><summary><b>Step 4 - Create the data</b></summary>
<p>
1. Create a new schema and name it RBS (for Room Booking System) and set the password as rbs.
2. Create a script and paste the following code to create the tables:
3. Create another script and paste the following code to insert template data:
</p>
</details>

## Team Members: Pardis Norouzi, Tamara Orosz & Conor Glynn
### About Our Project:
### How to Run Our Project and its Automated Tests:
### Brief Outline of Features/Tests:
### Percentage Contribution by each Group Member with a Brief Description:
