pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/cnuseenu/devops-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f devops-demo-container || true'
                sh 'docker run -d -p 5000:5000 --name devops-demo-container devops-demo'
            }
        }

    }
}
