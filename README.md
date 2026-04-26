# 🚀 Smart Task Manager – DevOps + Full Stack Project
AWS architecture of this project
<img width="5172" height="2768" alt="image" src="https://github.com/user-attachments/assets/74741fe3-e44c-4c80-b1a3-f4d1b61a8b37" />


## 📌 Project Overview

A full-stack task management application built with Flask and React, deployed using Docker, automated CI/CD pipelines, and Infrastructure as Code using Terraform.

## 🛠️ Tech Stack

### Backend

* Python (Flask)
* MySQL
* JWT Authentication

### Frontend

* React (Vite)

### DevOps

* Docker & Docker Compose
* GitHub Actions (CI/CD)
* Terraform (Infrastructure as Code)


## ☁️ Cloud & DevOps Features

* Containerized application using Docker
* CI/CD pipeline using GitHub Actions
* Infrastructure provisioning using Terraform
* Environment-based configuration
* Scalable architecture (can be deployed to AWS ECS/EKS)


## 📂 Project Structure

TaskManager/
│── backend/
│── frontend/
│── terraform/
│── .github/workflows/
│── docker-compose.yml


## ⚙️ How to Run Locally

### Step 1: Clone Repo

git clone https://github.com/sriram-768/devops_project_1.git

### Step 2: Run with Docker

docker-compose up --build


## 🔐 Features

* User Authentication (JWT)
* Task CRUD Operations
* Secure API
* RESTful architecture


## 📦 Future Improvements

* Deploy to AWS (ECS/EKS)
* Add monitoring (Prometheus + Grafana)
* Add logging system


## ☁️ AWS Deployment Architecture

This project is designed to be deployed on AWS using scalable and production-ready services.

### 🏗️ Architecture Overview

* **Frontend (React App)**
  Deployed on **Amazon S3** as static files and served globally using **CloudFront CDN**

* **Backend (Flask API)**
  Containerized using Docker and deployed on:

  * **Amazon ECS (Fargate)** OR
  * **Amazon EKS (Kubernetes)**

* **Database (MySQL)**
  Managed using **Amazon RDS** for high availability and automated backups

* **Container Registry**
  Docker images stored in **Amazon ECR**

* **CI/CD Pipeline**
  Implemented using **GitHub Actions**:

  * Build Docker images
  * Push to ECR
  * Deploy to ECS/EKS

* **Infrastructure as Code**
  Managed using **Terraform**:

  * Provision EC2/ECS/EKS
  * Setup networking (VPC, Subnets)
  * Configure RDS

### 🔐 Security Best Practices

* IAM Roles and Policies for secure access
* Environment variables for sensitive data
* Restricted network access using Security Groups
* HTTPS enabled via CloudFront
  
### ⚙️ Scalability & Reliability

* Auto-scaling enabled for backend containers
* Load balancing using AWS ALB
* Distributed frontend via CDN
* Managed database with failover support

### 📊 AWS Services Used

* Amazon EC2 / ECS / EKS
* Amazon S3
* Amazon CloudFront
* Amazon RDS
* Amazon ECR
* IAM (Identity & Access Management)
