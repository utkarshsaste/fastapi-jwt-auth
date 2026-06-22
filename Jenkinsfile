pipeline {
    agent any

    stages {

        stage('Download Code') {
            steps {
                echo 'Downloading code from GitHub'
            }
        }

        stage('Install Packages') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Check Python Files') {
            steps {
                bat 'dir'
            }
        }

        stage('Success') {
            steps {
                echo 'Project Build Successful'
            }
        }
    }
}
