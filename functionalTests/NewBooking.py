from splinter import Browser
from selenium import webdriver

executable_path = {'executable_path':r'C:\Users\novel\workspace\Year1Sem2\Room Booking Project\chromedriver'}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = Browser('chrome', **executable_path, headless=False, options=options)

url = 'http://127.0.0.1:5000/index'
browser.visit(url)

if(browser.is_element_present_by_name("submit")):
    browser.find_by_name("submit").click()
    if(browser.is_element_present_by_id("guests")):
        browser.find_by_id("guests").fill(5)
        browser.find_by_name("submit").click()

        if(browser.is_element_present_by_id("tbl")):
            headers = ["Room Description", "Min Capacity", "Max Capacity", "Book This"]
            for header in headers:
                assert browser.is_text_present(header), f"Header '{header}' not found"
                browser.find_by_id("tbl")
                browser.find_by_name('Book').first.click()
                



        else:
            assert browser.is_element_present_by_id("tbl"), "Table not found"

    else:
        assert browser.is_element_present_by_id("guests"), "Input field for specifying no. of guests doesn't exist"

else:
    assert browser.is_element_present_by_name("submit"), "No 'Make a Booking' button exists"

browser.quit()