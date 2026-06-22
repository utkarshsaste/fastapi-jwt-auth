pipeline {
    agent any

    stages {

        stage('Install Packages') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Check Python Files') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m py_compile *.py'
            }
        }

        stage('Success') {
            steps {
                echo 'Project Build Successful'
            }
        }
    }
}
