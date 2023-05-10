from splinter import Browser
browser = Browser('chrome')
url = 'http://localhost:5000'
browser.visit(url)
assert browser.is_text_present('hello world')
browser.quit()