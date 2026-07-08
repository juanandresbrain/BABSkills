# dbo.syncobj_0x4132303631374333

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4132303631374333"]
    dbo_CLNDR_TMPLT(["dbo.CLNDR_TMPLT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_TMPLT |

## View Code

```sql
create view [dbo].[syncobj_0x4132303631374333]as select  [CLNDR_TMPLT_ID],[CLNDR_TMPLT_DESC]  from  [dbo].[CLNDR_TMPLT]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_TMPLT]', 'OBJECT', 'SELECT')= 1
```

