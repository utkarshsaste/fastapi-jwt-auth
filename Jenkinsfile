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
                sh 'pip install -r practice1/requirements.txt'
            }
        }

        stage('Check Python Files') {
            steps {
                sh 'python -m py_compile practice1/*.py'
            }
        }

        stage('Success') {
            steps {
                echo 'Project Build Successful'
            }
        }
    }
}