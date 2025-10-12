# FastAPI Microservices (User + Order) with PostgreSQL

## What this contains
- Two microservices (user-service, order-service) built with FastAPI
- PostgreSQL database
- Local dev with `docker-compose`
- Kubernetes manifests to deploy to a cluster

## Run locally (docker-compose)
1. Edit `.env` if needed (network, ports). Default Postgres password is `postgrespw` in compose file.
2. Start:
   ```bash
   docker-compose up --build
   ```
3. APIs:
   - User service: `http://localhost:8001/docs`
   - Order service: `http://localhost:8002/docs`

## Build & push images
Edit `scripts/build-and-push.sh` with your registry and run:
```bash
scripts/build-and-push.sh
```

## Deploy to Kubernetes
1. Edit `k8s/secrets.yaml` with your base64-encoded values or use `kubectl create secret generic`.
2. Apply manifests:
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secrets.yaml -n microservices
kubectl apply -f k8s/configmap.yaml -n microservices
kubectl apply -f k8s/postgres-pvc.yaml -n microservices
kubectl apply -f k8s/postgres-deployment.yaml -n microservices
kubectl apply -f k8s/postgres-service.yaml -n microservices
kubectl apply -f k8s/user-deployment.yaml -n microservices
kubectl apply -f k8s/user-service.yaml -n microservices
kubectl apply -f k8s/order-deployment.yaml -n microservices
kubectl apply -f k8s/order-service.yaml -n microservices
```

## Notes
- Replace image names with your registry.
- For production, use managed Postgres and configure secrets accordingly.
