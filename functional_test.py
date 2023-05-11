from splinter import Browser
# https://splinter.readthedocs.io/en/latest/api/driver-and-element-api.html
# https://splinter.readthedocs.io/en/latest/tutorial.html

browser = Browser('chrome')
url = 'http://localhost:5000'
browser.visit(url)
assert browser.is_text_present('hello world')
browser.quit()