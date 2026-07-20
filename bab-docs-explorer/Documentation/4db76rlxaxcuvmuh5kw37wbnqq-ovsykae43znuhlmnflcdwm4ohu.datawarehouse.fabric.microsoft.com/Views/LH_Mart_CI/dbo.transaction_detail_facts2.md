# dbo.transaction_detail_facts2

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transaction_detail_facts2"]
    dbo_transaction_detail_facts(["dbo.transaction_detail_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_detail_facts |

## View Code

```sql
; CREATE   VIEW [dbo].[transaction_detail_facts2] AS     SELECT [product_key], [currency_key], [transaction_id], [transaction_line_seq], [Register_Num], [cashier_id], [time_key], [store_key], [unit_gross_amount], [date_key], [units],      [unit_disc_amount], [party_y_n] COLLATE Latin1_General_CI_AS AS [party_y_n], [transaction_type_key], [line_object_key], [tdf_key], [transaction_no]     , [reference_no] COLLATE Latin1_General_CI_AS AS [reference_no], [vat_tax_amount], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID], [upsell_disc_allocated], [ext_cost], [line_action_key]     ,case when line_object_key not in (21,22,42,5) then reference_no else null end as style_code     FROM LH_Mart.[dbo].[transaction_detail_facts]
```

