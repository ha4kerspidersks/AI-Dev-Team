# DevOps MCP Layer

## Guidelines
- Covers Infrastructure-as-Code (Terraform), container orchestration (Kubernetes), and CI/CD pipelines (GitHub Actions).
- Destruction Prevention: `terraform destroy`, `kubectl delete namespace`, and production deployment triggers must always be classified as DESTRUCTIVE or EXTERNAL ACTION requiring confirmation.
