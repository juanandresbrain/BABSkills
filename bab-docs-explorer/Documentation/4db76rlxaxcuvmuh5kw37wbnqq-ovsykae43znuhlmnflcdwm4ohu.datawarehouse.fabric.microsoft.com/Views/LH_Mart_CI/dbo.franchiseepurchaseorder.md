# dbo.franchiseepurchaseorder

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[franchiseepurchaseorder] AS     SELECT [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [PurchaseOrderID] COLLATE Latin1_General_CI_AS AS [PurchaseOrderID], [PurchaseOrderLineID], [WarehouseID] COLLATE Latin1_General_CI_AS AS [WarehouseID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units], [LinePrice], [DueDate], [InsertDate], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID]     FROM [dbo].[franchiseepurchaseorder]
```

