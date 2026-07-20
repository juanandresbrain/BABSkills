# dbo.vwOmsValidationSource

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwOmsValidationSource"]
    dbo_mulesoft_dynamicsheaderoms(["dbo.mulesoft_dynamicsheaderoms"]) --> VIEW
    dbo_mulesoft_dynamicstaxlineoms(["dbo.mulesoft_dynamicstaxlineoms"]) --> VIEW
    dbo_mulesoft_dynamicstenderlineoms(["dbo.mulesoft_dynamicstenderlineoms"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.mulesoft_dynamicsheaderoms |
| dbo.mulesoft_dynamicstaxlineoms |
| dbo.mulesoft_dynamicstenderlineoms |

## View Code

```sql
CREATE     view [vwOmsValidationSource]   as   select o.TransactionKey , o.TransDate , o.RetailReceiptId as SequenceNumber , o.Barcode , o.RetailTransactionId , cast (o.CreateTime as date) as CreateDate , o.DiscAmount as DiscountTotal , sum (t.Amount) as TaxTotal , sum (ten.AmountCur) as Total from [LH_Source].[dbo].[mulesoft_dynamicsheaderoms] o join [LH_Source].[dbo].[mulesoft_dynamicstaxlineoms] t on t.RetailTransactionId = o.RetailTransactionId join [LH_Source].[dbo].[mulesoft_dynamicstenderlineoms] ten on ten.RetailTransactionId = o.RetailTransactionId group by o.TransactionKey , o.TransDate , o.RetailReceiptId , o.Barcode , o.RetailTransactionId , cast (o.CreateTime as date) , o.DiscAmount
```

