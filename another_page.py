from selenium import webdriver
import time

# This function will click to go to another (next) page 2,3,4,5,6...
def go_to_page(page_number):
    driver = webdriver.Chrome()
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    button = driver.find_elements("css selector", "ul.css-1g90gv6 li a")[page_number]
    button.click()

    time.sleep(3)


go_to_page(2)
