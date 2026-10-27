DevOps Capstone Project
[![Build Status](https://github.com/Ali9858/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Ali9858/devops-capstone-project/actions/workflows/ci-build.yaml)

30 Days DevOps Challenge - NBA Data Lake
Day 3: Building a building a Sports Data Lake leveraging Azure blob storage, and Synapse Analytics

Project Structure

Project Overview
This project demonstrates how to build a data pipeline for NBA sports analytics using Azure services. The pipeline fetches NBA player data from an API, stores it in Azure Blob Storage, and creates a queryable table in Azure Synapse Analytics. The data can then be queried and processed using any tool.

Features
Data Ingestion: Fetch NBA player data from the sportsdata.io API.
Data Storage: Store raw JSON data in Azure Blob Storage.
Schema Transformation: Transform JSON data to Parquet using Synapse pipeline
Table Creation: Create a table in Azure Synapse Analytics with parquet schema.
Data Querying: Query the table using SQL.
Prerequisites
Python 3.x
Azure Account: An active Azure subscription.
Azure Blob Storage: To store raw JSON data.
Azure Synapse Analytics: To create and query tables.
SportsData API key
Dependencies
azure-storage-blob
azure-synapse-spark
requests
python-dotenv
pyodbc
Project Structure
03_NBADataLake/
├── azure_resources.py
├── data_operations.py
├── setup_data_lake.py
├── .gitignore
├── .env
├── requirements.txt
└── README.md
Running the application
Clone the repository
git clone git@github.com:Jekwulum/03_NBADataLake.git
cd 03_NBADataLake
Create a virtual environment:
python -m venv .venv
source .venv/Scripts/activate  # On Windows use `.venv\Scripts\activate`
Install the dependencies:
pip install -r requirements.txt
Configure environment variables (.env):
# Azure configurations
AZURE_SUBSCRIPTION_ID=your_subscription_id
AZURE_RESOURCE_GROUP=your_resource_group_name
AZURE_STORAGE_ACCOUNT=your_storage_account
AZURE_CONNECTION_STRING=your_connection_string # will be dynamucally filled

SQL_ADMIN_LOGIN=your_sql_admin_login
SQL_ADMIN_PASSWORD=your_sql_admin_password
SQL_DATABASE=nba_analytics
SYNAPSE_WORKSPACE_NAME=your-workspace-name
SYNAPSE_SQL_ENDPOINT=your_workspace_name.sql.azuresynapse.net # will be dynamucally filled

# Sportsdata.io configurations
SPORTS_DATA_API_KEY=your_api_key
NBA_ENDPOINT=your_nba_endpoint
Run the application:
python setup_nba_data_lake.py
What I learned
Azure Blob storage container creation and management
Environment variable management for secure API keys
Python best practices for API integration
Transforming JSON to Parquet
Git workflow for project development
Effective Error handling
Cloud resource management
Future Enhancements
Add weather forecasting
Implement data visualization
Add more cities
Create automated testing
Set up CI/CD pipeline
Workflow
Data Ingestion Fetch NBA player data from the sportsdata.io API.
The data is returned in JSON format.

Data Storage
Upload the JSON data to Azure Blob Storage.

Data Transformation
Transform the JSON data to Parquet format for efficient querying using Synapse pipeline.

Schema Inference
Create a table in Azure Synapse Analytics with an inferred schema.

Data Querying
Query the table using SQL.

This project is part of the IBM DevOps and Software Engineering Professional Certificate. It implements a RESTful Flask microservice for managing customer accounts in an e-commerce application.

Project Overview

The DevOps Capstone Project demonstrates Agile planning, Test-Driven Development (TDD), automated testing, code coverage, continuous integration, Docker containerization, and Kubernetes deployment.

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
