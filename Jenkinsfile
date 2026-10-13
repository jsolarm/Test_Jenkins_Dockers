pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '=== BUILD ==='

                script {
                    if (!fileExists('app.py')) {
                        error('No existe app.py')
                    }

                    if (!fileExists('test_app.py')) {
                        error('No existe test_app.py')
                    }

                    if (!fileExists('Dockerfile')) {
                        error('No existe Dockerfile')
                    }
                }

                bat 'docker build -t hello-world-jenkins .'
            }
        }

        stage('Test') {
            steps {
                echo '=== TEST ==='

                bat 'docker run --rm --entrypoint python hello-world-jenkins -m unittest -v test_app'
            }
        }

        stage('Deploy') {
            steps {
                echo '=== DEPLOY ==='

                bat 'docker rm -f hello-world-jenkins-test 2>NUL || exit /b 0'

                bat 'docker run --name hello-world-jenkins-test hello-world-jenkins'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizado correctamente.'
        }

        failure {
            echo 'El pipeline ha fallado. Revisa Console Output.'
        }
    }
}
