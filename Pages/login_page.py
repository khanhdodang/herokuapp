from Pages.base_page_object import BasePage
from Locators.locators import LoginPageLocators
import logging


class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to('url ')

  def login(self, account):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
    self.click(LoginPageLocators.BUTTON_LOGIN)

