import os
import sys
import unittest

from selenium import webdriver

from TestData.test_data import Data

sys.path.append('.')


# Base Class for the tests
class BaseTest(unittest.TestCase):

  @classmethod
  def setUp(self):
    # Setting up how we want Chrome to run
    browser = self.get_browser()
    self.driver = self.startBrowser(browser)
    self.driver.maximize_window()

  @classmethod
  def tearDown(self):
    # To do the cleanup after test has executed.
    try:
      self.driver.close()
      self.driver.quit()
    except Exception as e:
      pass

  def startBrowser(self, name='chrome'):
    """
    browsers= firefox, chrome, ie, phantomjs
    """
    try:
      if name.lower() == 'firefox' or name.lower() == 'ff':
        print('start browser name :Firefox')
        # return webdriver.Firefox(executable_path=r'')
        return webdriver.Firefox()
      elif name.lower() == 'chrome':
        print('start browser name :Chrome')
        # return webdriver.Chrome(executable_path=r'')
        return webdriver.Chrome(executable_path=r'/opt/homebrew/bin/chromedriver')
      elif name.lower() == 'phantomjs':
        print('start browser name :phantomjs')
        return webdriver.PhantomJS()
      else:
        print("Not found this browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘")
        return webdriver.Firefox()
    except Exception as msg:
      print('message: %s' % str(msg))

  def get_browser():
    try:
      return os.environ['BROWSER']
    except:
      return Data.BROWSER
