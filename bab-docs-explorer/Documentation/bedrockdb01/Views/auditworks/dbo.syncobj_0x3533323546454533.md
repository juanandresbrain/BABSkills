# dbo.syncobj_0x3533323546454533

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3533323546454533"]
    dbo_ORG_CHN_LOC_HRCHY_LVL_GRP_LANG(["dbo.ORG_CHN_LOC_HRCHY_LVL_GRP_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_HRCHY_LVL_GRP_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3533323546454533]as select  [HRCHY_LVL_GRP_ID],[LANG_ID],[HRCHY_LVL_GRP_DESC]  from  [dbo].[ORG_CHN_LOC_HRCHY_LVL_GRP_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_HRCHY_LVL_GRP_LANG]', 'OBJECT', 'SELECT')= 1
```

