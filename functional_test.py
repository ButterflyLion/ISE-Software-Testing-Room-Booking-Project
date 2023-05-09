from splinter import Browser

browser = Browser()
url = 'http://localhost'
browser.visit(url)
assert browser.is_text_present('hello world')
browser.quit()