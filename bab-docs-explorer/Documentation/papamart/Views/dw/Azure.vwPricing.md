# Azure.vwPricing

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPricing"]
    Azure_Price(["Azure.Price"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.Price |

## View Code

```sql
CREATE view [Azure].[vwPricing]

as
-- =============================================================================================================
-- Name: [Azure].[vwPricing]
--
-- Description: Warehouse Inventory
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		John Eck			12/19/2018		Initial Creation

--											
-- =============================================================================================================
With C AS (
Select ProductKey,[IE Price] as IE_Current_Retail , [DK Price] as DK_Current_Retail
From (Select ProductKey,PriceType,Current_Selling_REtail
	From Azure.Price) p
Pivot
 (Max(Current_Selling_Retail)
 For PriceType in ([IE Price],[DK Price])
 ) AS pvt),
O AS (
 Select ProductKey,[IE Price] as IE_Original_Retail , [DK Price] as DK_Original_Retail
From (Select ProductKey,PriceType,Original_Selling_REtail
	From Azure.Price) p
Pivot
 (Max(Original_Selling_Retail)
 For PriceType in ([IE Price],[DK Price])
 ) AS pvt2
 )

Select H.*,IE_Current_Retail, DK_Current_Retail, IE_Original_Retail, DK_Original_Retail
From Azure.Price H left Join C on h.productKey = c.productKey
					left Join o on h.productKey = o.productKey
					where PriceType = 'Home'
```

