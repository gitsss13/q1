pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               git branch: 'main', url: 'https://github.com/gitsss13/q1.git'
            }
        }

        stage('Install Dependencies') {
                  stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest' // Installs pytest directly without needing the file
            }
        }

        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest -q'
            }
        }
    }
}
