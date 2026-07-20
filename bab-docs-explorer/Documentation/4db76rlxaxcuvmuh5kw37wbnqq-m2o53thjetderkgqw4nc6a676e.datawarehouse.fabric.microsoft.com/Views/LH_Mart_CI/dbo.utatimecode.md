# dbo.utatimecode

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utatimecode"]
    dbo_utatimecode(["dbo.utatimecode"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utatimecode |

## View Code

```sql
;

CREATE VIEW dbo.utatimecode AS SELECT TCODE_ID, TCODE_NAME COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS TCODE_NAME, TCODE_DESC COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS TCODE_DESC, InsertDate, UpdateDate FROM LH_Mart.dbo.utatimecode;
```

