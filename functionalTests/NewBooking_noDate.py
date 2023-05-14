from splinter import Browser
from selenium import webdriver

executable_path = {'executable_path':r'C:\Users\novel\workspace\Year1Sem2\Room Booking Project\chromedriver'}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = Browser('chrome', **executable_path, headless=False, options=options)

url = 'http://127.0.0.1:5000'
browser.visit(url)

browser.find_by_name("username").fill("1@studentmail.ul.ie")
browser.find_by_name("password").fill(12345)
login = browser.find_by_value("Log In").click()

if(browser.url == "http://127.0.0.1:5000/index"):
    if(browser.is_element_present_by_name("submit")):
        browser.find_by_name("submit").click()
        if(browser.is_element_present_by_name("guests")):
            browser.find_by_id("guests").fill(5)
            browser.find_by_name("submit").click()
            if(browser.is_element_present_by_id("11")):
                browser.find_by_id("11").click()
                
            else:
                assert browser.is_element_present_by_id("11"), "No option to book room with id 11"
        
        else:
            assert browser.is_element_present_by_name("guests"), "Input field for specifying no. of guests doesn't exist"

    else:
        assert browser.is_element_present_by_name("submit"), "No 'Make a Booking' button exists"

else:
    print("Login failed")



browser.quit()