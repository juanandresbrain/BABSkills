# dbo.syncobj_0x3036353732373739

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3036353732373739"]
    dbo_ORG_CHN_OPRT_HOUR_HSTRY(["dbo.ORG_CHN_OPRT_HOUR_HSTRY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_OPRT_HOUR_HSTRY |

## View Code

```sql
create view [dbo].[syncobj_0x3036353732373739]as select  [ORG_CHN_NUM],[EFCTV_DATE],[EXPRTN_DATE],[HOUR_ID],[FDN_CSTMZTN_DATA]  from  [dbo].[ORG_CHN_OPRT_HOUR_HSTRY]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_OPRT_HOUR_HSTRY]', 'OBJECT', 'SELECT')= 1
```

