# dbo.syncobj_0x3543464241374431

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3543464241374431"]
    dbo_PRTY_CNTCT_PREF(["dbo.PRTY_CNTCT_PREF"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PRTY_CNTCT_PREF |

## View Code

```sql
create view [dbo].[syncobj_0x3543464241374431]as select  [CNTCT_PREF_ID],[MATCH_KEY],[PREF_TYPE_GRP_ID]  from  [dbo].[PRTY_CNTCT_PREF]  where HAS_PERMS_BY_NAME('[dbo].[PRTY_CNTCT_PREF]', 'OBJECT', 'SELECT')= 1
```

