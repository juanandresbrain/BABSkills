# dbo.franchiseeinventory

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseeinventory"]
    dbo_franchiseeinventory(["dbo.franchiseeinventory"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseeinventory |

## View Code

```sql
;

CREATE VIEW dbo.franchiseeinventory AS SELECT InventoryID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS InventoryID, InventoryLineNo, Franchisee COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Franchisee, StoreID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS StoreID, InventoryDate, Style COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Style, OnHand, Cost, InsertDate, BatchID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS BatchID FROM LH_Mart.dbo.franchiseeinventory;
```

