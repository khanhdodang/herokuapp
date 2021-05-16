herokuapp
================


#### Install

* git clone <this repo>; cd herokuapp
* pip3 install virtualenv --user
* virtualenv env
* source ./env/bin/activate

Note:

- Upgrade pip if you want `python3 -m pip install --user --upgrade pip`

##### Then, do this (all platforms)

Install the remaining requirements:

* pip install -r requirements.txt

#### Download drivers and put them into Drivers folder

- chromedriver https://chromedriver.chromium.org/downloads
- geckodriver https://github.com/mozilla/geckodriver/releases

**Note for Mac OS:**

- To install chromedriver, run:
  `brew install chromedriver`
  
- To re-install chromedriver, run:
  `brew reinstall chromedriver`

#### Start WebDriver Server

- Download selenium server standalone [here](https://www.selenium.dev/downloads/)

- Refer to https://www.selenium.dev/documentation/en/remote_webdriver/remote_webdriver_server/

- Launch server with the command below:
```
java -jar selenium-server-standalone-{VERSION}.jar
```

**Note for Mac OS:**

- Install selenium server standalone using: `brew install selenium-server-standalone`
- To have launchd start selenium-server-standalone now and restart at login:
  `brew services start selenium-server-standalone`
- Or, if you don't want/need a background service you can just run:
  `selenium-server -port 4444`

#### Run

##### Testing with single test case at local:

```
python3 TestCases/test_login_01.py
python3 TestCases/test_login_02.py
python3 TestCases/test_login_03.py
python3 TestCases/test_login_04.py
```

##### Testing with single test case at remote:

```
python3 TestCasesRemote/test_login_01.py
python3 TestCasesRemote/test_login_02.py
python3 TestCasesRemote/test_login_03.py
python3 TestCasesRemote/test_login_04.py
```

##### Testing with test suite at local

```
python3 TestSuites/testsuite.py
python3 TestSuites/testsuite_html_report.py
```

##### Testing with test suite at remote

```
python3 TestSuitesRemote/testsuite.py
python3 TestSuitesRemote/testsuite_html_report.py
```

##### Testing with test suite and generate allure report

```

python -m pytest --alluredir=%allure_result_folder% TestSuites/testsuite.py
```


Start server

```
allure serve %allure_result_folder%
```
