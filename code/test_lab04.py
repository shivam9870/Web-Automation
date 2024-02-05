# Here we automate the 'Katalon Healthcare' Page
# We automate the appointment with the help of selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_page():
    driver = webdriver.Edge()
    url = "https://katalon-demo-cura.herokuapp.com"
    driver.get(url)
    mke_apt = driver.find_element(By.ID,"btn-make-appointment")
    mke_apt.click()
    time.sleep(2)
    name = driver.find_element(By.XPATH,"//input[@id='txt-username']")
    name.click()
    name.send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password")
    password.click()
    password.send_keys("ThisIsNotAPassword")
    login = driver.find_element(By.ID,"btn-login")
    login.click()
    time.sleep(3)