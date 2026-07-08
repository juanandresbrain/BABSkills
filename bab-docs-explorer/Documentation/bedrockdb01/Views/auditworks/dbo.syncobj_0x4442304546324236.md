# dbo.syncobj_0x4442304546324236

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4442304546324236"]
    dbo_CLNDR_TMPLT_LANG(["dbo.CLNDR_TMPLT_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_TMPLT_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4442304546324236]as select  [LANG_ID],[CLNDR_TMPLT_ID],[CLNDR_TMPLT_DESC]  from  [dbo].[CLNDR_TMPLT_LANG]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_TMPLT_LANG]', 'OBJECT', 'SELECT')= 1
```

