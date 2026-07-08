# dbo.syncobj_0x4539313143424541

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4539313143424541"]
    dbo_CLNDR_LVL(["dbo.CLNDR_LVL"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_LVL |

## View Code

```sql
create view [dbo].[syncobj_0x4539313143424541]as select  [CLNDR_ID],[CLNDR_LVL_TYPE_ID],[ROOT_FLAG]  from  [dbo].[CLNDR_LVL]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_LVL]', 'OBJECT', 'SELECT')= 1
```

