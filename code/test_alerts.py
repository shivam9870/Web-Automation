# Alerts handling

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alerts1():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    js_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
    js_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)
    driver.quit()


def test_alert2():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    js_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
    js_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()  # For OK
    # alert.dismiss() # For CANCEL

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)
    driver.quit()


def test_alerts3():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    js_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
    js_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("shivam")
    alert.accept()

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)
    driver.quit()
