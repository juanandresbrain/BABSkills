# dbo.company

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.company"]
    dbo_FNDTN_SCRTY_CMPNY(["dbo.FNDTN_SCRTY_CMPNY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_CMPNY |

## View Code

```sql
CREATE VIEW dbo.company (comp_id,comp_name,comp_description)
AS SELECT CMPNY_ID,CMPNY_NAME,CMPNY_DESC
FROM dbo.FNDTN_SCRTY_CMPNY
```

