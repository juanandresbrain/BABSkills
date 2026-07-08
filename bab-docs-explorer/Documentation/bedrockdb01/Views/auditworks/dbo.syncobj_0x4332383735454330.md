# dbo.syncobj_0x4332383735454330

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4332383735454330"]
    dbo_EMPLY_HRCHY_LVL_GRP_A(["dbo.EMPLY_HRCHY_LVL_GRP_A"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLY_HRCHY_LVL_GRP_A |

## View Code

```sql
create view [dbo].[syncobj_0x4332383735454330]as select  [HRCHY_LVL_GRP_ID],[EMPLY_NUM],[HRCHY_ID],[HRCHY_LVL_ID],[VRTL]  from  [dbo].[EMPLY_HRCHY_LVL_GRP_A]  where HAS_PERMS_BY_NAME('[dbo].[EMPLY_HRCHY_LVL_GRP_A]', 'OBJECT', 'SELECT')= 1
```

