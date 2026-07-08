# dbo.syncobj_0x3943463041373735

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3943463041373735"]
    dbo_ORG_CHN_HRCHY_LVL_LANG(["dbo.ORG_CHN_HRCHY_LVL_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_HRCHY_LVL_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3943463041373735]as select  [HRCHY_LVL_ID],[LANG_ID],[HRCHY_LVL_DESC]  from  [dbo].[ORG_CHN_HRCHY_LVL_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_HRCHY_LVL_LANG]', 'OBJECT', 'SELECT')= 1
```

