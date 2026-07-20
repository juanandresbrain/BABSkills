# dbo.crmde4

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmde4"]
    dbo_crmde4(["dbo.crmde4"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmde4 |

## View Code

```sql
CREATE   VIEW dbo.crmde4 AS SELECT transactionID, units, event_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS event_name, category COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS category, unit_gross_amount, coupon_desc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS coupon_desc, InsertDate, UpdateDate, recID, couponNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8 as couponNumber, certificateNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS certificateNumber FROM LH_Mart.dbo.crmde4;;
```

