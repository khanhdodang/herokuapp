import sys

sys.path.append(".")

from Utils.utils import Utility


class Data():
  BASE_URL = 'https://the-internet.herokuapp.com/login'
  USERNAME = 'tomsmith'
  FAKE_USERNAME = 'khanhdo'
  PASSWORD = 'SuperSecretPassword!'
  FAKE_PASSWORD = 'SuperSecretPassword'
  BROWSER = 'chrome'

  ACCOUNTS_CSV_FILE = './TestData/accounts.csv'
  ACCOUNTS_JSON_FILE = './TestData/accounts.json'

  def get_account_csv(self):
    utility = Utility()
    return utility.read_csv(Data.ACCOUNTS_CSV_FILE)

  def get_account_json(self):
    utility = Utility()
    return utility.read_json(Data.ACCOUNTS_JSON_FILE)
