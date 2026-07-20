# dbo.InventSumCurrentViewForWHSEnabledItems

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.InventSumCurrentViewForWHSEnabledItems"]
    dbo_InventSumCurrentViewForWHSEnabledItems_base(["dbo.InventSumCurrentViewForWHSEnabledItems_base"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.InventSumCurrentViewForWHSEnabledItems_base |

## View Code

```sql
/****** Object:  View [dbo].[InventSumCurrentViewForWHSEnabledItems]    Script Date: 3/27/2026 11:31:06 AM ******/  CREATE   VIEW [dbo].[InventSumCurrentViewForWHSEnabledItems] AS   SELECT [LocationKey]       ,[product_key]       ,[dataareaid]       ,[inventsiteid]       ,[inventlocationid]       ,[inventstatusid]       ,[itemid]       ,[AvailablePhysicalCalculated]       ,[Available to Distribute]       ,[AllocationUnit]       ,[onorder]       ,[lastupddateexpected]       ,[AVAIL + INTRANS]       ,[CUR AVAI O/H]       ,[CUR AVAI O/H Sellable]       ,[CUR AVAI O/H Non-Sellable]       ,[InTr Qty]       ,[arrived]       ,[availordered]       ,[availphysical]       ,[deducted]       ,[ordered]       ,[physicalinvent]       ,[picked]       ,[postedqty]       ,[quotationissue]       ,[quotationreceipt]       ,[received]       ,[registered]       ,[reservordered]       ,[reservphysical]       ,[CreatedNotShippedQty]       ,[ShippedNotReceivedQty]       ,[SO On Order]       ,[PO Ordered]       ,[CurrentWeekSales]       ,[CUR AVAI O/H Prior Day] 	  ,[Next Ordered Quantity] 	  ,[Next Ordered Date] 	  ,[intransit_units]         ,[on_hand_unit_cost] FROM [dbo].[InventSumCurrentViewForWHSEnabledItems_base] --WHERE [inventstatusid] IN ('AVAIL', 'PendPut')
```

