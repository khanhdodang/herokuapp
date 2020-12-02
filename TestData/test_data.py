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

  def get_account(self):
    utility = Utility()
    return utility.read_csv(Data.ACCOUNTS_CSV_FILE)
