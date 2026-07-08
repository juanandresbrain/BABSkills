# dbo.syncobj_0x3338453841354246

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3338453841354246"]
    dbo_ORG_CHN_PSTN(["dbo.ORG_CHN_PSTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_PSTN |

## View Code

```sql
create view [dbo].[syncobj_0x3338453841354246]as select  [PSTN_CODE],[PSTN_DESC],[PSTN_SHRT_DESC],[SYS_CODE],[ACTV]  from  [dbo].[ORG_CHN_PSTN]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_PSTN]', 'OBJECT', 'SELECT')= 1
```

