"""
TC_001 : It is a test case to print the title of webpage.
"""

import pytest


@pytest.mark.usefixtures("setup")
class Test:

    def test_printGoogleTitle(self, setup):
        self.driver.get("https://www.google.com")
        print("The title is :", self.driver.title)
