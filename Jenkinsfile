pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Run'){
            steps {
                sh 'python3 main.py'
            }
        }
    }
}