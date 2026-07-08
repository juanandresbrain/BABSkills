# dbo.syncobj_0x4337464638354332

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4337464638354332"]
    dbo_EMPLY_HRCHY(["dbo.EMPLY_HRCHY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLY_HRCHY |

## View Code

```sql
create view [dbo].[syncobj_0x4337464638354332]as select  [HRCHY_ID],[HRCHY_DESC],[ACTV],[DFLT_GRP_ID],[SCRTY_USER_ID],[MTLY_EXCLSV],[MNDTRY_ASGNMNT]  from  [dbo].[EMPLY_HRCHY]  where HAS_PERMS_BY_NAME('[dbo].[EMPLY_HRCHY]', 'OBJECT', 'SELECT')= 1
```

