# dbo.syncobj_0x4331463933423234

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4331463933423234"]
    dbo_ORG_CHN_FCLTY_CNTNR_TYPE_A(["dbo.ORG_CHN_FCLTY_CNTNR_TYPE_A"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_FCLTY_CNTNR_TYPE_A |

## View Code

```sql
create view [dbo].[syncobj_0x4331463933423234]as select  [LOC_ID],[CNTNR_TYPE_CODE]  from  [dbo].[ORG_CHN_FCLTY_CNTNR_TYPE_A]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_FCLTY_CNTNR_TYPE_A]', 'OBJECT', 'SELECT')= 1
```

