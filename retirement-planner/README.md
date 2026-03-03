# 📘 README.md

# Retirement Planning Engine (Serverless AWS Version)

## Overview

This project converts a deterministic Excel-based retirement calculator into a cloud-native, serverless web application.

---

## Architecture

S3 → CloudFront → API Gateway → Lambda → DynamoDB

---

## Why Serverless?

To eliminate:

* NAT Gateway cost
* ALB cost
* RDS fixed cost
* Idle compute cost

This ensures:

* Near-zero monthly expense
* Automatic scaling
* Simpler networking
* Faster deployment

---

## Infrastructure as Code

Provisioned entirely via Terraform.

---

## CI/CD

GitHub Actions:

* Lint
* Test
* Build
* Deploy

---

## Financial Engine

Implements:

* Growing annuity retirement corpus
* SIP and step-up SIP calculation
* Inflation-adjusted projections
* Deterministic outputs

---

## Cost Summary

Estimated monthly cost under light load: ₹500–₹800.