# Fluent wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


@pytest.mark.positive
# pytest -k "positive" - to run the all positive test cases
# pytest -k "negative" - to run the all negative test cases
def test_vwo_webpagePositive():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    name = driver.find_element(By.XPATH, "//input[@id='login-username']")
    name.send_keys("contact+atb5x@thetestingacademy.com")
    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("ATBx@1234")
    button_click = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    button_click.click()


    # fluent wait
    #  FLUENT WAIT  -> Condition + frequency, -> Customize exception
    # e1 -> Frequency = 1 , check after 1 sec element visible? 2,3,4,5,?,6?,7 (visible) -> move to next command

    ignore_list = [ElementNotSelectableException,ElementNotVisibleException]
    wait = WebDriverWait(driver,15, poll_frequency=1, ignored_exceptions=ignore_list)
    element = EC.presence_of_element_located((By.CSS_SELECTOR,".page-heading"))

    print(driver.title)

    driver.quit()
