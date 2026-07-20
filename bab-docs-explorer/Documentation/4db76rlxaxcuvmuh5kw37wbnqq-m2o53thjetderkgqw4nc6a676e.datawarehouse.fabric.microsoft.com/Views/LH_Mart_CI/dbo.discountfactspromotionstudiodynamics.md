# dbo.discountfactspromotionstudiodynamics

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.discountfactspromotionstudiodynamics"]
    dbo_discountfactspromotionstudiodynamics(["dbo.discountfactspromotionstudiodynamics"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.discountfactspromotionstudiodynamics |

## View Code

```sql
;

CREATE VIEW dbo.discountfactspromotionstudiodynamics AS SELECT transaction_id, store_key, date_key, coupon_key, line_object_key, units, unit_gross_amount, reference_no COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS reference_no, process_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS process_name, process_date, uid, transaction_no, INS_DT, UPDT_DT, ETL_LOG_ID, ETL_EVNT_ID, categoryTypeID, isExpired, lift_amount, line_action_key FROM LH_Mart.dbo.discountfactspromotionstudiodynamics;;
```

