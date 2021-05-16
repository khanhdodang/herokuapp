virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
py.test --alluredir=Reports TestSuites/testsuite.py
allure serve Reports
source ./env/bin/deactivate