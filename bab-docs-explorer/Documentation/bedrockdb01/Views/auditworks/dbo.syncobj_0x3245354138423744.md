# dbo.syncobj_0x3245354138423744

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3245354138423744"]
    dbo_ORG_CHN_LOC_FNCTN_A(["dbo.ORG_CHN_LOC_FNCTN_A"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_FNCTN_A |

## View Code

```sql
create view [dbo].[syncobj_0x3245354138423744]as select  [LOC_ID],[FNCTN_NUM],[PRMRY_LOC_FNCTN_A],[FDN_CSTMZTN_DATA]  from  [dbo].[ORG_CHN_LOC_FNCTN_A]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_FNCTN_A]', 'OBJECT', 'SELECT')= 1
```

