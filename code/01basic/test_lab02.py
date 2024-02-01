import time

from selenium import webdriver
import logging
import os


def test_open_page():
    chrome_option = webdriver.ChromeOptions()
    # Give some extra argument or extension or anything to chrome
    # Chrome Options - Chrome with extensions, Window size, Proxy, JS disabled/enabled
    extension_path = "C:/Users/Shivam/Downloads/adblocker.crx"
    chrome_option.add_extension(extension_path)
    chrome_option.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_option)
    Logger = logging.getLogger(__name__)
    driver.get("https://google.com")
    Logger.info(driver.title)
    time.sleep(20000)
