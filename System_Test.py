import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

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
time.sleep(5)  # wait for 5 seconds to let the page load
assert "Welcome" in driver.page_source

# navigate to the next page and click on the Make a Booking button
driver.get("http://127.0.0.1:5000/index")
make_booking_button = driver.find_element("name" , "submit").click()

# navigate to the booking page and enter the number of guests
driver.get("http://127.0.0.1:5000/index")
guests_field = driver.find_element("name" , "guests")
guests_field.send_keys("1")
submit_button = driver.find_element("name", "submit").click()

# wait for the system to load and verify that the booking was successful
time.sleep(5)  # wait for 5 seconds to let the page load
assert "Booking Successful" in driver.page_source

# driver.get("http://127.0.0.1:5000/index")
# make_booking_button = driver.find_element("name" , "s").click()






# # verify that the system shows a list of available rooms with a capacity of at least 1 guest
# time.sleep(5)  # wait for 5 seconds to let the page load
# room_list = driver.find_element_by_id("room-list")
# assert "BooK" in room_list.text

# # select the Study Room from the list of available rooms
# study_room_button = driver.find_element_by_id("Submit")
# study_room_button.click()

# # choose the date 05/17/2023 from the calendar
# date_picker = driver.find_element_by_id("date-picker")
# date_picker.click()
# select = Select(driver.find_element_by_class_name("ui-datepicker-year"))
# select.select_by_value("2023")
# select = Select(driver.find_element_by_class_name("ui-datepicker-month"))
# select.select_by_value("5")
# driver.find_element_by_xpath("//a[text()='17']").click()

# # verify that the system displays available time slots for the chosen date
# time.sleep(5)  # wait for 5 seconds to let the page load
# time_slot_list = driver.find_element_by_id("time-slot-list")
# assert "8:00 AM - 9:00 AM" in time_slot_list.text

# # choose the first available time slot from 8:00 AM to 9:00 AM
# time_slot_button = driver.find_element_by_id("time-slot-button-0")
# time_slot_button.click()

# # click on the Confirm button to book the Study Room for the chosen time slot
# confirm_button = driver.find_element_by_id("confirm-button")
# confirm_button.click()

# # verify that the system displays a confirmation message for the booking
# time.sleep(5)  # wait for 5 seconds to let the page load
# assert "confirm" in driver.page_source

# close the browser
driver.quit()
