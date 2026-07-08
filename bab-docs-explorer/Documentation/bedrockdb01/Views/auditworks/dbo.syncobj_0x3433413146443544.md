# dbo.syncobj_0x3433413146443544

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3433413146443544"]
    dbo_ATRBT_ENTY_TYPE_LANG(["dbo.ATRBT_ENTY_TYPE_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ATRBT_ENTY_TYPE_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3433413146443544]as select  [ATRBT_TYPE],[LANG_ID],[ATRBT_TYPE_DESC]  from  [dbo].[ATRBT_ENTY_TYPE_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ATRBT_ENTY_TYPE_LANG]', 'OBJECT', 'SELECT')= 1
```

