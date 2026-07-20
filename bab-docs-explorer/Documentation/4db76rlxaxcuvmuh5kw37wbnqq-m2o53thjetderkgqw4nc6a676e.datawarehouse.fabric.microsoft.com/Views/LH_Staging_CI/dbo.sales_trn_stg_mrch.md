# dbo.sales_trn_stg_mrch

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sales_trn_stg_mrch"]
    dbo_sales_trn_stg_mrch(["dbo.sales_trn_stg_mrch"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sales_trn_stg_mrch |

## View Code

```sql
;
CREATE   VIEW [dbo].[sales_trn_stg_mrch]
AS
    SELECT [Transaction_Date], [Store_No], [Register_No], [Transaction_ID], [Transaction_No], [Line_ID], [Line_Sequence], [Cashier_No], [Gross_Line_Amount], [POS_Discount_Amount], [POS_Discount_Type], [Entry_Date_Time], [Line_Object], [Reference_No] COLLATE Latin1_General_CI_AS AS [Reference_No], [Line_Action], [Units], [Transaction_Begin] COLLATE Latin1_General_CI_AS AS [Transaction_Begin], [Vat_Tax_Amt], [VirtualWorld_SerialNumber] COLLATE Latin1_General_CI_AS AS [VirtualWorld_SerialNumber], [Dummy_Flag], [bear_id] COLLATE Latin1_General_CI_AS AS [bear_id], [store_key], [date_key], [time_key], [product_key], [Upsell_Discount_Allocated], [ext_Cost]
    FROM LH_Staging.[dbo].[sales_trn_stg_mrch]
```

