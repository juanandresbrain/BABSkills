# dbo.sysmail_faileditems

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysmail_faileditems"]
    dbo_sysmail_allitems(["dbo.sysmail_allitems"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysmail_allitems |

## View Code

```sql
CREATE VIEW sysmail_faileditems
AS
SELECT * FROM msdb.dbo.sysmail_allitems WHERE sent_status = 'failed'
```

