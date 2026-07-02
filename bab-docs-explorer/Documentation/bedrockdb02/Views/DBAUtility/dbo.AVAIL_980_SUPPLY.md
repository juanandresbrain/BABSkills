# dbo.AVAIL_980_SUPPLY

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.AVAIL_980_SUPPLY"]
    dbo_AVAIL_980_SUPPLY(["dbo.AVAIL_980_SUPPLY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AVAIL_980_SUPPLY |

## View Code

```sql
CREATE VIEW [dbo].[AVAIL_980_SUPPLY]
AS
select * FROM [WMDB01].[WMPROD].[dbo].[AVAIL_980_SUPPLY]
```

