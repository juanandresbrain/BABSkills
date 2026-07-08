# dbo.syncobj_0x3630374246444346

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3630374246444346"]
    dbo_ORG_CHN_LOC_HRCHY_LANG(["dbo.ORG_CHN_LOC_HRCHY_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_HRCHY_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3630374246444346]as select  [HRCHY_ID],[LANG_ID],[HRCHY_DESC]  from  [dbo].[ORG_CHN_LOC_HRCHY_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_HRCHY_LANG]', 'OBJECT', 'SELECT')= 1
```

