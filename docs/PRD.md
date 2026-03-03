# 📘 docs/PRD.md

# Product Requirements Document

## Project: Serverless Retirement Planning Engine

## Purpose: DevOps Mid-Level Interview Demonstration

---

## 1. Product Vision

Build a deterministic retirement planning engine converted from Excel into a cloud-native, serverless web application deployed on AWS with:

* Zero always-on infrastructure
* Minimal monthly cost
* Infrastructure as Code
* CI/CD automation
* Secure design
* Deterministic financial engine

---

## 2. Target Outcome

Demonstrate:

* Cloud architecture design
* Cost optimization thinking
* Serverless compute
* API design
* Infrastructure automation
* Observability
* Security best practices

---

## 3. Architecture Overview

Frontend:

* S3 static hosting
* CloudFront CDN

Backend:

* FastAPI
* AWS Lambda (via Mangum)

API Layer:

* API Gateway (HTTP API)

Database:

* DynamoDB (on-demand billing)

IaC:

* Terraform

CI/CD:

* GitHub Actions

---

## 4. Functional Requirements

### User Management

* Create user
* Authenticate user (JWT)

### Client Management

* Create client profile
* Store retirement assumptions

### Financial Engine

* Calculate:

  * Inflated expense
  * Corpus required
  * Future value of assets
  * Deficit
  * Fixed SIP
  * Step-up SIP

### Projection Graph

* Wealth growth curve
* Retirement depletion curve

---

## 5. Non-Functional Requirements

* Stateless backend
* Cold start under 1.5 seconds
* Response time < 1 second
* Infrastructure cost < ₹1000/month under light load
* Deterministic calculations
* Secure secrets handling

---

## 6. Constraints

* No NAT Gateway
* No ALB
* No RDS
* No always-on compute

---

## 7. Acceptance Criteria

* All APIs return correct financial outputs
* Infrastructure deployable via single Terraform command
* CI/CD pipeline builds and deploys automatically
* Cost analysis documented