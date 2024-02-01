from selenium import webdriver
import logging


def test_open_page():
    driver = webdriver.Chrome()
    Logger = logging.getLogger(__name__)
    driver.get("https://google.com")
    Logger.info(driver.title)
