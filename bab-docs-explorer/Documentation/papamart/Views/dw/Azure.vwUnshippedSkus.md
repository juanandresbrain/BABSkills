# Azure.vwUnshippedSkus

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwUnshippedSkus"]
    dbo_tmpUnshippedItemsWithLWunitsSales(["dbo.tmpUnshippedItemsWithLWunitsSales"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpUnshippedItemsWithLWunitsSales |

## View Code

```sql
CREATE view [Azure].[vwUnshippedSkus]

AS
-- =============================================================================================================
-- Name: [Azure].[vwDateFilter]
-- Description: This view is used to populate the power BI unshipped report 
-- Dependencies: 
-- Revision History
--		Name:				Date:			Comments:
--		Ian Wallace			4/16/2020		Initial creation
-- =============================================================================================================


SELECT [PickupStore],[StoreName],[StoreConcept],[ItemNumber],[ItemQty],[DistroDay],[DCsource],[StyleDescription],[consumer group],
[department],[class],[deptcode],[subclasscode],[OnHand],[Allocated],[InTransit],[DateKey],[ProductKey],[StoreKey],[PreviousFiscalWeek],[LWunitsSold]
,[keyStory],[mstat],[UnbufferedQty],[StoreInventoryBuffer],[totalQuantity],[StoreInTransit],[storeAllocated]
  FROM papamart.DWStaging.dbo.tmpUnshippedItemsWithLWunitsSales
```

