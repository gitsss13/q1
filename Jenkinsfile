pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch:'main', url:'https://github.com/gitsss13/q5.git'
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Unit Check') {
                    steps {
                        sh 'python3 unit_check.py'
                    }
                }

                stage('Integration Check') {
                    steps {
                        sh 'python3 integration_check.py'
                    }
                }
            }
        }

        stage('Summary') {
            steps {
                echo 'All checks passed. Summary is complete.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}