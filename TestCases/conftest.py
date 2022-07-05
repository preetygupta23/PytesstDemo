"""
It is a config file where common setup method is placed.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())  # To install Chrome driver and assign it to driver.
    driver.maximize_window()
    driver.get("https://www.google.com")
    request.cls.driver = driver                # Method specific driver object passed to calling method.
    yield
    driver.close()
