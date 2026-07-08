# dbo.syncobj_0x3334433446313333

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3334433446313333"]
    dbo_EMPLY_ORG_BANK_A(["dbo.EMPLY_ORG_BANK_A"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLY_ORG_BANK_A |

## View Code

```sql
create view [dbo].[syncobj_0x3334433446313333]as select  [EMPLY_NUM],[BANK_ID],[BRNCH_NUM],[ACNT_NUM],[FDN_CSTMZTN_DATA]  from  [dbo].[EMPLY_ORG_BANK_A]  where HAS_PERMS_BY_NAME('[dbo].[EMPLY_ORG_BANK_A]', 'OBJECT', 'SELECT')= 1
```

