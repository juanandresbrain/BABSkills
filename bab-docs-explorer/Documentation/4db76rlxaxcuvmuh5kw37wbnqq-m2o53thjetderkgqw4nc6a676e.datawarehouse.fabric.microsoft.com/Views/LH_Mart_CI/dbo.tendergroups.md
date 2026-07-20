# dbo.tendergroups

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tendergroups"]
    dbo_tendergroups(["dbo.tendergroups"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tendergroups |

## View Code

```sql
;

CREATE VIEW dbo.tendergroups AS SELECT TenderCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS TenderCode, TenderDesc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS TenderDesc, LoyaltyGrouping COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS LoyaltyGrouping FROM LH_Mart.dbo.tendergroups;
```

