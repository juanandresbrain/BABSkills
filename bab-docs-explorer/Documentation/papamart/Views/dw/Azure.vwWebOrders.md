# Azure.vwWebOrders

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebOrders"]
    dbo_WebOrders(["dbo.WebOrders"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebOrders |

## View Code

```sql
/* =============================================================================================================
 Name: [Azure].[vwFlashGaapSales]

 Description: Azure view of the flaashGaap sales so the data can be pushed to Power BI


 Dependencies: 

 Revision History
		Name:				Date:			Comments:
		John Eck			8/7/2018		Initial creation*/
CREATE VIEW [Azure].[vwWebOrders]
AS
SELECT        SourceSite, TransactionID, OrderID, OrderNum, CAST(OrderDate AS Date) AS OrderDate, ShippingAmount, OrderStatus, StatusDate, Physical, StatusSortOrder,
              InsertDate, UpdateDate,ShipToPostalCode, ShipToState , ShipToCountry,
			  Case SourceSite when 'US' then 13 else 267 end as StoreKey,
			  Case ISNULL(ESReferenceNbr,'0') when '0' then 0 else 1 End AS ESFlag
			  FROM            dbo.WebOrders
```

