# dbo.serializedvoucher

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.serializedvoucher"]
    dbo_serializedvoucher(["dbo.serializedvoucher"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.serializedvoucher |

## View Code

```sql
; CREATE   VIEW [dbo].[serializedvoucher] AS     SELECT [SerializedNumber], [StartDate], [DiscountAmount], [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [Email] COLLATE Latin1_General_CI_AS AS [Email], [ExpirationDate], [isExported], [InsertDate], [UpdateDate], [FirstName] COLLATE Latin1_General_CI_AS AS [FirstName], [LastName] COLLATE Latin1_General_CI_AS AS [LastName], [Address1] COLLATE Latin1_General_CI_AS AS [Address1], [Address2] COLLATE Latin1_General_CI_AS AS [Address2], [City] COLLATE Latin1_General_CI_AS AS [City], [State] COLLATE Latin1_General_CI_AS AS [State], [ZipCode] COLLATE Latin1_General_CI_AS AS [ZipCode], [Country] COLLATE Latin1_General_CI_AS AS [Country], [ExportedDate], [ExportedDateXML], [CouponID], [Description] COLLATE Latin1_General_CI_AS AS [Description], [Status] COLLATE Latin1_General_CI_AS AS [Status], [title] COLLATE Latin1_General_CI_AS AS [title]     FROM [dbo].[serializedvoucher]
```

