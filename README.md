# ct-log
# CT Log Collection System

## Overview
This project collects Certificate Transparency (CT) logs in real-time for phishing detection research.

## Method
CT logs are collected using a local Certstream server.

1. A Certstream server is deployed using Docker Desktop.
2. The server streams CT log data via WebSocket.
3. A Python client connects to the server and continuously receives CT log events.
4. The collected logs are processed and stored for further analysis.

## Environment
- Docker Desktop
- Python 3.11
- MongoDB (optional for storage)

## Usage
Run the Certstream server:
```bash
docker run -p 4000:4000 certstream-server
