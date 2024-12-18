from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException, ElementNotInteractableException
import time
from getting_data import data
from database import connecting_to_database

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(r"--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument(r"--profile-directory=Profile 4")

ttime = 5
    

def clicking_to_links():
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
            print("clicking_to_links is successfully")
            break
        except Exception as e:
            print('first, TRY AGAIN!!!!!!!!')
            time.sleep(5)


    wait = WebDriverWait(driver, timeout=2)

    while True:
        try:
            links = driver.find_elements("css selector", "ul.css-1faftfv li div div div div div div table tbody tr td div h2 a")
            for link in links:
                print(link.get_attribute('href'))
                time.sleep(3)
                connecting_to_database(link.get_attribute('href'))
                print("we got the link, we are going to get the function data .......")
                data()
            break
        except Exception as e:
            time.sleep(5)
            # clicking_to_links()
        
        

    print('time to sleep 10 seconds')
    time.sleep(10)
    # Ensure the browser closes
    driver.close()



