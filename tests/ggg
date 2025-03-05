from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://gor-pathology.web.app/")
    driver.find_element(By.NAME, "email").send_keys("test@kennect.io")
    driver.find_element(By.NAME, "password").send_keys("Qwerty@1234")
    driver.find_element(By.TAG_NAME, "button").click()
    assert "/home" in driver.current_url
    driver.quit()
