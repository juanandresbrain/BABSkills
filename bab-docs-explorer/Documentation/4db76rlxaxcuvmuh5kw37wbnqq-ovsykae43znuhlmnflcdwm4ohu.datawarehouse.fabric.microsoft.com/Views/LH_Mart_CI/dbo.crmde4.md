# dbo.crmde4

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmde4"]
    dbo_crmde4(["dbo.crmde4"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmde4 |

## View Code

```sql
; CREATE   VIEW [dbo].[crmde4] AS     SELECT [transactionID], [units], [event_name] COLLATE Latin1_General_CI_AS AS [event_name], [category] COLLATE Latin1_General_CI_AS AS [category], [unit_gross_amount], [coupon_desc] COLLATE Latin1_General_CI_AS AS [coupon_desc], [InsertDate], [UpdateDate], [recID], [couponNumber], [certificateNumber] COLLATE Latin1_General_CI_AS AS [certificateNumber]     FROM [dbo].[crmde4]
```

