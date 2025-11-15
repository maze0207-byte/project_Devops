pipeline {
    agent any

    environment {
        BACKEND_IMAGE = "mybackend:latest"
        FRONTEND_IMAGE = "myfrontend:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/username/your-repo.git' 
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                dir('backend-flask') {
                    sh 'docker build -t $BACKEND_IMAGE .'
                }
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                dir('frontend-html') {
                    sh 'docker build -t $FRONTEND_IMAGE .'
                }
            }
        }

        stage('Stop & Remove Existing Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }   

        stage('Verify Services') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo " Pipeline executed successfully!"
        }
        failure {
            echo " Pipeline failed!"
        }
    }
}
