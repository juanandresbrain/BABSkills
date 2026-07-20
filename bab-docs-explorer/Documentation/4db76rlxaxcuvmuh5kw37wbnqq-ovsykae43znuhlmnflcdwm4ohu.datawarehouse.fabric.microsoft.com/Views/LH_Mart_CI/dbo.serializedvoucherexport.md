# dbo.serializedvoucherexport

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.serializedvoucherexport"]
    dbo_serializedvoucherexport(["dbo.serializedvoucherexport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.serializedvoucherexport |

## View Code

```sql
; CREATE   VIEW [dbo].[serializedvoucherexport] AS     SELECT [cntryAbbr] COLLATE Latin1_General_CI_AS AS [cntryAbbr], [discountID], [totalCoupons], [couponNumber]     FROM [dbo].[serializedvoucherexport]
```

