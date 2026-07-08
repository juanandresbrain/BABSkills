# dbo.syncobj_0x3445463042343744

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3445463042343744"]
    dbo_PRTY_CNTCT_PREF_VAL(["dbo.PRTY_CNTCT_PREF_VAL"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PRTY_CNTCT_PREF_VAL |

## View Code

```sql
create view [dbo].[syncobj_0x3445463042343744]as select  [CNTCT_PREF_ID],[PREF_TYPE_GRP_ID],[PREF_TYPE_CODE],[PREF_TYPE_VAL_SEQ]  from  [dbo].[PRTY_CNTCT_PREF_VAL]  where HAS_PERMS_BY_NAME('[dbo].[PRTY_CNTCT_PREF_VAL]', 'OBJECT', 'SELECT')= 1
```

