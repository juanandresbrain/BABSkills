# dbo.outbounddiscountresults

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.outbounddiscountresults"]
    dbo_outbounddiscountresults(["dbo.outbounddiscountresults"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.outbounddiscountresults |

## View Code

```sql
; CREATE   VIEW [dbo].[outbounddiscountresults] AS SELECT [fiscal_year], [fiscal_period], [dmDiscountID], [categoryTypeID], [isExpired], [transaction_id], [country] COLLATE Latin1_General_CI_AS AS [country], [unit_Gross_Amount], [numRedeemed] FROM [dbo].[outbounddiscountresults]
```

