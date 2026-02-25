Pulse — Real-Time Incident Intelligence Platform
Overview

Pulse is a real-time incident intelligence system that ingests public incident data, processes and categorizes events, assigns severity scores, and delivers live geospatial updates and alerts to users.

The platform is designed as an event-driven architecture using a streaming pipeline, relational storage, caching, and a real-time frontend dashboard.

Architecture (v1)

(Add your architecture diagram here later)

Core data flow:

Data Sources → Ingestion Service → Kafka → Processing Worker → PostgreSQL → FastAPI → Next.js Dashboard (WebSocket live updates)

Tech Stack
Backend

Python

FastAPI

PostgreSQL

Redis

Kafka / Redpanda

SQLAlchemy

Pydantic

Docker

Frontend

Next.js

TypeScript

Tailwind CSS

Mapbox GL

Planned Features (v1)

Real-time ingestion of incident events

Normalization and deduplication

Category tagging

Severity scoring system

Geospatial filtering

Live WebSocket updates

Alert triggering based on thresholds

Roadmap

Week 1: Architecture + schema + setup
Week 2: Streaming ingestion
Week 3: Processing & scoring
Week 4: API endpoints
Week 5: WebSocket system
Week 6: Frontend dashboard
Week 7: Caching & performance
Week 8: Deployment & polish