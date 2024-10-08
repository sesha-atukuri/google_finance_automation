import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/finance")
    request.cls.driver = driver
    yield
    driver.quit()
