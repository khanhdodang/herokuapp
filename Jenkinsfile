pipeline {
	agent any

	stages {
    stage('Checkout') { // Checkout the repository containing your deploy automation
      steps {
        checkout scm
       }
     }
   }

   stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }

}