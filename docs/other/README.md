# Prima Senior SRE Tech Challenge 2026

Production-ready solution for the **Senior Site Reliability Engineer** position at Prima.

## Project Overview

This project implements a reliable Python REST API with the following features:

- **FastAPI** backend supporting user creation with avatar image upload
- Image storage in **AWS S3**
- User metadata persistence in **AWS DynamoDB**
- Containerized with **Docker** (using modern `uv` dependency manager)
- Infrastructure provisioned with **Terraform** on real AWS
- Kubernetes deployment ready via **Helm Chart**
- Automated **GitHub Actions** CI/CD pipeline

## Architecture

```
Client → FastAPI (Docker) → AWS S3 (avatars) + DynamoDB (users)
↓
Kubernetes (via Helm)
```

Key reliability features:

- Horizontal Pod Autoscaler (CPU-based)
- Liveness & Readiness probes
- Resource requests & limits
- Least-privilege IAM role (prepared for IRSA)
- Proper error handling for AWS services

## Quick Start (Local)

```bash
# Start the application
docker compose up -d --build

# Test endpoints
curl http://localhost:8000/health

curl http://localhost:8000/users

# Create a user with avatar
curl -X POST http://localhost:8000/user \
  -F "name=Test User" \
  -F "email=test-user@prima.it" \
  -F "avatar=@/path/to/your/image.png"
```

## Infrastructure (Terraform)

```bash
cd terraform
terraform init
terraform apply -auto-approve
```

Provisions:

- S3 bucket for avatars
- DynamoDB table (`users`)
- IAM role + policy (ready for Kubernetes ServiceAccount)

## Kubernetes Deployment (Helm)

```bash
helm template ./helm
# For actual deployment:
# helm install prima-users-api ./helm
```

Features:

- Horizontal Pod Autoscaler (min 2, max 10 replicas, 60% CPU target)
- Liveness & Readiness probes on `/health`
- Resource limits and requests
- ServiceAccount with IAM role annotation

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/cicd.yml`) performs:

- Docker image build
- Helm chart linting and validation
- Trivy security scan

## Project Structure

```
.
├── app/                    # FastAPI application + pyproject.toml + Dockerfile
├── terraform/              # Infrastructure as Code (S3, DynamoDB, IAM)
├── helm/                   # Kubernetes Helm chart
├── .github/workflows/      # GitHub Actions CI/CD
├── docker-compose.yml
├── .env.example
└── README.md
```

## Technologies

- **Backend**: FastAPI, boto3, Pydantic
- **Container**: Docker + uv
- **IaC**: Terraform
- **Orchestration**: Helm + Kubernetes
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (S3 + DynamoDB)

## Reliability Considerations

- Health checks implemented
- Autoscaling via HPA
- Graceful error handling for AWS services
- Resource constraints to prevent pod eviction
- Security scanning in CI/CD

**Note**: The IAM role is prepared for EKS IRSA. In a full production setup, an OIDC provider would be configured.

## Submission

- All code is my own work.
- Solution runs on Ubuntu Linux.
- Uses real AWS account (Free Tier).
- Repository is private.
