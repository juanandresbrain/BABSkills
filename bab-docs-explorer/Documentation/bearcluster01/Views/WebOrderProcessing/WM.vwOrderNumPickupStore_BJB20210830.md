# WM.vwOrderNumPickupStore_BJB20210830

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwOrderNumPickupStore_BJB20210830"]
    WM_Orders(["WM.Orders"]) --> VIEW
    WM_vwOrderOrderTransactionIdentifier(["WM.vwOrderOrderTransactionIdentifier"]) --> VIEW
    WM_vwTransactionDetailPayments_V2(["WM.vwTransactionDetailPayments_V2"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.Orders |
| WM.vwOrderOrderTransactionIdentifier |
| WM.vwTransactionDetailPayments_V2 |

## View Code

```sql
CREATE VIEW [WM].[vwOrderNumPickupStore_BJB20210830]
AS
SELECT        MAX(o.OrderNum) AS OrderNumber, td.TransactionID, v.PickupStore, MAX(o.ShipmentNumber) AS ShipmentNumber, v.OrderTransactionIdentifier
FROM            WM.vwTransactionDetailPayments_V2 AS td INNER JOIN
                         WM.vwOrderOrderTransactionIdentifier AS v ON td.TransactionID = v.TransactionID AND td.OrderTransactionIdentifier = v.OrderTransactionIdentifier INNER JOIN
                         WM.Orders AS o ON v.TransactionID = o.TransactionID AND v.PickupStore = o.PickupStore AND o.OrderStatus IN ('Complete', 'Shipped', 'StorePickedForPickup')
GROUP BY td.TransactionID, v.PickupStore, v.OrderTransactionIdentifier
```

