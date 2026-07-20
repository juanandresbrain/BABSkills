# dbo.Azure_vwPricing

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Azure_vwPricing"]
    dbo_azure_price(["dbo.azure_price"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_price |

## View Code

```sql
CREATE view dbo.Azure_vwPricing as With C AS ( Select  ProductKey,[IE Price] as IE_Current_Retail , [DK Price] as DK_Current_Retail From (Select ProductKey,PriceType,Current_Selling_Retail 	From dbo.azure_price) p Pivot  (Max(Current_Selling_Retail)  For PriceType in ([IE Price],[DK Price])  ) AS pvt), O AS (  Select ProductKey,[IE Price] as IE_Original_Retail , [DK Price] as DK_Original_Retail From (Select ProductKey,PriceType,Original_Selling_Retail 	From dbo.azure_price) p Pivot  (Max(Original_Selling_Retail)  For PriceType in ([IE Price],[DK Price])  ) AS pvt2  )  Select H.*,IE_Current_Retail, DK_Current_Retail, IE_Original_Retail, DK_Original_Retail From dbo.azure_price H left Join C on H.ProductKey = C.ProductKey 					left Join O on H.ProductKey = O.ProductKey 					where PriceType = 'Home'
```

