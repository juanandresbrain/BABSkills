# dbo.syncobj_0x3345313544443835

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3345313544443835"]
    dbo_ORG_CHN_LOC_ENV_CLS_A(["dbo.ORG_CHN_LOC_ENV_CLS_A"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_ENV_CLS_A |

## View Code

```sql
create view [dbo].[syncobj_0x3345313544443835]as select  [LOC_ID],[ENV_CLS_CODE],[FDN_CSTMZTN_DATA]  from  [dbo].[ORG_CHN_LOC_ENV_CLS_A]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_ENV_CLS_A]', 'OBJECT', 'SELECT')= 1
```

