# dbo.vwDW_dim_crm_transaction_category_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_dim_crm_transaction_category_dim"]
    dbo_dim_crm_transaction_category(["dbo.dim_crm_transaction_category"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dim_crm_transaction_category |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_dim_crm_transaction_category_dim]
AS
SELECT [crm_trans_category_key]
      ,[crm_trans_category_code]
      ,[crm_trans_category_desc]
  FROM [dw].[dbo].[dim_crm_transaction_category]
```

