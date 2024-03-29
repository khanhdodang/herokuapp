import sys

sys.path.append(".")
import unittest
from Pages.login_page import LoginPage
from Pages.result_page import ResultPage
from TestCasesRemote.base_test_remote import BaseTest
from TestData.test_data import Data
from Objects.account import Account


class HerokuAppLogin4(BaseTest):
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

    account = Account(Data.USERNAME, Data.PASSWORD)
    login_page.login_object(account)
    result_page = ResultPage(self.driver)

    print(result_page.get_message())
    self.assertIn("You logged into a secure area!", result_page.get_message())


if __name__ == "__main__":
  unittest.main()
