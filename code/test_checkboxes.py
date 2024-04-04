import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(2)
    checkbox = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")

    # check the boxes is not selected
    for c in checkbox:
        if not c.is_selected():
            c.click()

    time.sleep(5)
    driver.quit()