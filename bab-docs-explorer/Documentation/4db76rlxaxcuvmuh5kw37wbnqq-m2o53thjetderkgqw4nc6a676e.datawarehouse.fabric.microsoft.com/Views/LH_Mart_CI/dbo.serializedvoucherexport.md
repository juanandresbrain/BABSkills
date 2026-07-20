# dbo.serializedvoucherexport

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.serializedvoucherexport"]
    dbo_serializedvoucherexport(["dbo.serializedvoucherexport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.serializedvoucherexport |

## View Code

```sql
;

CREATE VIEW dbo.serializedvoucherexport AS SELECT cntryAbbr COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS cntryAbbr, discountID, totalCoupons, couponNumber FROM LH_Mart.dbo.serializedvoucherexport;
```

