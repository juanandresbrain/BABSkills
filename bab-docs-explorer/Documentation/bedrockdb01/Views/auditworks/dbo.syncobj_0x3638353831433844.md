# dbo.syncobj_0x3638353831433844

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3638353831433844"]
    dbo_CRDM_PRMTRS_LANG(["dbo.CRDM_PRMTRS_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CRDM_PRMTRS_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3638353831433844]as select  [PRMTR_NAME],[LANG_ID],[PRMTR_DESC]  from  [dbo].[CRDM_PRMTRS_LANG]  where HAS_PERMS_BY_NAME('[dbo].[CRDM_PRMTRS_LANG]', 'OBJECT', 'SELECT')= 1
```

