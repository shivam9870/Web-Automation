import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo_webpage():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    name = driver.find_element(By.XPATH, "//input[@id='login-username']")
    name.send_keys("admin")
    password= driver.find_element(By.XPATH,"//input[@id='login-password']")
    password.send_keys("admin")
    time.sleep(2)
    button_click = driver.find_element(By.XPATH,"//button[@id='js-login-btn']")
    button_click.click()
    print(driver.title)
    time.sleep(3)