# dbo.syncobj_0x3332424135303342

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3332424135303342"]
    dbo_GEOG_CRDNT_TYPE(["dbo.GEOG_CRDNT_TYPE"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GEOG_CRDNT_TYPE |

## View Code

```sql
create view [dbo].[syncobj_0x3332424135303342]as select  [CRDNT_TYPE_CODE],[CRDNT_TYPE_DESC],[CRDNT_TYPE_SHRT_DESC],[SYS_CODE]  from  [dbo].[GEOG_CRDNT_TYPE]  where HAS_PERMS_BY_NAME('[dbo].[GEOG_CRDNT_TYPE]', 'OBJECT', 'SELECT')= 1
```

