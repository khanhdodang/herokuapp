import os
import sys

sys.path.append(".")
import unittest
from Utils.HTMLTestRunner import *
from TestCasesRemote.test_login_01 import HerokuAppLogin1
from TestCasesRemote.test_login_02 import HerokuAppLogin2
from TestCasesRemote.test_login_03 import HerokuAppLogin3

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Login class
login1 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin1)
login2 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin2)
login3 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin3)

# create a test suite
test_suite = unittest.TestSuite([login1, login2, login3])

# open the report file
outfile = open(dir + "/SeleniumPythonTestSummary.html", 'wb')

# configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
outfile.close()
