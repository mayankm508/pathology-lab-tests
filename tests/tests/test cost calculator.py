from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cost_calculator():
    driver = webdriver.Chrome()
    driver.get("https://gor-pathology.web.app/")
    
    # Login
    driver.find_element(By.NAME, "email").send_keys("test@kennect.io")
    driver.find_element(By.NAME, "password").send_keys("Qwerty@1234")
    driver.find_element(By.TAG_NAME, "button").click()
    
    # Navigate to cost calculator
    driver.find_element(By.ID, "cost-calculator").click()
    driver.find_element(By.ID, "test1").click()
    driver.find_element(By.ID, "test2").click()
    driver.find_element(By.ID, "calculate").click()
    
    total_cost = driver.find_element(By.ID, "total-cost").text
    assert total_cost != ""
    driver.quit()
