# dbo.syncobj_0x4437353343303430

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4437353343303430"]
    dbo_GEOG_CNTRY_ADRS_RULE(["dbo.GEOG_CNTRY_ADRS_RULE"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GEOG_CNTRY_ADRS_RULE |

## View Code

```sql
create view [dbo].[syncobj_0x4437353343303430]as select  [CNTRY_CODE_ISO3],[ADRS_RULE_ID]  from  [dbo].[GEOG_CNTRY_ADRS_RULE]  where HAS_PERMS_BY_NAME('[dbo].[GEOG_CNTRY_ADRS_RULE]', 'OBJECT', 'SELECT')= 1
```

