from splinter import Browser
from selenium import webdriver
# https://splinter.readthedocs.io/en/latest/api/driver-and-element-api.html
# https://splinter.readthedocs.io/en/latest/tutorial.html
# https://www.youtube.com/watch?v=ApA7EVwSzg0

# change path to chrome driver to your own! (download from here: https://chromedriver.chromium.org/)
executable_path = {'executable_path':r'C:\Users\novel\workspace\Year1Sem2\Room Booking Project\chromedriver'}
# set some default behaviours for our browser
options = webdriver.ChromeOptions()
# make sure the window is maximised
options.add_argument("--start-maximized")

# create a new browser object, by default it is firefox. If headless is set to true then it will open a browser but you won't see it.
browser = Browser('chrome', **executable_path, headless=False, options=options)
# specify what page we want it to visit
url = 'http://localhost:5000'
browser.visit(url)
# first we want it to login
# find idnum element
username_box = browser.find_by_name("username")
# fill out the element
username_box.fill("1@studentmail.ul.ie")
# find the password element and fill
password_box = browser.find_by_name("password").fill("12345")
# click the login button
login = browser.find_by_value("Log In").first.click()

# Welcome page:
make_a_booking_button = browser.find_by_name("submit").click()

# Guests page:
no_of_guests = browser.find_by_id("guests").fill(1)
# click next button
next_button = browser.find_by_name("submit").click()

# Rooms page:
table = browser.find_by_id("tbl")
button_class = "btn bookbtn"
button = table.find_by_css(button_class).first
button.click()

# Dates page:

# Hours page:

# Confirm page:



browser.quit()