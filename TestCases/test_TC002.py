"""
TC_002 : It is a test case to know the no. of links present on "Google" webpage.
Command to run : pytest TestCases -s -v --html=Reports\test_report.html
"""
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Test:

    def test_findNoOfLinks(self,setup):
        self.driver.implicitly_wait(10)
        noOfLinks = self.driver.find_elements(By.TAG_NAME,"a")
        print("Total links are:",len(noOfLinks))