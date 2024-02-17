# App.vwo | Negative and positive test cases

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_positive_login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    login = driver.find_element(By.XPATH,"//input[@id='login-username']")
    login.send_keys("contact+atb5x@thetestingacademy.com")
    password = driver.find_element(By.XPATH,"//input[@id='login-password']")
    password.send_keys("ATBx@1234")
    login_but = driver.find_element(By.XPATH,"//span[@data-qa='ezazsuguuy']")
    login_but.click()
    print(driver.title)
    time.sleep(5)
    driver.quit()


def test_negative_login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    login = driver.find_element(By.XPATH,"//input[@id='login-username']")
    login.send_keys("admin")
    password = driver.find_element(By.XPATH,"//input[@id='login-password']")
    password.send_keys("admin")
    login_but = driver.find_element(By.XPATH,"//span[@data-qa='ezazsuguuy']")
    login_but.click()
    print(driver.title)
    time.sleep(5)
    driver.quit()