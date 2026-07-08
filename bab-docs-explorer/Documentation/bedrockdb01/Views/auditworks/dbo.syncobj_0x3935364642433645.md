# dbo.syncobj_0x3935364642433645

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3935364642433645"]
    dbo_ATRBT_LANG(["dbo.ATRBT_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ATRBT_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3935364642433645]as select  [ATRBT_CODE],[LANG_ID],[ATRBT_DESC],[ATRBT_TYPE]  from  [dbo].[ATRBT_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ATRBT_LANG]', 'OBJECT', 'SELECT')= 1
```

