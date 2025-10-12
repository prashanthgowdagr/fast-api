#!/usr/bin/env bash
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
