# dbo.syncobj_0x3345363730454138

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3345363730454138"]
    dbo_CORE_RSN_GRP(["dbo.CORE_RSN_GRP"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CORE_RSN_GRP |

## View Code

```sql
create view [dbo].[syncobj_0x3345363730454138]as select  [RSN_GRP_ID],[RSN_GRP_DESC],[RSN_GRP_SHRT_DESC],[SYS_CODE]  from  [dbo].[CORE_RSN_GRP]  where HAS_PERMS_BY_NAME('[dbo].[CORE_RSN_GRP]', 'OBJECT', 'SELECT')= 1
```

