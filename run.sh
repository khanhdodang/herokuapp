virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
py.test --alluredir=%allure_result_folder% TestSuites/testsuite.py
allure serve %allure_result_folder%
source ./env/bin/deactivate