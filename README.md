# SOAP Integration Demo
A Python integration service that pulls data from a SOAP API on a schedule, 
validates and loads it into PostgreSQL, and serves it through REST and GraphQL 
endpoints built with FastAPI and Strawberry.

## Architecture
```
    SOAP Source             Client
    |^                      |^
    v|                      v|
    SOAP sync job           API(REST/GraphQL)
    |                       |^
    v                       v|
    Ingest Service          Query Service
    |                       |^                        
    v                       v|
+-------------------------------+      
|       Shared Repository       |
+-------------------------------+      
                |^
                v|
        Database (PostgreSQL)
```

**Key design choices**
- SOAP sync job runs separate from the APIs to ensure that the pull can be
    scheduled separately and running one doesn't depend on the other.
- Ingest service validates data, records success or failure from each pull, and
    loads data into the database via the repository layer.
- Query service loads data from the database and never the SOAP API directly.
    This ensures data remains available even if the SOAP Source is down.

## Quick Start
TODO