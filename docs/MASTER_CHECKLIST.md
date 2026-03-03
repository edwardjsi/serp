# 📘 docs/MASTER_CHECKLIST.md

# Master Checklist — Retirement Planning Engine

> 10-Day execution plan. Check off items daily as completed.

---

## Day 1 — Project Setup & Documentation

- [ ] Define project scope and objectives
- [ ] Write PRD (Product Requirements Document)
- [ ] Write Cost Analysis (why serverless over ALB + NAT + RDS)
- [ ] Write Architecture Decision Records (ADRs)
- [ ] Define DynamoDB single-table schema and access patterns
- [ ] Document Core Financial Engine formulas
- [ ] Initialize Git repository with folder structure
- [ ] Create README with architecture overview

---

## Day 2 — Financial Engine (Python)

- [x] Create Python project structure (`backend/`)
- [x] Implement `engine/calculator.py` with all formulas:
  - [x] Time calculations (years_to_retirement, retirement_years)
  - [x] Inflated expense calculation
  - [x] Corpus required (growing annuity model)
  - [x] Future value of existing assets
  - [x] Deficit calculation
  - [x] Fixed monthly SIP
  - [x] Step-up SIP (growing annuity)
- [x] Use `Decimal` for all monetary values
- [x] Write unit tests for every formula
- [x] Validate against known Excel outputs

---

## Day 3 — FastAPI Backend + DynamoDB Integration

- [ ] Set up FastAPI project with Mangum adapter
- [ ] Create Pydantic models for all entities:
  - [ ] UserProfile
  - [ ] Client
  - [ ] FinancialInput
  - [ ] Asset
  - [ ] Scenario
- [ ] Implement DynamoDB data access layer (`db/dynamo.py`)
  - [ ] put_item / get_item / query helpers
  - [ ] Single-table key construction (PK/SK)
- [ ] Create API routes:
  - [ ] `POST /users` — create user
  - [ ] `POST /login` — authenticate (JWT)
  - [ ] `POST /clients` — create client
  - [ ] `GET /clients` — list clients for user
  - [ ] `GET /clients/{id}` — full client detail (single query)
  - [ ] `POST /clients/{id}/assets` — add asset
  - [ ] `POST /clients/{id}/calculate` — run financial engine
- [ ] Test all routes locally with DynamoDB Local

---

## Day 4 — Authentication & Security

- [ ] Implement JWT authentication (PyJWT)
- [ ] Password hashing with bcrypt
- [ ] Create auth middleware for protected routes
- [ ] Add input validation on all endpoints
- [ ] Implement GSI for email-based login lookup
- [ ] Test auth flow end-to-end locally

---

## Day 5 — Containerization & Lambda Packaging

- [ ] Write `Dockerfile` for Lambda container image
- [ ] Configure Mangum handler as Lambda entry point
- [ ] Create `requirements.txt` with pinned dependencies
- [ ] Test Lambda container locally with `docker run`
- [ ] Create ECR repository (or use zip packaging)
- [ ] Verify cold start time < 1.5 seconds

---

## Day 6 — Terraform Infrastructure (Core)

- [ ] Set up Terraform project structure (`infra/`)
- [ ] Create `providers.tf` (AWS provider, region, backend)
- [ ] Create DynamoDB table resource (on-demand, PK/SK, GSI)
- [ ] Create Lambda function resource
- [ ] Create IAM role + policy for Lambda → DynamoDB access
- [ ] Create API Gateway HTTP API
- [ ] Create API Gateway → Lambda integration
- [ ] Create API Gateway routes and stage
- [ ] Output API endpoint URL
- [ ] `terraform plan` and `terraform apply` successfully

---

## Day 7 — Terraform Infrastructure (Frontend + CDN)

- [ ] Create S3 bucket for static frontend hosting
- [ ] Configure S3 bucket policy (CloudFront OAI access)
- [ ] Create CloudFront distribution
  - [ ] Origin: S3 bucket
  - [ ] Default root object: `index.html`
  - [ ] HTTPS redirect
- [ ] Create Origin Access Identity (OAI)
- [ ] Output CloudFront domain URL
- [ ] Deploy placeholder `index.html` to verify

---

## Day 8 — Frontend (React/HTML)

- [ ] Initialize frontend project (`frontend/`)
- [ ] Create login page
- [ ] Create client list dashboard
- [ ] Create client detail view with:
  - [ ] Financial inputs form
  - [ ] Asset management
  - [ ] Calculate button → display results
- [ ] Implement wealth projection graph (Chart.js or similar)
  - [ ] Pre-retirement growth curve
  - [ ] Post-retirement depletion curve
- [ ] Connect frontend to API Gateway endpoint
- [ ] Build and deploy to S3

---

## Day 9 — CI/CD Pipeline

- [ ] Create GitHub Actions workflow (`.github/workflows/deploy.yml`)
- [ ] Pipeline stages:
  - [ ] Lint (flake8 / ruff)
  - [ ] Unit tests (pytest)
  - [ ] Build Lambda package
  - [ ] Deploy Lambda (AWS CLI / Terraform)
  - [ ] Build frontend
  - [ ] Deploy frontend to S3
  - [ ] Invalidate CloudFront cache
- [ ] Configure GitHub secrets (AWS credentials)
- [ ] Test full pipeline on push to main
- [ ] Verify end-to-end deployment

---

## Day 10 — Polish, Testing & Documentation

- [ ] End-to-end testing (create user → create client → calculate → view graph)
- [ ] Verify all acceptance criteria from PRD
- [ ] Verify cost stays under ₹1000/month
- [ ] Update TASK_LOG.md with final entries
- [ ] Finalize README with:
  - [ ] Setup instructions
  - [ ] Architecture diagram description
  - [ ] API documentation summary
  - [ ] Cost analysis summary
- [ ] Review and finalize all ADRs
- [ ] Clean up code, remove debug logs
- [ ] Final `terraform plan` to confirm clean state
- [ ] Tag release v1.0

---

## Bonus (Post Day 10)

- [ ] Add CloudWatch alarms + dashboards
- [ ] Add X-Ray tracing for Lambda
- [ ] Add DynamoDB TTL for scenario expiry
- [ ] Add Cognito for production-grade auth
- [ ] Add custom domain with Route53 + ACM