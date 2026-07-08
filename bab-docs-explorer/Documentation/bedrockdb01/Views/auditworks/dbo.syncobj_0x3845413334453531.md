# dbo.syncobj_0x3845413334453531

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3845413334453531"]
    dbo_PRTY_ADRS_FNCTN(["dbo.PRTY_ADRS_FNCTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PRTY_ADRS_FNCTN |

## View Code

```sql
create view [dbo].[syncobj_0x3845413334453531]as select  [ADRS_FNCTN_CODE],[ADRS_FNCTN_DESC],[ADRS_FNCTN_SHRT_DESC],[SYS_CODE]  from  [dbo].[PRTY_ADRS_FNCTN]  where HAS_PERMS_BY_NAME('[dbo].[PRTY_ADRS_FNCTN]', 'OBJECT', 'SELECT')= 1
```

