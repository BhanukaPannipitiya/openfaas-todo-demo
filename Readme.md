# 🩺 OpenFaaS TODO API — Serverless on Kubernetes

This project demonstrates a **serverless architecture** built on **Kubernetes** using **OpenFaaS**, developed as part of my practical learning after completing the [Introduction to Kubernetes (LFS158x)](https://training.linuxfoundation.org/training/introduction-to-kubernetes/) course by The Linux Foundation.

## 🚀 Project Overview
A simple TODO API implemented with two OpenFaaS functions:
- `add-todo`: Adds a new todo item
- `get-todos`: Retrieves the list of todos

Each function runs as an independent, containerized, and serverless workload managed by OpenFaaS on Kubernetes.

## 🧱 Architecture
- **Kind (Kubernetes-in-Docker)** for local cluster setup  
- **OpenFaaS** for serverless function management  
- **GitHub Container Registry (GHCR)** for hosting function images  
- **FaaS CLI** for build, deploy, and invoke operations  

```plaintext
Client → OpenFaaS Gateway → Function Pods (add-todo, get-todos)
