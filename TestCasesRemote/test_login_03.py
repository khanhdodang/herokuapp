import sys

sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.result_page import ResultPage
from TestCasesRemote.base_test_remote import BaseTest
from TestData.test_data import TestData


class HerokuAppLogin3(BaseTest):
  """A sample test class to show how page object works"""

  @classmethod
  def setUp(self):
    super().setUp()

  @classmethod
  def tearDown(self):
    super().tearDown()

  @unittest.SkipTest
  def test_login_with_invalid_username_password(self):
    login_page = LoginPage(self.driver)
    login_page.login(TestData.FAKE_USERNAME, TestData.FAKE_PASSWORD)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    self.assertIn("Your password is invalid!", result_page.get_message())


if __name__ == "__main__":
  unittest.main()
