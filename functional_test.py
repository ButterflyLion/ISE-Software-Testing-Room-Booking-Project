from splinter import Browser
from selenium.webdriver.chrome.service import Service

my_service = Service()
browser = Browser('chrome', service=my_service)

url = 'http://localhost'
browser.visit(url)
assert browser.is_text_present('hello world')
browser.quit()

