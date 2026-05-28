pipeline {
    agent any
    stages {
        stage('Clone Code') {
            steps {
                //Replace with your Github repository URL
                git branch: 'main', url: 'https://github.com/snehiljain34/jenkins.git'
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t flask-app:latest .'
            }
        }
        stage('Deploy with Docker Compose'){
            steps{
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
    }
}