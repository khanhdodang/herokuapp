import sys

sys.path.append(".")
import unittest
from TestCasesRemote.test_login_01 import HerokuAppLogin1
from TestCasesRemote.test_login_02 import HerokuAppLogin2
from TestCasesRemote.test_login_03 import HerokuAppLogin3

# get all tests from Login class
login1 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin1)
login2 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin2)
login3 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin3)

# create a test suite
test_suite = unittest.TestSuite([login1, login2, login3])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
