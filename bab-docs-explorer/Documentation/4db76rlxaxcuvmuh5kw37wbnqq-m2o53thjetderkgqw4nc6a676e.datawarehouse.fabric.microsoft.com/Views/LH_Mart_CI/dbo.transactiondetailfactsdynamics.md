# dbo.transactiondetailfactsdynamics

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transactiondetailfactsdynamics"]
    dbo_transactiondetailfactsdynamics(["dbo.transactiondetailfactsdynamics"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transactiondetailfactsdynamics |

## View Code

```sql
;

CREATE VIEW dbo.transactiondetailfactsdynamics AS SELECT product_key, currency_key, transaction_id, transaction_line_seq, Register_Num, cashier_id, time_key, store_key, unit_gross_amount, date_key, units, unit_disc_amount, party_y_n COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS party_y_n, transaction_type_key, line_object_key, tdf_key, transaction_no, reference_no COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS reference_no, vat_tax_amount, INS_DT, UPDT_DT, ETL_LOG_ID, ETL_EVNT_ID, upsell_disc_allocated, ext_cost, line_action_key FROM LH_Mart.dbo.transactiondetailfactsdynamics;
```

