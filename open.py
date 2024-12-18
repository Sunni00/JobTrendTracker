from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException, ElementNotInteractableException
import time
import pyperclip

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(r"--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument(r"--profile-directory=Profile 4")

ttime = 5

def finding_element(driver):
    result = driver.find_element(By.XPATH, '//*[@id="example_xpath"]/button')

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=2, ignored_exceptions=errors)
    wait.until(lambda d: result.send_keys("Displayed") or True)
    driver.execute_script("window.scrollBy(0, 800)")
    time.sleep(3)

    # Optional: Perform a click
    result.click()

    # Read from clipboard
    time.sleep(5)
    copied_link = pyperclip.paste()
    print('vacancy link: ', copied_link)

    return copied_link
    

def function_main():
    """Main function to open Chrome, search jobs, and get links."""
    global ttime
    # Trying infinitely to open chrome until cloudcatpcha dissapear 
    while True:

        try:
            # Initialize driver
            driver = webdriver.Chrome()#options=chrome_options)
            driver.get("https://www.example.com/?from=jobsearch")
            time.sleep(5)

            # Search for "data science"
            elem = driver.find_element(By.NAME, "q")
            elem.clear()
            elem.send_keys("data science")
            elem.send_keys(Keys.RETURN)
            time.sleep(5)
            break
        except Exception as e:
            print('first, TRY AGAIN!!!!!!!!')
            time.sleep(5)


    wait = WebDriverWait(driver, timeout=2)

    while True:

        # Try to locate the button element
        try:
            link = finding_element(driver)
            break
        except Exception as e:
            print('TRYING AGAIN!!!!!', e)
            time.sleep(ttime)
            function_main()
            ttime += 1

        
    
    # Ensure the browser closes
    driver.close()
    return link


