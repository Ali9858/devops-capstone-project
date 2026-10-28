DevOps Capstone Project
[![Build Status](https://github.com/Ali9858/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Ali9858/devops-capstone-project/actions/workflows/ci-build.yaml)

The microservice provides REST API endpoints for creating, reading, updating, deleting, and listing customer accounts.

Project Goals
Implement REST API endpoints for customer account management.
Develop automated unit and integration tests using nosetests.
Achieve at least 95% code coverage.
Apply secure coding practices, including CORS policies and security headers.
Build and run the application using Docker.
Automate testing and integrate code changes using GitHub Actions.
Support Kubernetes-based development and deployment.
Technology Stack
Language: Python 3.9
Web framework: Flask
Database: PostgreSQL
ORM: Flask-SQLAlchemy and SQLAlchemy
Testing: Nose, Coverage, and Factory Boy
Code quality: Flake8, Pylint, and Black
CI/CD: GitHub Actions
Containerization: Docker
Orchestration: Kubernetes and K3D
Pipeline tooling: Tekton
REST API Features

The service supports the following account management operations:

Operation	HTTP method	Description
Create account	POST	Create a customer account
Read account	GET	Retrieve an account by ID
List accounts	GET	Retrieve all customer accounts
Update account	PUT	Update an existing account
Delete account	DELETE	Delete an account by ID
Health check	GET	Check service health

The API includes request validation, appropriate HTTP status codes, CORS support, and security headers.

Account Data Model

Each account contains the following fields:

Field	Type	Required
id	Integer	Yes
name	String (64 characters)	Yes
email	String (64 characters)	Yes
address	String (256 characters)	Yes
phone_number	String (32 characters)	No
date_joined	Date	Yes
Project Structure
text
devops-capstone-project/
├── service/
│   ├── common/
│   │   ├── cli_commands.py
│   │   ├── error_handlers.py
│   │   ├── log_handlers.py
│   │   └── status.py
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── factories.py
│   ├── test_cli_commands.py
│   ├── test_models.py
│   └── test_routes.py
├── .github/
│   └── workflows/
├── requirements.txt
├── setup.cfg
├── Makefile
└── README.md

Development Environment Setup

This project was created from the IBM Skills Network DevOps Capstone template.

1. Set up the environment

In the IBM Skills Network Cloud IDE, run:

bash
source bin/setup.sh


This initializes the Python environment and activates the virtual environment.

2. Install dependencies
bash
make install

3. Start PostgreSQL
bash
make db


Verify that the PostgreSQL container is running:

bash
docker ps

4. Run the tests

With the required dependencies and database configured, execute:

bash
nosetests -v --with-spec --spec-color --with-coverage --cover-package=service


Run the critical Flake8 checks with:

bash
flake8 service --count --select=E9,F63,F7,F82 --show-source --statistics

Testing and Code Coverage

Automated tests validate account model operations, API routes, error handling, health checks, CORS policies, and security headers.

The latest recorded GitHub Actions build completed successfully:

Test results: 27 tests passed.
Code coverage: 91%.
Critical Flake8 errors: 0.
Build status: Successful.

The project target is at least 95% code coverage. Additional tests are needed to reach this target.

Continuous Integration

GitHub Actions automates dependency installation, code checks, and testing. The build status badge at the top of this README links to the workflow status for this repository.

Workflow badge URL:

text
https://github.com/Ali9858/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg


Make sure ci-build.yaml matches the actual workflow filename in .github/workflows/.

Docker and Kubernetes

The project supports local container and Kubernetes development.

The following Makefile commands are available in the supported local development environment:

bash
make cluster
make tekton
make clustertasks


These commands create a local K3D Kubernetes cluster, install Tekton, and install the required ClusterTasks.

Note: Local Kubernetes development requires Docker Desktop and the configured development environment. These commands are intended for standalone local development, not necessarily for the IBM Cloud IDE.

Security

The project incorporates security-related practices, including:

CORS configuration.
HTTP security headers.
Input and request validation.
Appropriate API error handling.
Database-backed account persistence.

Production deployments should also use secure database credentials, environment-based configuration, and appropriate authentication and authorization controls.

License

This project uses the Apache License. See the LICENSE file for details.

Author and Attribution

Based on the IBM Skills Network DevOps Capstone Project template, part of the IBM DevOps and Software Engineering Professional Certificate.

Original project author: John Rofrano, IBM Research.

Repository: Ali9858/devops-capstone-project

README: View README.md
