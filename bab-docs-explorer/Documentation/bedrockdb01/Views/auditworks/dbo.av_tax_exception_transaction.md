# dbo.av_tax_exception_transaction

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.av_tax_exception_transaction"]
    dbo_tax_exception_transaction(["dbo.tax_exception_transaction"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tax_exception_transaction |

## View Code

```sql
CREATE view  dbo.av_tax_exception_transaction AS 
SELECT * /* dummy version of view */
  FROM dbo.tax_exception_transaction
```

