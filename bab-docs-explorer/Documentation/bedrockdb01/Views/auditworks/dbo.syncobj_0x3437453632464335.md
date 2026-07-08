# dbo.syncobj_0x3437453632464335

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3437453632464335"]
    dbo_ORG_CHN_ACTVTY_LANG(["dbo.ORG_CHN_ACTVTY_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_ACTVTY_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3437453632464335]as select  [ACTVTY_CODE],[LANG_ID],[ACTVTY_DESC],[ACTVTY_SHRT_DESC]  from  [dbo].[ORG_CHN_ACTVTY_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_ACTVTY_LANG]', 'OBJECT', 'SELECT')= 1
```

