# dbo.syncobj_0x3433323030303436

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3433323030303436"]
    dbo_CORE_HOUR_LANG(["dbo.CORE_HOUR_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CORE_HOUR_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3433323030303436]as select  [HOUR_ID],[LANG_ID],[HOUR_DESC],[HOUR_SHRT_DESC]  from  [dbo].[CORE_HOUR_LANG]  where HAS_PERMS_BY_NAME('[dbo].[CORE_HOUR_LANG]', 'OBJECT', 'SELECT')= 1
```

