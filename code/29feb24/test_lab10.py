# On ebay.com search 16 gb and print all the name of items

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_ebay():
    driver = webdriver.Edge()
    driver.get("https://www.ebay.com/")
    search_box = driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    search_box.send_keys("16 gb")
    search_btn = driver.find_element(By.XPATH,"//input[@id='gh-btn']")
    search_btn.click()
    time.sleep(2)
    items = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in items:
        print(i.text)

    driver.quit()