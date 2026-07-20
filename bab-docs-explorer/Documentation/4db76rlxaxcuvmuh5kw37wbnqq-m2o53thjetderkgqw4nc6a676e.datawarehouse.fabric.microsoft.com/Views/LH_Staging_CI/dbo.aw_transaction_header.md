# dbo.aw_transaction_header

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.aw_transaction_header"]
    dbo_aw_transaction_header(["dbo.aw_transaction_header"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.aw_transaction_header |

## View Code

```sql
;
CREATE   VIEW [dbo].[aw_transaction_header]
AS
    SELECT [transaction_id], [store_no], [register_no], [transaction_no], [cashier_no], [transaction_category], [transaction_series] COLLATE Latin1_General_CI_AS AS [transaction_series], [transaction_date], [entry_date_time], [store_key], [date_key], [time_key], [party_y_n] COLLATE Latin1_General_CI_AS AS [party_y_n], [tender_total], [batchNumber], [transaction_type] COLLATE Latin1_General_CI_AS AS [transaction_type], [currency_code] COLLATE Latin1_General_CI_AS AS [currency_code], [currency_key], [cashier_key], [party_master], [party_key]
    FROM LH_Staging.[dbo].[aw_transaction_header]
```

