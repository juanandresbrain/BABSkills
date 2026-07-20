# dbo.tmpliccode

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpliccode"]
    dbo_tmpliccode(["dbo.tmpliccode"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpliccode |

## View Code

```sql
;

CREATE VIEW dbo.tmpliccode AS SELECT KeyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS KeyStory, licenseCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS licenseCode FROM LH_Mart.dbo.tmpliccode;
```

