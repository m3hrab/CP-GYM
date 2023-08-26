from selenium import webdriver
import time

driver = webdriver.Chrome()

def get_browser_url():
    previous_url = None
    
    while True:
        browser_url = driver.current_url
        
        if browser_url != previous_url:
            print("Browser URL:", browser_url)
            previous_url = browser_url
        
        time.sleep(1)


get_browser_url()
