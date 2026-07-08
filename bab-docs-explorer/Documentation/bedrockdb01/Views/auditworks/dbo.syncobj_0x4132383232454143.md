# dbo.syncobj_0x4132383232454143

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4132383232454143"]
    dbo_CORE_ENV_CLS(["dbo.CORE_ENV_CLS"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CORE_ENV_CLS |

## View Code

```sql
create view [dbo].[syncobj_0x4132383232454143]as select  [ENV_CLS_CODE],[ENV_CLS_DESC],[ENV_CLS_SHRT_DESC]  from  [dbo].[CORE_ENV_CLS]  where HAS_PERMS_BY_NAME('[dbo].[CORE_ENV_CLS]', 'OBJECT', 'SELECT')= 1
```

