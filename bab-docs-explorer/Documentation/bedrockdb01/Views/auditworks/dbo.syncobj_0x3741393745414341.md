# dbo.syncobj_0x3741393745414341

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3741393745414341"]
    dbo_CLNDR_LVL_ASCTN(["dbo.CLNDR_LVL_ASCTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_LVL_ASCTN |

## View Code

```sql
create view [dbo].[syncobj_0x3741393745414341]as select  [CLNDR_ID],[PRNT_CLNDR_LVL_TYPE_ID],[CHLD_CLNDR_LVL_TYPE_ID]  from  [dbo].[CLNDR_LVL_ASCTN]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_LVL_ASCTN]', 'OBJECT', 'SELECT')= 1
```

