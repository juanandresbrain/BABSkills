# dbo.syncobj_0x3632453230363339

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3632453230363339"]
    dbo_ORG_CHN_PSTN_LANG(["dbo.ORG_CHN_PSTN_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_PSTN_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3632453230363339]as select  [PSTN_CODE],[LANG_ID],[PSTN_DESC],[PSTN_SHRT_DESC]  from  [dbo].[ORG_CHN_PSTN_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_PSTN_LANG]', 'OBJECT', 'SELECT')= 1
```

