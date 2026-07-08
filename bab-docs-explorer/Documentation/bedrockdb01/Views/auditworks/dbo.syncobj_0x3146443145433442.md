# dbo.syncobj_0x3146443145433442

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3146443145433442"]
    dbo_ATRBT_VAL_LANG(["dbo.ATRBT_VAL_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ATRBT_VAL_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3146443145433442]as select  [ATRBT_CODE],[ATRBT_VAL_CODE],[LANG_ID],[ATRBT_VAL_DESC],[ATRBT_TYPE]  from  [dbo].[ATRBT_VAL_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ATRBT_VAL_LANG]', 'OBJECT', 'SELECT')= 1
```

