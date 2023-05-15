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
    if(browser.is_element_present_by_name("submit")):
        browser.find_by_name("submit").click()
        if(browser.is_element_present_by_id("guests")):
            browser.find_by_id("guests").fill(1)
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
                        browser.find_by_text("16:00 - 17:00").click()
                    
                        if(browser.is_element_present_by_id("myTable")):
                            table = browser.find_by_id("myTable")
                            rows = table.find_by_tag("tr")
                            expected = [
                                ['No of Guests', '1'],
                                ['Room', 'study desk'],
                                ['Date', '05/25/2023'],
                                ['Time', '16:00 - 17:00']
                            ]
                            for i, row in enumerate(rows):
                                cells = row.find_by_tag("td")
                                for j, cell in enumerate(cells):
                                    expected_value = expected[i][j]
                                    actual_value = cell.text
                                    assert expected_value == actual_value, f"Table data mismatch at Row {i+1}, Column {j+1}"
                            browser.find_by_name("submit").click()

                            if(browser.is_text_present("You can not submit more than twice in a day")):
                                browser.find_by_name("submit").click() 
                                print("Booking 3 was denied because a 3rd room can't be booked for one day")

                            else:
                                assert browser.is_text_present("Submission was a success"), "Couldn't confirm the booking"

                        else:
                            assert browser.is_element_present_by_id("myTable"), "Table to show options selected for the room booking doesn't exist"

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