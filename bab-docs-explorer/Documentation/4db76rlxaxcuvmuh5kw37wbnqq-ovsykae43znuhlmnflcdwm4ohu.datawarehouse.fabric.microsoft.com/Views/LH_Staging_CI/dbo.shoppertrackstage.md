# dbo.shoppertrackstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.shoppertrackstage"]
    dbo_shoppertrackstage(["dbo.shoppertrackstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.shoppertrackstage |

## View Code

```sql
; CREATE   VIEW [dbo].[shoppertrackstage] AS SELECT [ShopperTrakOrgId], [StoreKey], [DateKey], [TimeKey], [Enters], [Exits], [DataIndicatorName] COLLATE Latin1_General_CI_AS AS [DataIndicatorName] FROM [dbo].[shoppertrackstage]
```

