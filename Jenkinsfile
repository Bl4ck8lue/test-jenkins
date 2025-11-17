pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Run'){
            steps {
                sh 'python3 main.py'
            }
        }
        stage('Run one more'){
            steps {
                sh 'python script.py vlad pochta@yandex.ru qwerty'
            }
        }
    }
}