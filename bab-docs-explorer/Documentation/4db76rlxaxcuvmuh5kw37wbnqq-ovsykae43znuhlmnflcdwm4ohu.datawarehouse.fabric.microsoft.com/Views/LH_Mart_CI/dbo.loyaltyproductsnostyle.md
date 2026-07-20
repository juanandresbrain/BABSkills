# dbo.loyaltyproductsnostyle

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.loyaltyproductsnostyle"]
    dbo_loyaltyproductsnostyle(["dbo.loyaltyproductsnostyle"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.loyaltyproductsnostyle |

## View Code

```sql
; CREATE   VIEW [dbo].[loyaltyproductsnostyle] AS     SELECT [ProductKey], [Style] COLLATE Latin1_General_CI_AS AS [Style], [StyleDescription] COLLATE Latin1_General_CI_AS AS [StyleDescription], [Color] COLLATE Latin1_General_CI_AS AS [Color], [Concept] COLLATE Latin1_General_CI_AS AS [Concept], [Chain] COLLATE Latin1_General_CI_AS AS [Chain], [Division] COLLATE Latin1_General_CI_AS AS [Division], [Department] COLLATE Latin1_General_CI_AS AS [Department], [Class] COLLATE Latin1_General_CI_AS AS [Class], [SubClass] COLLATE Latin1_General_CI_AS AS [SubClass], [DeptCode] COLLATE Latin1_General_CI_AS AS [DeptCode], [SubClassCode] COLLATE Latin1_General_CI_AS AS [SubClassCode], [ScorecardCategory] COLLATE Latin1_General_CI_AS AS [ScorecardCategory], [PrimaryVendorCode] COLLATE Latin1_General_CI_AS AS [PrimaryVendorCode], [PrimaryVendorName] COLLATE Latin1_General_CI_AS AS [PrimaryVendorName], [AltPrimaryVendorCode] COLLATE Latin1_General_CI_AS AS [AltPrimaryVendorCode], [CurrentRetail], [OriginalRetail], [CurrentSellingRetailHome], [PriceWithVat], [EuroValue], [CanValue], [MerchStatus] COLLATE Latin1_General_CI_AS AS [MerchStatus], [JurisdictionCode] COLLATE Latin1_General_CI_AS AS [JurisdictionCode], [Gender] COLLATE Latin1_General_CI_AS AS [Gender], [CoreFashCode] COLLATE Latin1_General_CI_AS AS [CoreFashCode], [InlineCode] COLLATE Latin1_General_CI_AS AS [InlineCode], [ActivationDate], [KeyStory] COLLATE Latin1_General_CI_AS AS [KeyStory], [LicenseCode] COLLATE Latin1_General_CI_AS AS [LicenseCode]     FROM [dbo].[loyaltyproductsnostyle]
```

