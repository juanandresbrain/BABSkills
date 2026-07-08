# dbo.group_user

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.group_user"]
    dbo_FNDTN_SCRTY_GRP_USER(["dbo.FNDTN_SCRTY_GRP_USER"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_GRP_USER |

## View Code

```sql
CREATE VIEW dbo.group_user (group_id,user_id,primary_group)
AS SELECT GRP_ID,USER_ID,PRMRY_GRP
FROM dbo.FNDTN_SCRTY_GRP_USER
```

