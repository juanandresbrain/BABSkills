# dbo.InventJourTransView_missingKeys

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.InventJourTransView_missingKeys"]
    dbo_InventJourTransView(["dbo.InventJourTransView"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.InventJourTransView |

## View Code

```sql
CREATE   VIEW [dbo].[InventJourTransView_missingKeys]
AS
SELECT
 [Department]
      ,[Subclass]
      ,[IB Inventory ID]
      ,[Inventory Document Number]
      ,[Inventory Status Description]
      ,[Inventory Status Code]
      ,[Inventory Trans Cost]
      ,[Inventory Trans Date]
      ,[Inventory Trans Retail]
      ,[Inventory Trans Selling Retail]
      ,[Inventory Trans Type Code]
      ,[Inventory Trans Type Desc]
      ,[InventoryTrans Units]
      ,[Jurisdiction Code]
      ,[Location Code]
      ,[dataareaid]
      ,[MDSE\Supply]
      ,[Other Location Code]
      ,[Style Code]
      ,[Style Short Description]
      ,[Trans Reason Code (outer)]
      ,[journaltype]
      ,[journalnameid]
      ,[productkey]
      ,[LocationKey]
      ,[ZeroBalanceVoucher]
FROM [dbo].[InventJourTransView]
--WHERE [productkey] IS NULL
--OR [LocationKey] IS NULL
```

