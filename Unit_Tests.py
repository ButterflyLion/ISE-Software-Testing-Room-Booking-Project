import unittest
from datetime import date, timedelta
from flask import Flask , session, redirect, url_for, request, render_template
from main import app

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Student/Staff ID', response.data)

    def test_valid_login2(self):
        response = self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'},follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)
    
    def test_invalid_login(self):
         response = self.app.post('/login', data={'username': 'invalid_username', 'password': 'invalid_password'}, follow_redirects=True)
         self.assertEqual(response.status_code, 200)
         self.assertIn(b'Invalid username or password', response.data)

    def test_empty_login(self):
        response = self.app.post('/login', data={'username': '', 'password': ''}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)

class TestNumberOfGuests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_number_of_guests(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Description', response.data)
    def test_invalid_number_of_guests(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': 'invalid_guests'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    def test_empty_number_of_guests(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': ''}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    def test_negative_number_of_guests(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '-10'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    def test_zero_number_of_guests(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '0'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    def invalid_number_of_guests(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '200'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No Rooms', response.data)

class  TestAvailableRooms(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    #student
    def test_available_rooms_for_one_guest_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'study desk', response.data)

    def test_available_rooms_for_one_guest_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'computer', response.data)

    def test_available_rooms_for_over_three_guests_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '4'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'meeting room', response.data)

    def test_invalid_available_rooms_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '30'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Conference room  ', response.data)

    def test_invalid_available_rooms_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '30'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Classroom', response.data)
    
    def test_invalid_available_rooms_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'TAs', response.data)
    
    def test_invalid_available_rooms_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '16'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No Rooms', response.data)
    
    def test_invalid_available_rooms_for_student(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '0'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    
    #TA
    def test_available_rooms_for_one_guest_for_TA(self):
        self.app.post('/login',data={'username': '12@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TA space', response.data)
    
    def test_available_rooms_for_TA(self):
        self.app.post('/login',data={'username': '12@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '30'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'classroom', response.data)
    
    def test_available_rooms_for_TA(self):
        self.app.post('/login',data={'username': '12@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'meeting room', response.data)
    
    def test_available_rooms_for_TA(self):
        self.app.post('/login',data={'username': '12@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'conference room', response.data)
    
    def test_invalid_available_rooms_for_TA(self):
        self.app.post('/login',data={'username': '12@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'study desk', response.data)
    
    def test_invalid_available_rooms_for_TA(self):
        self.app.post('/login',data={'username': '12@studetmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'computer lab', response.data)
    
    def test_invalid_available_rooms_for_TA(self):
        self.app.post('/login',data={'username': '12@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '51'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No Rooms', response.data)
    
    def test_invalid_available_rooms_for_TA(self):
        self.app.post('/login',data={'username': '12@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '0'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    
    #Faculty
    def test_available_rooms_for_one_guest_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TA space', response.data)
    
    def test_available_rooms_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '30'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'classroom', response.data)
    
    def test_available_rooms_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'meeting room', response.data)
    
    def test_available_rooms_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'conference room', response.data)
    
    def test_invalid_available_rooms_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'study desk', response.data)
    
    def test_invalid_available_rooms_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'computer lab', response.data)
    
    def test_invalid_available_rooms_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '51'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No Rooms', response.data)
    
    def test_invalid_available_rooms_for_Faculty(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '0'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    
    #Staff
    def test_available_rooms_for_Staff(self):
        self.app.post('/login',data={'username': '3@staffmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'meeting room', response.data)
    
    def test_available_rooms_for_Staff(self):
        self.app.post('/login',data={'username': '3@staffmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'conference room', response.data)

    def test_invalid_available_rooms_for_Staff(self):
        self.app.post('/login',data={'username': '3@staffmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'study desk', response.data)

    def test_invalid_available_rooms_for_Staff(self):
        self.app.post('/login',data={'username': '3@staffmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'computer lab desk', response.data)
    
    def test_invalid_available_rooms_for_Staff(self):
        self.app.post('/login',data={'username': '3@staffmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'TA space', response.data)
    
    def test_invalid_available_rooms_for_Staff(self):
        self.app.post('/login',data={'username': '3@staffmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '30'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'classroom', response.data)

    def test_invalid_available_rooms_for_Staff(self):
        self.app.post('/login',data={'username': '3@staffmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '0'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    
    #admin
    def test_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TA space', response.data)
    
    def test_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'study desk', response.data)
    
    def test_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'computer lab', response.data)

    def test_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '30'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'classroom', response.data)
    
    def test_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'meeting room', response.data)
    
    def test_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '15'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'conference room', response.data)
    
    def test_invalid_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '51'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No Rooms', response.data)
    
    def test_invalid_available_rooms_for_admin(self):
        self.app.post('/login',data={'username': '5@adminmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'rooms','guests': '0'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid guests', response.data)
    
    #user
    def test_Book_Room_for_user(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie', 'password': '12345'})
        response = self.app.post('/index', data={ 's': 'dates','roomid': '1','guests': '1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Next', response.data)
    
    
class TestAvailableDate(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_available_date_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'hours','roomid': '1','guests': '1','sdate': '05/18/2023'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Available Time Slots', response.data)

    def test_invalid_available_date_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'hours','roomid': '1','guests': '1','sdate': '2020-12-12'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Available Time Slots', response.data)

    def test_invalid_available_date_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'dates','roomid': '4','guests': '1','sdate': '05/18/2023'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Available Time Slots', response.data)
    
    def test_invalid_available_date_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'hours','roomid': '1','guests': '1','sdate': ''}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No date was selected', response.data)
    
    def test_invalid_available_date_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'dates','roomid': '1','guests': '1','sdate': '0/05/2023'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'available slots', response.data)
    
    def test_invalid_available_date_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'dates','roomid': '1','guests': '1','sdate': '00/00/2023'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'available slots', response.data)
    
    
class TestAvailableHours(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_available_time_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'confirm','roomid': '1','guests': '1','sdate': '05/18/2023','shour':4 }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have selected the following:', response.data)
    
    
    def test_invalid_available_time_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'confirm','roomid': '1','guests': '1','sdate': '05/18/2023','shour':0 }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Slot!', response.data)
    
    def test_invalid_available_time_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'confirm','roomid': '1','guests': '1','sdate': '05/18/2023','shour':14 }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Slot!', response.data)
    
    def test_invalid_available_time_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'confirm','roomid': '4','guests': '15','sdate': '05/18/2023','shour':13 }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'You have selected the following:', response.data)
    
    def test_invalid_available_time_for_User(self):
        self.app.post('/login',data={'username': '1@studentmail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'confirm','roomid': '4','guests': '1','sdate': '05/18/2023','shour':13 }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'You have selected the following:', response.data)
    
class TestBooking(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_booking_for_User(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'submit','roomid': '11','guests': '15','sdate': '05/26/2023','shour':4,  }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Submission was a success', response.data)

class TestSubmitBooking(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_confirm_booking_for_User(self):
        self.app.post('/login',data={'username': '4@facultymail.ul.ie','password': '12345'})
        response = self.app.post('/index', data={ 's': 'main','roomid': '11','guests': '15','sdate': '05/26/2023','shour':4,  }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data) 


if __name__ == '__main__':
     unittest.main()
