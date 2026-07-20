# dbo.franchiseetransactiondetailfacts_stage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactiondetailfacts_stage"]
    dbo_franchiseetransactiondetailfacts_stage(["dbo.franchiseetransactiondetailfacts_stage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactiondetailfacts_stage |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactiondetailfacts_stage] AS SELECT [product_key], [currency_key], [transaction_id] COLLATE Latin1_General_CI_AS AS [transaction_id], [transaction_line_seq], [register_num], [cashier_id], [time_key], [store_key], [unit_gross_amount], [date_key], [units], [unit_disc_amount], [party_y_n], [transaction_type_key], [line_object_key], [tdf_key], [transaction_no] COLLATE Latin1_General_CI_AS AS [transaction_no], [reference_no], [vat_tax_amount], [INS_DT], [UPDT_DT], [etl_log_id], [etl_evnt_id], [upsell_disc_allocated], [ext_cost], [line_action_key] FROM [dbo].[franchiseetransactiondetailfacts_stage]
```

