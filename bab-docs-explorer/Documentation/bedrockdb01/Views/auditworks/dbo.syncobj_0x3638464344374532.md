# dbo.syncobj_0x3638464344374532

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3638464344374532"]
    dbo_ORG_CHN_LOC_FNCTN(["dbo.ORG_CHN_LOC_FNCTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_FNCTN |

## View Code

```sql
create view [dbo].[syncobj_0x3638464344374532]as select  [FNCTN_NUM],[FNCTN_DESC],[FNCTN_SHRT_DESC],[SYS_CODE],[ACTV]  from  [dbo].[ORG_CHN_LOC_FNCTN]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_FNCTN]', 'OBJECT', 'SELECT')= 1
```

