# verified the title of the page

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_page():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)

    assert driver.title == "CURA Healthcare Service"

    driver.quit()