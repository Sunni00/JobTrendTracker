from selenium import webdriver
import time

vacancy = None
company = None
salary = None
typee = None

def data():    
    print("we are in data function")
    driver = webdriver.Chrome()
 
    time.sleep(8)

    vacancy = driver.find_element('css selector', 'h1.css-1b4cr5z span').text
    print("we get the text: ", vacancy)
    company = driver.find_element('css selector', 'span.css-1saizt3').text
    print('we get the company name: ', company)
    salary = driver.find_element('css selector', 'span.css-19j1a75').text
    print('we get the company name: ', salary)
    typee = driver.find_element('css selector', 'span.css-k5flys').text
    print('we get the company name: ', typee)

    return vacancy, company, salary, typee

