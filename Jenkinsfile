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
                sh 'python3 script.py vlad pochta@yandex.ru qwerty'
            }
        }
        stage('SonarQube analysis') {
            sh 'echo Run SAST - SonarQube analysis'
            def scannerHome = tool 'sonar_scanner';
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=myapp"
            }
        }
        stage("SonarQube Quality Gate") {
            waitForQualityGate abortPipeline: true
        }
    }
}