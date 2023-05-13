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
user_id_box = browser.find_by_id("idnum")
# fill out the element
user_id_box.fill(1)
# find the password element and fill
password = browser.find_by_id("password").fill("pswrd")

# click the login button
submit = browser.find_by_value("Log In").first.click()


browser.quit()