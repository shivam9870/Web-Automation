import time

from selenium import webdriver


def test_open_page():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.refresh()
    time.sleep(2)
    driver.get("https://www.bing.com")
    driver.refresh()
    time.sleep(2)
    driver.back()
