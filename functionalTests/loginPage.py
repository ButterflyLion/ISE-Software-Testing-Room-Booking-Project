from splinter import Browser
from selenium import webdriver

executable_path = {'executable_path':r'C:\Users\novel\workspace\Year1Sem2\Room Booking Project\chromedriver'}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = Browser('chrome', **executable_path, headless=False, options=options)

url = 'http://127.0.0.1:5000'
browser.visit(url)

if(
    browser.is_text_present("Student/Staff ID:"), "Title is not present" and
    browser.is_element_present_by_name("username"), "Username field can't be found" and 
    browser.is_element_present_by_name("password"), "Password field can't be found" and 
    browser.is_element_present_by_value("Log In"), "Login button doesn't exist"
):
    browser.find_by_name("username").fill("6@studentmail.ul.ie")
    browser.find_by_name("password").fill(12345)
    login = browser.find_by_value("Log In").click()

    if(browser.url == "http://127.0.0.1:5000/index"):
        assert browser.is_text_present("Welcome Olivia Johnson")
        assert browser.is_text_present("Role: student")
        print("Successful login")
    else:
        print("Login failed")

else:
    assert browser.is_text_not_present("Student/Staff ID:"), "Title is not present"
    assert browser.is_element_not_present_by_name("username"), "Username field can't be found"
    assert browser.is_element_present_by_name("password"), "Password field can't be found"
    assert browser.is_element_present_by_value("Log In"), "Login button doesn't exist"

browser.quit()