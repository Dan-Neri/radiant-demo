# SOAP Integration Demo
A Python integration service that uses zeep to pull weather data from the
National Digital Forecast Database (NDFD) on a schedule, validates and loads it
into a local PostgreSQL database, and serves it through REST and GraphQL
endpoints built with FastAPI and Strawberry.

## Architecture
```
                   
            Scheduled data pull job       Client                 
                        |^                  |^
                        ||                  v|
+-----------+           ||          REST / GraphQL API
|           |           v|                  |^
|   NDFD    | <--> SOAP client              ||
|           |           |^                  ||
+-----------+           ||                  ||
                        v|                  v|
                    Ingest Service      Query Service
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
- The data pull job runs separately from the APIs, so it can be scheduled on
    its own and neither side depends on the other being up.
- The ingest service validates data, records success or failure from each pull, and
    loads data into the database via the repository layer.
- The repository layer relies only on a database session, not on FastAPI
    context (`Depends`), so both processes can use the same repository code
    and run independently.
- The query service reads data from the database and never the SOAP API directly.
    This ensures data remains available even if the NDFD is down.
- Since data is loaded from the NDFD on a schedule, the locations to be 
    requested must be known beforehand. I chose to pull data only for state 
    capitals. Coordinates come directly from the NDFD LatLonListCityNames()
    SOAP function. For the seven capitals without a matching entry (Annapolis,
    Carson City, Concord, Frankfort, Jefferson City, Raleigh, and Saint Paul),
    I used coordinates from geonames.org. The NDFD lists Raleigh only as
    Raleigh-Durham, which is a combined entry.

## Quick Start
TODO