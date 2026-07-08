# dbo.syncobj_0x4234373445353638

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4234373445353638"]
    dbo_GEOG_CNTRY_TLPHNY_RULE_LANG(["dbo.GEOG_CNTRY_TLPHNY_RULE_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GEOG_CNTRY_TLPHNY_RULE_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4234373445353638]as select  [LANG_ID],[TLPHNY_RULE_ID],[TLPHNY_RULE_DESC],[TLPHNY_RULE_SHRT_DESC]  from  [dbo].[GEOG_CNTRY_TLPHNY_RULE_LANG]  where HAS_PERMS_BY_NAME('[dbo].[GEOG_CNTRY_TLPHNY_RULE_LANG]', 'OBJECT', 'SELECT')= 1
```

