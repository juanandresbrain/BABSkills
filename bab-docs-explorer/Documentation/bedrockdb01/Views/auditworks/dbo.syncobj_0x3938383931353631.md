# dbo.syncobj_0x3938383931353631

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3938383931353631"]
    dbo_GEOG_TRTRY(["dbo.GEOG_TRTRY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GEOG_TRTRY |

## View Code

```sql
create view [dbo].[syncobj_0x3938383931353631]as select  [TRTRY_CODE],[CNTRY_CODE_ISO3],[TRTRY_DESC],[TRTRY_SHRT_DESC]  from  [dbo].[GEOG_TRTRY]  where HAS_PERMS_BY_NAME('[dbo].[GEOG_TRTRY]', 'OBJECT', 'SELECT')= 1
```

