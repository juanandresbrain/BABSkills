# dbo.syncobj_0x4645313833374341

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4645313833374341"]
    dbo_ORG_CAR_LANG(["dbo.ORG_CAR_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CAR_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4645313833374341]as select  [CAR_ID],[LANG_ID],[CAR_NAME]  from  [dbo].[ORG_CAR_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CAR_LANG]', 'OBJECT', 'SELECT')= 1
```

