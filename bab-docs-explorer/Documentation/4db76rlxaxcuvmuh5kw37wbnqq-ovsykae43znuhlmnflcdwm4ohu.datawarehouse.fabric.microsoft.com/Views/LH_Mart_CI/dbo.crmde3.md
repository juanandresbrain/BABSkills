# dbo.crmde3

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmde3"]
    dbo_crmde3(["dbo.crmde3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmde3 |

## View Code

```sql
; CREATE   VIEW [dbo].[crmde3] AS     SELECT [customerNumber] COLLATE Latin1_General_CI_AS AS [customerNumber], [transactionID], [purchaseDate], [purchaseChannel] COLLATE Latin1_General_CI_AS AS [purchaseChannel], [purchaseStoreNumber] COLLATE Latin1_General_CI_AS AS [purchaseStoreNumber], [purchaseRevenue], [purchaseUnitCount], [stuffed], [unstuffed], [licensedORNot], [consumerGroup] COLLATE Latin1_General_CI_AS AS [consumerGroup], [keyStory] COLLATE Latin1_General_CI_AS AS [keyStory], [department] COLLATE Latin1_General_CI_AS AS [department], [Country] COLLATE Latin1_General_CI_AS AS [Country], [sku] COLLATE Latin1_General_CI_AS AS [sku], [InsertDate], [UpdateDate], [recID], [Emailable]     FROM [dbo].[crmde3]
```

