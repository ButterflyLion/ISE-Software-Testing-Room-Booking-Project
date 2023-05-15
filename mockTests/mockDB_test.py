from main import app
from tests.mockTests.mockDB import MockDB
import unittest

class TestMain(MockDB):

    def test_db_login(self):
        with self.mock_db_config:
            formData = {
                'username': '14@facultymail.ul.ie',
                'password': '12345'
            }

            with app.test_client() as client:
                with client.session_transaction() as session:
                    session.clear()

                response = client.post('/login', data=formData)
                self.assertEqual(response.status_code, 500)
                self.assertEqual(response.location, 'http://127.0.0.1:5000/index')

                with client.session_transaction() as session:
                    self.assertEqual(session['userid'], '14')
                    self.assertEqual(session['firstname'], 'Diana')
                    self.assertEqual(session['lastname'], 'Dunnes')
                    self.assertEqual(session['username'], '14@facultymail.ul.ie')
                    self.assertEqual(session['userrole'], 'faculty')
                    self.assertEqual(session['userroleid'], '3')


if __name__ == '__main__':
     unittest.main()                   