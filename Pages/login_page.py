from Pages.base_page_object import BasePage
from Locators.locators import LoginPageLocators
import logging
from TestData.test_data import Data


class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    self.navigate_to(Data.BASE_URL)

  def login(self, username, password):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)
    self.click(LoginPageLocators.BUTTON_LOGIN)

  def login_object(self, account):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
    self.click(LoginPageLocators.BUTTON_LOGIN)

  def is_title_matches(self):
    logging.info("Check the title match or not")
    """Verifies that the hardcoded text "The Internet" appears in page title"""
    return "The Internet" in self.get_title()
