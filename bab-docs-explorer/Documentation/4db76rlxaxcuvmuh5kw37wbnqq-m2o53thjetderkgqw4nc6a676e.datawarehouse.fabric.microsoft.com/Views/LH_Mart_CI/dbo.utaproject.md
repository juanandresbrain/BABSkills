# dbo.utaproject

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaproject"]
    dbo_utaproject(["dbo.utaproject"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaproject |

## View Code

```sql
;

CREATE VIEW dbo.utaproject AS SELECT PROJ_ID, PROJ_NAME COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS PROJ_NAME, PROJ_DESC COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS PROJ_DESC, InsertDate, UpdateDate FROM LH_Mart.dbo.utaproject;
```

