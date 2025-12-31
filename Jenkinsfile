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
                anyOf {
                    branch 'main'
                    tag 'dlh-dag-utils-v*'
                }
            }
            steps {
                // Build individual packages
                // When built from a tag, hatch-vcs produces a clean version (e.g., 0.1.0)
                // When built from main (no tag), it produces a dev version (e.g., 0.1.1.dev0+g...)
                sh 'uv build --package dlh-dag-utils'
            }
        }

        stage('Publish') {
            when {
                // Enforce tag-only releases
                tag 'dlh-dag-utils-v*'
            }
            steps {
                // Publish built packages
                // Ensure TWINE_REPOSITORY_URL is set if not using PyPI
                sh 'uv publish dist/*'
            }
        }
    }
}
