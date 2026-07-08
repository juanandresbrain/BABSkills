# dbo.syncobj_0x3045343836414633

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3045343836414633"]
    dbo_EMPLY_HRCHY_LVL_LANG(["dbo.EMPLY_HRCHY_LVL_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLY_HRCHY_LVL_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3045343836414633]as select  [HRCHY_LVL_ID],[LANG_ID],[HRCHY_LVL_DESC]  from  [dbo].[EMPLY_HRCHY_LVL_LANG]  where HAS_PERMS_BY_NAME('[dbo].[EMPLY_HRCHY_LVL_LANG]', 'OBJECT', 'SELECT')= 1
```

