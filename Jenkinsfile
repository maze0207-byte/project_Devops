pipeline {
    agent any

    environment {
        BACKEND_IMAGE = "mybackend:latest"
        FRONTEND_IMAGE = "myfrontend:latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/maze0207-byte/project_Devops.git']]
                ])
            }
        }

        stage('Build Docker Images') {
            steps {
                bat 'docker-compose build'
            }
        }

        stage('Start Containers') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test Backend API') {
            steps {
                bat 'curl http://localhost:5000/test || exit 1'
            }
        }

        stage('Show Running Containers') {
            steps {
                bat 'docker ps'
            }
        }

        /* -------------------------
           PROMETHEUS + GRAFANA
        ------------------------- */
        stage('Start Monitoring (Prometheus + Grafana)') {
            steps {
                echo "Starting Prometheus and Grafana..."
                bat 'docker-compose up -d prometheus grafana'

                echo "Testing Prometheus endpoint..."
                bat 'curl http://localhost:9090 || exit 1'

                echo "Testing backend metrics endpoint..."
                bat 'curl http://localhost:5000/metrics || exit 1'
            }
        }
        
        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                bat 'docker tag backend mazen2025/backend:latest'
                bat 'docker push mazen2025/backend:latest'
                bat 'docker tag frontend mazen2025/frontend:latest'
                bat 'docker push mazen2025/frontend:latest'
            
            }
        }
            
        post {
           always {
                echo "Pipeline finished!"
           }
        }  
    }
}
       
