# dbo.syncobj_0x3732374243413931

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3732374243413931"]
    dbo_CLNDR_TMPLT_LVL(["dbo.CLNDR_TMPLT_LVL"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_TMPLT_LVL |

## View Code

```sql
create view [dbo].[syncobj_0x3732374243413931]as select  [CLNDR_TMPLT_ID],[CLNDR_LVL_TYPE_ID],[TMPLT_LVL_TIME_SPAN],[LBL_ALGRTHM_ID],[ROOT_FLAG]  from  [dbo].[CLNDR_TMPLT_LVL]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_TMPLT_LVL]', 'OBJECT', 'SELECT')= 1
```

