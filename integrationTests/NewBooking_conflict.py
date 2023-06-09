# Make sure to run NewBooking.py first!
# This is to demonstrate that a timeslot can't be booked twice
from splinter import Browser
from selenium import webdriver

executable_path = {'executable_path':r'C:\Users\novel\workspace\Year1Sem2\Room Booking Project\chromedriver'}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = Browser('chrome', **executable_path, headless=False, options=options)

url = 'http://127.0.0.1:5000/index'
browser.visit(url)

browser.find_by_name("username").fill("11@studentmail.ul.ie")
browser.find_by_name("password").fill(12345)
login = browser.find_by_value("Log In").click()

if(browser.url == "http://127.0.0.1:5000/index"):
    if(browser.is_element_present_by_name("submit")):
        browser.find_by_name("submit").click()
        if(browser.is_element_present_by_id("guests")):
            browser.find_by_id("guests").fill(5)
            browser.find_by_name("submit").click()

            if(browser.is_element_present_by_id("tbl")):
                headers = ["Room Description", "Min Capacity", "Max Capacity", "Book This"]
                for header in headers:
                    assert browser.is_text_present(header), f"Header '{header}' not found"
                button = browser.find_by_css('.btn.bookbtn')
                button.first.click()

                if(browser.is_element_present_by_css("#datepicker")):
                    browser.find_by_text("25").click()  #selects 25th of May
                    browser.find_by_name("submit").click()
                    if(browser.is_element_present_by_css(".btn.hourbtn")):
                        assert browser.is_text_present("15:00 - 16:00"), "No option to book timeslot which has been already booked"

                    else:
                        assert browser.is_element_present_by_css(".btn.hourbtn"), "There are no time slots to pick from"            

                else:
                    assert browser.is_element_present_by_css("#datepicker"), "Calendar doesn't exist"

            else:
                assert browser.is_element_present_by_id("tbl"), "Table not found for choosing a room to book"

        else:
            assert browser.is_element_present_by_id("guests"), "Input field for specifying no. of guests doesn't exist"

    else:
        assert browser.is_element_present_by_name("submit"), "No 'Make a Booking' button exists"

else:
    print("Login failed")

browser.quit()