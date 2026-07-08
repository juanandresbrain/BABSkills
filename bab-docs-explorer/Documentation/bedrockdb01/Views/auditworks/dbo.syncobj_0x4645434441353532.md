# dbo.syncobj_0x4645434441353532

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4645434441353532"]
    dbo_CLNDR_TMPLT_ALGRTHM_LANG(["dbo.CLNDR_TMPLT_ALGRTHM_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_TMPLT_ALGRTHM_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4645434441353532]as select  [LANG_ID],[CLNDR_TMPLT_ALGRTHM_ID],[CLNDR_TMPLT_ALGRTHM_DESC]  from  [dbo].[CLNDR_TMPLT_ALGRTHM_LANG]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_TMPLT_ALGRTHM_LANG]', 'OBJECT', 'SELECT')= 1
```

