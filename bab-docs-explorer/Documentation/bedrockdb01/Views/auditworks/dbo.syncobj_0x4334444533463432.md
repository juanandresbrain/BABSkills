# dbo.syncobj_0x4334444533463432

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4334444533463432"]
    dbo_ORG_PYMNT_PRCSR(["dbo.ORG_PYMNT_PRCSR"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_PYMNT_PRCSR |

## View Code

```sql
create view [dbo].[syncobj_0x4334444533463432]as select  [PYMNT_PRCSR_CODE],[PYMNT_PRCSR_NAME],[PYMNT_PRCSR_SHRT_NAME],[ACTV]  from  [dbo].[ORG_PYMNT_PRCSR]  where HAS_PERMS_BY_NAME('[dbo].[ORG_PYMNT_PRCSR]', 'OBJECT', 'SELECT')= 1
```

