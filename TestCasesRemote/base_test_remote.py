import os
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from TestData.test_data import TestData

sys.path.append(".")


# Base Class for the tests
class BaseTest(unittest.TestCase):

  @classmethod
  def setUp(self):
    # Setting up how we want Chrome to run
    browser = self.get_browser()
    self.driver = self.startBrowserRemote(browser)
    self.driver.maximize_window()

  @classmethod
  def tearDown(self):
    # To do the cleanup after test has executed.
    self.driver.close()
    try:
      self.driver.quit()
    except Exception as e:
      pass

  def startBrowserRemote(name="chrome"):
    """
    browsers，"firefox"、"chrome"、"ie"、"phantomjs"
    https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.desired_capabilities.html
    """
    try:
      if name.lower() == "firefox" or name.lower() == "ff":
        print("start browser name :Firefox")
        # return webdriver.Firefox(executable_path='')
        return webdriver.Remote(
          command_executor='http://127.0.0.1:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.FIREFOX)
      elif name.lower() == "chrome":
        print("start browser name :Chrome")
        return webdriver.Remote(
          command_executor='http://127.0.0.1:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
      elif name.lower() == "edge":
        print("start browser name :Edge")
        return webdriver.Remote(
          command_executor='http://127.0.0.1:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.EDGE)
      elif name.lower() == "phantomjs":
        print("start browser name :phantomjs")
        return webdriver.Remote(
          command_executor='http://127.0.0.1:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.PHANTOMJS)
      else:
        print("Not found this browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘")
    except Exception as msg:
      print("message: %s" % str(msg))

  def get_browser():
    try:
      return os.environ['BROWSER']
    except KeyError:
      return TestData.BROWSER
