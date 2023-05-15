from splinter import Browser
from selenium import webdriver

executable_path = {'executable_path':r'C:\Users\novel\workspace\Year1Sem2\Room Booking Project\chromedriver'}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = Browser('chrome', **executable_path, headless=False, options=options)

url = 'http://127.0.0.1:5000/index'
browser.visit(url)

browser.find_by_name("username").fill("1@studentmail.ul.ie")
browser.find_by_name("password").fill(12345)
login = browser.find_by_value("Log In").click()

if(browser.url == "http://127.0.0.1:5000/index"):
    if(browser.is_element_present_by_id("tbl")):
        headers = ["Room Description", "Date", "TimeSlot", "Guests"]
        for header in headers:
            assert browser.is_text_present(header), f"Header '{header}' not found"
        assert browser.is_text_present("Meeting Room 1"), "Couldn't find room booked"
        assert browser.is_text_present("25/05/23"), "Couldn't find date picked"
        assert browser.is_text_present("09:00 - 10:00"), "Couldn't find timeslot picked"
        assert browser.is_text_present("5"), "Couldn't find number of guests in booking"
        print("Booking was successfully retrieved from records")

    else:
        assert browser.is_element_present_by_id("tbl"), "There are no bookings to be found"

else:
    print("Login failed")

browser.quit()