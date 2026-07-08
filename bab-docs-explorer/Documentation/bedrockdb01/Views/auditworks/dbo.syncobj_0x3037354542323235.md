# dbo.syncobj_0x3037354542323235

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3037354542323235"]
    dbo_ORG_CHN_STR_SAFE_LANG(["dbo.ORG_CHN_STR_SAFE_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_STR_SAFE_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3037354542323235]as select  [SAFE_ID],[LANG_ID],[SAFE_DESC],[SAFE_SHRT_DESC]  from  [dbo].[ORG_CHN_STR_SAFE_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_STR_SAFE_LANG]', 'OBJECT', 'SELECT')= 1
```

