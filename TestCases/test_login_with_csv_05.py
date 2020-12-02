import sys

sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.result_page import ResultPage
from TestCases.base_test import BaseTest
from TestData.test_data import Data
from Objects.account import Account


class HerokuAppLogin5(BaseTest):
  """A sample test class to show how page object works"""

  @classmethod
  def setUp(self):
    super().setUp()

  @classmethod
  def tearDown(self):
    super().tearDown()

  def test_login_successfully(self):
    accounts = Data.get_account(self)

    for account in accounts:
      username = account[0]
      password = account[1]
      message = account[2]
      account = Account(username, password)

      login_page = LoginPage(self.driver)
      self.assertTrue(login_page.is_title_matches())
      login_page.login_object(account)

      result_page = ResultPage(self.driver)
      self.assertIn(message, result_page.get_message())


if __name__ == "__main__":
  unittest.main()
