# dbo.transactiontaxdynamicsstage

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transactiontaxdynamicsstage"]
    dbo_transactiontaxdynamicsstage(["dbo.transactiontaxdynamicsstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transactiontaxdynamicsstage |

## View Code

```sql
CREATE   VIEW [dbo].[transactiontaxdynamicsstage] AS SELECT transaction_id, line_sequence, line_object, line_action, gross_line_amount, pos_discount_amount, taxable_amount, nontaxable_amount, combined_rate, tax_amount_expected, InsertDate, UpdateDate, tax_level, line_id FROM LH_Mart.dbo.transactiontaxdynamicsstage;
```

