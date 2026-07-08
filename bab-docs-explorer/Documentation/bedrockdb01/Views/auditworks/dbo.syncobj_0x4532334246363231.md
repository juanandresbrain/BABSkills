# dbo.syncobj_0x4532334246363231

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4532334246363231"]
    dbo_EMPLY_HRCHY_LVL_GRP_LANG(["dbo.EMPLY_HRCHY_LVL_GRP_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLY_HRCHY_LVL_GRP_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4532334246363231]as select  [HRCHY_LVL_GRP_ID],[LANG_ID],[HRCHY_LVL_GRP_DESC]  from  [dbo].[EMPLY_HRCHY_LVL_GRP_LANG]  where HAS_PERMS_BY_NAME('[dbo].[EMPLY_HRCHY_LVL_GRP_LANG]', 'OBJECT', 'SELECT')= 1
```

