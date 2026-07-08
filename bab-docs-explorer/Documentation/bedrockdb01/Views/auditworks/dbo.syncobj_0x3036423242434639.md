# dbo.syncobj_0x3036423242434639

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3036423242434639"]
    dbo_ORG_CHN_PSTN_ACTVTY_A(["dbo.ORG_CHN_PSTN_ACTVTY_A"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_PSTN_ACTVTY_A |

## View Code

```sql
create view [dbo].[syncobj_0x3036423242434639]as select  [PSTN_CODE],[ACTVTY_CODE]  from  [dbo].[ORG_CHN_PSTN_ACTVTY_A]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_PSTN_ACTVTY_A]', 'OBJECT', 'SELECT')= 1
```

