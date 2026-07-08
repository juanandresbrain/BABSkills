# dbo.DW_CHNG_RSPNS_QUEUE

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.DW_CHNG_RSPNS_QUEUE"]
    CHNG_RSPNS_QUEUE(["CHNG_RSPNS_QUEUE"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| CHNG_RSPNS_QUEUE |

## View Code

```sql
create view dbo.DW_CHNG_RSPNS_QUEUE AS
SELECT *
 FROM CHNG_RSPNS_QUEUE
```

