from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
def test_login(driver):
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    sleep(5)
    assert driver.find_element(By.CSS_SELECTOR,".oxd-text--h6").text == "Dashboard"


def test_error_login(driver):
    driver.find_element(By.NAME,"username").send_keys("Admin12")
    driver.find_element(By.NAME,"password").send_keys("admin1234")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    assert driver.find_element(By.CSS_SELECTOR,".oxd-alert-content-text").text == "Invalid credentials"