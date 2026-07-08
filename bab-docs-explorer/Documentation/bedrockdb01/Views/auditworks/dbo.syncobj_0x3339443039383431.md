# dbo.syncobj_0x3339443039383431

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3339443039383431"]
    dbo_ORG_CHN_LOC_LANG(["dbo.ORG_CHN_LOC_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3339443039383431]as select  [LOC_ID],[LANG_ID],[LOC_DESC]  from  [dbo].[ORG_CHN_LOC_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_LANG]', 'OBJECT', 'SELECT')= 1
```

