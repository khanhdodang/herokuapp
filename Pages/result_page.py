from Pages.base_page_object import BasePage
from Locators.locators import ResultPageLocators
import logging


class ResultPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def get_message(self):
    return self.get_text(ResultPageLocators.LABEL_MESSAGE)
