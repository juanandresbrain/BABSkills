# dbo.syncobj_0x4530324235313544

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4530324235313544"]
    dbo_CLNDR_MNTH_LANG(["dbo.CLNDR_MNTH_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_MNTH_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4530324235313544]as select  [LANG_ID],[MNTH_NUM],[MNTH_LBL]  from  [dbo].[CLNDR_MNTH_LANG]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_MNTH_LANG]', 'OBJECT', 'SELECT')= 1
```

