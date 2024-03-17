# Implicit waits

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.positive
# pytest -k "positive" - to run the all positive test cases
# pytest -k "negative" - to run the all negative test cases
def test_vwo_webpagePositive():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(20)
    name = driver.find_element(By.XPATH, "//input[@id='login-username']")
    name.send_keys("contact+atb5x@thetestingacademy.com")
    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("ATBx@1234")
    button_click = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    button_click.click()
    print(driver.title)
    # time.sleep(5) # wait for 5 sec to load the page
    heading_name = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    assert heading_name.text == "Aman"
    # time.sleep(5) # for loading page successfully

    driver.quit()
