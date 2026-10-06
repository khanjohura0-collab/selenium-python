import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google(driver):
    driver.get("https://www.selenium.dev")
    driver.find_element(By.LINK_TEXT, "Downloads").click()
    assert "Downloads" in driver.title

def test_selenium_homepage_title(driver):
    driver.get("https://www.selenium.dev")
    assert "Selenium" in driver.title