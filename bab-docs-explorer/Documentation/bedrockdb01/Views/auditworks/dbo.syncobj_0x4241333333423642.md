# dbo.syncobj_0x4241333333423642

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4241333333423642"]
    dbo_ORG_CHN_HRCHY(["dbo.ORG_CHN_HRCHY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_HRCHY |

## View Code

```sql
create view [dbo].[syncobj_0x4241333333423642]as select  [HRCHY_ID],[HRCHY_DESC],[ACTV],[DFLT_GRP_ID],[SCRTY_USER_ID],[MTLY_EXCLSV],[MNDTRY_ASGNMNT]  from  [dbo].[ORG_CHN_HRCHY]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_HRCHY]', 'OBJECT', 'SELECT')= 1
```

