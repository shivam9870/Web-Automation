# selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_page():
    driver = webdriver.Edge()
    driver.get("https://www.flipkart.com/")
    print(driver.title)
    time.sleep(2)
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
    search_box.send_keys("iphone 15 pro")
    search_btn = driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More']//*[name()='svg']")
    search_btn.click()
    time.sleep(5)
    driver.quit()

# always use the Relative Xpath
# Don't use the Absolute Xpath

# Absoulte Xpath example = /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[
# 1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]
# Relative Xpath example = //*[name()='path' and contains(@d,'M10.5 18C1')]
