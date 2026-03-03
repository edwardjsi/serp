
# 📘 docs/ARCHITECTURE_DECISIONS.md

# Architecture Decision Record (ADR)

---

## ADR-001: Serverless vs ECS

Decision: Use Lambda instead of ECS.

Reason:

* Zero idle cost
* No ALB required
* Automatic scaling
* Simplified networking
* Cost efficient for MVP traffic

Tradeoff:

* Cold starts
* Execution timeout limit

---

## ADR-002: DynamoDB vs RDS

Decision: DynamoDB.

Reason:

* No fixed cost
* Fully managed
* Scales automatically
* No subnet complexity

Tradeoff:

* No joins
* Must design access patterns upfront

---

## ADR-003: API Gateway vs ALB

Decision: API Gateway HTTP API.

Reason:

* Integrated with Lambda
* Lower cost than ALB
* No need for VPC routing

---

## ADR-004: Terraform for IaC

Decision: Terraform over manual setup.

Reason:

* Repeatability
* Version-controlled infra
* Professional DevOps practice

---

## ADR-005: S3 + CloudFront for Frontend

Decision:
Static hosting.

Reason:

* Zero server maintenance
* Cheap
* Globally distributed