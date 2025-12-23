from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()