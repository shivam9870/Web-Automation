# HERE WE WRITE THE NEGATIVE AND POSITIVE TEST CASES

# Here we automate the 'Katalon Healthcare' Page
# We automate the appointment with the help of selenium
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_open_page():
    driver = webdriver.Edge()
    url = "https://katalon-demo-cura.herokuapp.com"
    driver.get(url)
    mke_apt = driver.find_element(By.ID, "btn-make-appointment")
    mke_apt.click()
    time.sleep(2)
    name = driver.find_element(By.XPATH, "//input[@id='txt-username']")
    name.click()
    name.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.click()
    password.send_keys("ThisIsNotAPassword")
    login = driver.find_element(By.ID, "btn-login")
    # error_msg = driver.find_element(By.XPATH, "//p[@class='lead text-danger']")
    login.click()
    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error wrong URL"
    time.sleep(1)
    driver.quit()



def test_open_page_neg():
    driver = webdriver.Edge()
    url = "https://katalon-demo-cura.herokuapp.com"
    driver.get(url)
    mke_apt = driver.find_element(By.ID, "btn-make-appointment")
    mke_apt.click()
    time.sleep(2)
    name = driver.find_element(By.XPATH, "//input[@id='txt-username']")
    name.click()
    name.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.click()
    password.send_keys("ThisIsNotAPassword")
    login = driver.find_element(By.ID, "btn-login")
    # error_msg = driver.find_element(By.XPATH, "//p[@class='lead text-danger']")
    login.click()
    print(driver.current_url)
    error_xpath= "//p[text()='Login failed! Please ensure the username and password are valid.']"
    error_msg = driver.find_element(By.XPATH,error_xpath)
    assert error_msg == error_xpath, "Error credentials"
    driver.quit()