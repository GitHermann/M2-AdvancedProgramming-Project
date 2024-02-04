pipeline {
  agent {
    label 'advancedProgramming-slave'
  }
  stages {
    stage('Cloning Github Repository') {
      steps {
        git branch: 'main', credentialsId: 'GitHubFchar', url: 'https://github.com/GitHermann/M2-AdvancedProgramming-Project.git'
      }
    }
    stage('Building Frontend Image') {
      steps {
        script {
          dir('frontend') {
            bat 'docker build -t francoischarvet/advanced-programming-frontend:1.0 .'
          }
        }
      }
    }
	  stage('Publish Frontend Image') {
      steps {
        bat 'docker push francoischarvet/advanced-programming-frontend:1.0'
      }
    }
    stage('Building Internships Service Image') {
      steps {
        script {
          dir('backend/project/internships') {
            bat 'docker build -t francoischarvet/advanced-programming-internships:1.0 .'
          }
        }
      }
    }
	  stage('Publish Internships Service Image') {
      steps {
        bat 'docker push francoischarvet/advanced-programming-internships:1.0'
      }
    }
    stage('Building InternshipSpaces Service Image') {
      steps {
        script {
          dir('backend/project/internshipSpaces') {
            bat 'docker build -t francoischarvet/advanced-programming-internshipspaces:1.0 .'
          }
        }
      }
    }
	  stage('Publish InternshipSpaces Service Image') {
      steps {
        bat 'docker push francoischarvet/advanced-programming-internshipspaces:1.0'
      }
    }
	  stage('Building Users Service Image') {
      steps {
        script {
          dir('backend/project/users') {
            bat 'docker build -t francoischarvet/advanced-programming-users:1.0 .'
          }
        }
      }
    }
	  stage('Publish Users Service Image') {
      steps {
        bat 'docker push francoischarvet/advanced-programming-users:1.0'
      }
    }
    stage('Building Documents Service Image') {
      steps {
        script {
          dir('backend/project/documents') {
            bat 'docker build -t francoischarvet/advanced-programming-documents:1.0 .'
          }
        }
      }
    }
	  stage('Publish Documents Service Image') {
      steps {
        bat 'docker push francoischarvet/advanced-programming-documents:1.0'
      }
    }
	  stage('Starting Minikube') {
	    steps {
	      script {
		      bat 'minikube start'
		    }
	    }
	  }
	  stage('Enable Ingress') {
	    steps {
	      script {
			    bat 'minikube addons enable ingress'
			    bat 'minikube addons enable ingress-dns'
		    }
	    }
	  }
	  stage('Apply Deployments') {
      steps {
	      script {
		      dir('config') {
            bat 'kubectl apply -f kube-deployments.yml'
		      }
		    }
      }
    }
	  stage('Apply Services') {
      steps {
	      script {
		      dir('config') {
            bat 'kubectl apply -f kube-services.yml'
		      }
		    }
      }
    }
	  stage('Apply Ingress Config') {
      steps {
	      script {
		      dir('config') {
            bat 'kubectl apply -f ingress.yml'
		      }
		    }
      }
    }
    stage('Display Pods, Services and Deployments Information') {
      steps {
	      script {
            bat 'kubectl get pods,services,deployments'
		    }
      }
    }
  }
}
