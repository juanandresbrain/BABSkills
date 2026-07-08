# dbo.syncobj_0x3244343146343134

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3244343146343134"]
    dbo_ORG_CHN_OPEN_HOUR_EXCPTN(["dbo.ORG_CHN_OPEN_HOUR_EXCPTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_OPEN_HOUR_EXCPTN |

## View Code

```sql
create view [dbo].[syncobj_0x3244343146343134]as select  [ORG_CHN_NUM],[EXCPTN_DATE],[START_TIME],[END_TIME],[CLSD],[RSN_ID],[FDN_CSTMZTN_DATA]  from  [dbo].[ORG_CHN_OPEN_HOUR_EXCPTN]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_OPEN_HOUR_EXCPTN]', 'OBJECT', 'SELECT')= 1
```

