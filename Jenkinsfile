pipeline {
    agent any

    stages {
        stage('Stage 1: Checkout') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '2f1c8efe-7033-426a-8c1c-2897cd65e2fe', url: 'https://github.com/khanhdodang/herokuapp.git']]])
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
                sh 'cp Reports/* ~/Documents/NordicCoder/allureReports/Reports/ '
            }
        }
    }
}