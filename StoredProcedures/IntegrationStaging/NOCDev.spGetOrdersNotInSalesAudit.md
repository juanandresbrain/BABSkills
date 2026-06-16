# NOCDev.spGetOrdersNotInSalesAudit

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["NOCDev.spGetOrdersNotInSalesAudit"]
    WM_OrdersNotInSalesAudit(["WM.OrdersNotInSalesAudit"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.OrdersNotInSalesAudit |

## Stored Procedure Code

```sql
CREATE proc [NOCDev].[spGetOrdersNotInSalesAudit]

as

-------------------------------------------------------------------------					
-- 2021-11-10 - Brandon Hickey - Created Proc
-------------------------------------------------------------------------

set nocount on

SELECT OrderNum,
	ShipDate,
	InSettlementData,
	CheckDateTime 
FROM [BEARCLUSTER01.SQL.BUILDABEAR.COM].[WebOrderProcessing].[WM].[OrdersNotInSalesAudit]
```

