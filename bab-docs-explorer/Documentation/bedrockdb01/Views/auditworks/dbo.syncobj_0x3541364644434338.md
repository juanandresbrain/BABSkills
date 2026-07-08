# dbo.syncobj_0x3541364644434338

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3541364644434338"]
    dbo_ORG_BANK_LANG(["dbo.ORG_BANK_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_BANK_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3541364644434338]as select  [BANK_ID],[LANG_ID],[BANK_NAME],[BANK_SHRT_NAME]  from  [dbo].[ORG_BANK_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_BANK_LANG]', 'OBJECT', 'SELECT')= 1
```

