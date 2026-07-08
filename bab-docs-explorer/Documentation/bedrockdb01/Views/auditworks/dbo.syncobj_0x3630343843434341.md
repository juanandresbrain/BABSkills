# dbo.syncobj_0x3630343843434341

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3630343843434341"]
    dbo_EMPLY_HRCHY_LANG(["dbo.EMPLY_HRCHY_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLY_HRCHY_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3630343843434341]as select  [HRCHY_ID],[LANG_ID],[HRCHY_DESC]  from  [dbo].[EMPLY_HRCHY_LANG]  where HAS_PERMS_BY_NAME('[dbo].[EMPLY_HRCHY_LANG]', 'OBJECT', 'SELECT')= 1
```

