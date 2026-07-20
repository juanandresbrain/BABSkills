# dbo.franchiseepurchaseorder

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseepurchaseorder"]
    dbo_franchiseepurchaseorder(["dbo.franchiseepurchaseorder"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseepurchaseorder |

## View Code

```sql
;

CREATE VIEW dbo.franchiseepurchaseorder AS SELECT Franchisee COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Franchisee, PurchaseOrderID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS PurchaseOrderID, PurchaseOrderLineID, WarehouseID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS WarehouseID, Style COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Style, Units, LinePrice, DueDate, InsertDate, BatchID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS BatchID FROM LH_Mart.dbo.franchiseepurchaseorder;
```

