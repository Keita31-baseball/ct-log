# CT Log Collection System

## Overview

This repository implements a Python collector for Certificate Transparency
(CT) log events.

The collector connects to a local Certstream-compatible WebSocket server,
receives CT log events in real time, and stores certificate update data in
MongoDB. The collected data is intended for phishing detection research.

## What This Repository Contains

- `get_log.py`: WebSocket client that receives CT log events
- `requirements.txt`: Python dependencies
- MongoDB insertion logic that stores logs in daily collections

This repository does not include the Certstream server implementation itself.
The Certstream server should be prepared separately.

## System Architecture

```text
Certstream server
  ws://localhost:4000
        |
        v
Python collector
  get_log.py
        |
        v
MongoDB
  certstream_db.ctlogs_YYYY_MM_DD
```

## Environment

- Docker Desktop
- Python 3.11
- MongoDB
- Certstream-compatible WebSocket server

## Certstream Server

This collector assumes that a Certstream-compatible WebSocket server is running
locally at:

```text
ws://localhost:4000
```

In this research, the Certstream server was prepared using Docker from an
external repository. The server implementation is not included in this
repository.

If you use an external Certstream server implementation, follow the README and
license of that repository.

Example:

```bash
docker run -p 4000:4000 certstream-server
```

Note: replace `certstream-server` with the actual image name or build command
used by the Certstream server repository.

## MongoDB

Start MongoDB locally before running the collector.

The collector connects to:

```text
mongodb://localhost:27017/
```

Logs are stored in the `certstream_db` database. Each day is stored in a
separate collection:

```text
ctlogs_YYYY_MM_DD
```

## Setup

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start MongoDB.
2. Start the Certstream-compatible WebSocket server on port `4000`.
3. Run the collector:

```bash
python get_log.py
```

When a `certificate_update` event is received, the event data is inserted into
MongoDB.

## Notes

- This project focuses on the collector side, not the Certstream server side.
- The WebSocket URL and MongoDB URL are currently hard-coded in `get_log.py`.
- The collector runs continuously and reconnects after connection errors.
