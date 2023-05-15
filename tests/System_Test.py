import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Code for the happy path scenario
class TestHappyPath1Student:
    def test_login_and_make_booking(self):
        # launch the browser and navigate to the login page
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/index")

        # enter email and password and click login
        email_field = driver.find_element("name", "username")
        email_field.send_keys("1@studentmail.ul.ie")

        password_field = driver.find_element("name", "password")
        password_field.send_keys("12345")
        password_field.send_keys(Keys.RETURN)

        # wait for the system to load and verify that the user has successfully logged in
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Welcome" in driver.page_source

        # navigate to the next page and click on the Make a Booking button
        driver.find_element("name" , "submit").click()

        # navigate to the booking page and enter the number of guests
        guests_field = driver.find_element("name" , "guests")
        guests_field.send_keys("3")
        guests_field.send_keys(Keys.RETURN)
        #submit_button = driver.find_element("name", "submit").click()

        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Rooms for" in driver.page_source


        driver.find_element("id" , "11").click()


        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Dates for" in driver.page_source

        # Locate the datepicker input element and click on it
        datepicker = driver.find_element("id", "datepicker")
        datepicker.click()


        # Click on the datepicker input element again to close the widget (if necessary)
        datepicker.click()

        # Select the desired date in the datepicker widget
        date_element = driver.find_element(By.XPATH, "//a[@data-date='25']")
        date_element.click()

        driver.find_element("name" , "submit").click()

        time.sleep(3) 

        driver.find_element(By.CSS_SELECTOR, ".hourbtn:first-of-type").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(10)

        driver.quit()

class TestHappyPath2Student:
    def test_login_and_make_booking(self):
        # launch the browser and navigate to the login page
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/index")

        # enter email and password and click login
        email_field = driver.find_element("name", "username")
        email_field.send_keys("1@studentmail.ul.ie")

        password_field = driver.find_element("name", "password")
        password_field.send_keys("12345")
        password_field.send_keys(Keys.RETURN)

        # wait for the system to load and verify that the user has successfully logged in
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Welcome" in driver.page_source

        # navigate to the next page and click on the Make a Booking button
        driver.find_element("name" , "submit").click()

        # navigate to the booking page and enter the number of guests
        guests_field = driver.find_element("name" , "guests")
        guests_field.send_keys("3")
        guests_field.send_keys(Keys.RETURN)
        #submit_button = driver.find_element("name", "submit").click()

        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Rooms for" in driver.page_source


        driver.find_element("id" , "12").click()


        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Dates for" in driver.page_source

        # Locate the datepicker input element and click on it
        datepicker = driver.find_element("id", "datepicker")
        datepicker.click()


        # Click on the datepicker input element again to close the widget (if necessary)
        datepicker.click()

        # Select the desired date in the datepicker widget
        date_element = driver.find_element(By.XPATH, "//a[@data-date='25']")
        date_element.click()

        driver.find_element("name" , "submit").click()

        time.sleep(3) 

        driver.find_element(By.CSS_SELECTOR, ".hourbtn:nth-of-type(2)").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(10)

        driver.quit()


# Test that the same person can not book another room at the same date and time        
class TestBookingSameRoomTimeAndDate:
    def test_booking_without_information(self):
        # launch the browser and navigate to the login page
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/index")

        # enter email and password and click login
        email_field = driver.find_element("name", "username")
        email_field.send_keys("1@studentmail.ul.ie")

        password_field = driver.find_element("name", "password")
        password_field.send_keys("12345")
        password_field.send_keys(Keys.RETURN)      

        # wait for the system to load and verify that the user has successfully logged in
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Welcome" in driver.page_source
    
    # navigate to the next page and click on the Make a Booking button
        driver.find_element("name" , "submit").click()

        # navigate to the booking page and enter the number of guests
        guests_field = driver.find_element("name" , "guests")
        guests_field.send_keys("3")
        guests_field.send_keys(Keys.RETURN)
        #submit_button = driver.find_element("name", "submit").click()

        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Rooms for" in driver.page_source

        driver.find_element("id" , "12").click()


        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Dates for" in driver.page_source

        # Locate the datepicker input element and click on it
        datepicker = driver.find_element("id", "datepicker")
        datepicker.click()


        # Click on the datepicker input element again to close the widget (if necessary)
        datepicker.click()

        # Select the desired date in the datepicker widget
        date_element = driver.find_element(By.XPATH, "//a[@data-date='25']")
        date_element.click()

        driver.find_element("name" , "submit").click()

        time.sleep(3) 

        driver.find_element(By.CSS_SELECTOR, ".hourbtn:first-of-type").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(10)

        driver.quit()

# Test that the same person can not book more than two times a day 
class TestBookingMoreThanTwiceADay:
    def test_login_and_make_booking(self):
        # launch the browser and navigate to the login page
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/index")

        # enter email and password and click login
        email_field = driver.find_element("name", "username")
        email_field.send_keys("1@studentmail.ul.ie")

        password_field = driver.find_element("name", "password")
        password_field.send_keys("12345")
        password_field.send_keys(Keys.RETURN)

        # wait for the system to load and verify that the user has successfully logged in
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Welcome" in driver.page_source

        # navigate to the next page and click on the Make a Booking button
        driver.find_element("name" , "submit").click()

        # navigate to the booking page and enter the number of guests
        guests_field = driver.find_element("name" , "guests")
        guests_field.send_keys("1")
        guests_field.send_keys(Keys.RETURN)
        #submit_button = driver.find_element("name", "submit").click()

        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Rooms for" in driver.page_source

        driver.find_element("id" , "1").click()


        # wait for the system to load and verify that the booking was successful
        time.sleep(2)  # wait for 5 seconds to let the page load
        assert "Available Dates for" in driver.page_source

        # Locate the datepicker input element and click on it
        datepicker = driver.find_element("id", "datepicker")
        datepicker.click()


        # Click on the datepicker input element again to close the widget (if necessary)
        datepicker.click()

        # Select the desired date in the datepicker widget
        date_element = driver.find_element(By.XPATH, "//a[@data-date='25']")
        date_element.click()

        driver.find_element("name" , "submit").click()

        time.sleep(3) 

        driver.find_element(By.CSS_SELECTOR, ".hourbtn:nth-of-type(2)").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(3)

        driver.find_element("name" , "submit").click()

        time.sleep(10)

        driver.quit()

# Test concurrent booking with threads


