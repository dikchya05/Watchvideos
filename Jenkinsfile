pipeline {
    agent any

    environment {
        NODE_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dikchya05/Watchvideos.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'node -v'
                bat 'npm install --legacy-peer-deps'
            }
        }

        stage('Build') {
            steps {
                bat 'npm run build'
            }
        }

        stage('Test') {
            steps {
                bat 'npm test'
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}