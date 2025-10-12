#!/usr/bin/env bash
set -e

REGISTRY=${1:-yourrepo}

# build user
docker build -t ${REGISTRY}/user-service:latest ./user-service
# build order
docker build -t ${REGISTRY}/order-service:latest ./order-service

# push
docker push ${REGISTRY}/user-service:latest
docker push ${REGISTRY}/order-service:latest

echo "Images pushed to ${REGISTRY}"
