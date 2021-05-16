pipeline {
    agent any
    environment {
        CC = 'clang'
    }
    stages {
        stage('Stage 1: Checkout') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                checkout scm
            }
        }
        stage('Stage 2: Build') {
            steps {
                echo 'Building..'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Stage 3: Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m pytest --alluredir=Reports TestSuites/testsuite.py'
            }
        }
        stage('Stage 4: Deploy') {
            steps {
                echo 'Deploying....'
                sh 'mv Reports ~/Documents/NordicCoder/allureReports'
            }
        }
    }
}