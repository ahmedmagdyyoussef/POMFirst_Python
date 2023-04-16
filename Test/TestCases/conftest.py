import pytest
from selenium import webdriver

@pytest.fixture
def Driver():
    Driver = webdriver.Chrome()
    Driver.maximize_window()
    Driver.get("https://www.youtube.com/")
    yield Driver
    Driver.close()
