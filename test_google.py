import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google(driver):
    driver.get("https://www.selenium.dev")
    driver.find_element("link text", "Downloads").click()
    print(driver.title)