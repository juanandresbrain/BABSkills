# dbo.spLogRemoveOldEntries

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spLogRemoveOldEntries"]
    dbo_pollingdebug(["dbo.pollingdebug"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.pollingdebug |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spLogRemoveOldEntries] AS

delete from mamamart.babw.dbo.pollingdebug
where datestamp < dateadd(mm,-1, getdate())
```

