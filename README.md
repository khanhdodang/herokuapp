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

#### Start WebDriver Server

- Download selenium server standalone [here](https://www.selenium.dev/downloads/)

- Refer to https://www.selenium.dev/documentation/en/remote_webdriver/remote_webdriver_server/

- Launch server with the command below:
```
java -jar selenium-server-standalone-{VERSION}.jar
```

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
