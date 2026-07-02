# dbo.sysmail_sentitems

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysmail_sentitems"]
    dbo_sysmail_allitems(["dbo.sysmail_allitems"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysmail_allitems |

## View Code

```sql
CREATE VIEW sysmail_sentitems
AS
SELECT * FROM msdb.dbo.sysmail_allitems WHERE sent_status = 'sent'
```

