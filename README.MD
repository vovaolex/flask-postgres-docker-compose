# Docker Project 2 — Flask + PostgreSQL + Docker Compose

A multi-container application using Flask, PostgreSQL and Docker Compose.

## Features

- Flask REST API
- PostgreSQL database
- Docker Compose
- Multi-container architecture
- Persistent database storage
- Environment variables
- PostgreSQL healthcheck
- Service dependency management

## Architecture

Client
↓
Flask container
↓
Docker network
↓
PostgreSQL container
↓
Docker volume

## Endpoints

### GET /health
Checks application status.

### GET /tasks
Returns all tasks.

### POST /tasks
Creates a new task.

Example:

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Docker Compose"}'