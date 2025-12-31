pipeline {
    agent any

    environment {
        // Environment variables for publishing can be set in Jenkins credentials
        // TWINE_USERNAME = credentials('nexus-username')
        // TWINE_PASSWORD = credentials('nexus-password')
        // TWINE_REPOSITORY_URL = 'https://your-nexus-repo-url/repository/pypi-internal/'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install uv tox'
                sh 'uv sync'
            }
        }

        stage('Static Analysis') {
            steps {
                // Run linting and type checking via tox
                sh 'tox -e lint,type'
            }
        }

        stage('Test') {
            steps {
                // Run tests for all packages via tox
                sh 'tox -e dag-utils'
            }
        }

        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                // Build individual packages
                sh 'uv build --package dlh-dag-utils'
            }
        }

        stage('Publish') {
            when {
                branch 'main'
            }
            steps {
                // Publish built packages
                // Ensure TWINE_REPOSITORY_URL is set if not using PyPI
                sh 'uv publish dist/*'
            }
        }
    }
}
