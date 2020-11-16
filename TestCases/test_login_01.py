import sys

sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.result_page import ResultPage
from TestCases.base_test import BaseTest
from TestData.test_data import TestData


class HerokuAppLogin1(BaseTest):
  """A sample test class to show how page object works"""

  @classmethod
  def setUp(self):
    super().setUp()

  @classmethod
  def tearDown(self):
    super().tearDown()

  def test_login_successfully(self):
    login_page = LoginPage(self.driver)
    self.assertTrue(login_page.is_title_matches())
    login_page.login(TestData.USERNAME, TestData.PASSWORD)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    self.assertIn("You logged into a secure area!", result_page.get_message())


if __name__ == "__main__":
  unittest.main()
