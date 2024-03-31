# explicit waits

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)

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
    print(driver.title)
    # time.sleep(5) # wait for 5 sec to load the page
    # here we observe the problem to load the element
    # so here we add the condition, webdriver wait for that condition

    # 1st way : by dashboard -> (use this always because dashboard is constant)

    WebDriverWait(driver,15).until(
        EC.text_to_be_present_in_element((By.XPATH,"//h1[@class='page-heading']"), text_="Dashboard")
    )

    # # 2nd method : by Aman name -> (  Aman name is not constant vary upon username )

    # WebDriverWait(driver, 15).until(
    #     EC.text_to_be_present_in_element((By.XPATH, "//span[@data-qa='lufexuloga']"), text_="Aman")
    # )

    heading_name = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    assert heading_name.text == "Aman"
    # time.sleep(5) # for loading page successfully

    driver.quit()
