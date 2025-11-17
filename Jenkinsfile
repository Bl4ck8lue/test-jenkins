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
            steps {
                script {
                    // 1) scanner tool name must match "Name" in Manage Jenkins -> Global Tool Configuration -> SonarScanner
                    def scannerHome = tool 'SonarQube'  
                    // 2) Sonar server name must match "Name" in Manage Jenkins -> Configure System -> SonarQube servers
                    withSonarQubeEnv('SonarCloud') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

    }
}