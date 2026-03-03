# 📘 docs/COST_ANALYSIS.md

# Cost Optimization Strategy

## Why Not ALB + NAT + RDS?

| Service      | Monthly Cost (approx) |
| ------------ | --------------------- |
| NAT Gateway  | ₹3000–₹4000           |
| ALB          | ₹2000–₹3000           |
| RDS Multi-AZ | ₹4000+                |
| Total        | ₹9000–₹15000          |

Not justified for low-traffic demo project.

---

## Selected Stack Cost

| Service     | Estimated Monthly      |
| ----------- | ---------------------- |
| Lambda      | Free tier / negligible |
| API Gateway | ₹200–₹400              |
| DynamoDB    | Free tier              |
| S3          | ₹100                   |
| CloudFront  | ₹100                   |
| Total       | ₹500–₹800              |

---

## Decision Rationale

Optimized for:

* Low traffic
* Minimal idle cost
* Maximum architectural demonstration
* Operational simplicity