# dbo.dw_transaction_range

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_transaction_range"]
    dbo_transaction_range(["dbo.transaction_range"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_range |

## View Code

```sql
CREATE VIEW dbo.dw_transaction_range AS
SELECT store_no,
       register_no,
       transaction_date,
       date_reject_id,
       transaction_series,
       first_transaction_no,
       last_transaction_no FROM auditworks_external.dbo.transaction_range
```

