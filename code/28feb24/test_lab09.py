# xpath using contains attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_openpage():
    # partial text Xpath
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_apt_but = driver.find_element(By.XPATH,"//a[contains(text(),'Make App')]")
    make_apt_but.click()
    time.sleep(2)
    driver.quit()

