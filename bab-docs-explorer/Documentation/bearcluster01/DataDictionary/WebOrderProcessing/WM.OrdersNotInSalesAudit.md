# WM.OrdersNotInSalesAudit

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNum | varchar | 10 | 1 |  |  |  |
| ShipDate | datetime | 8 | 1 |  |  |  |
| InSettlementData | varchar | 3 | 1 |  |  |  |
| CheckDateTime | datetime | 8 | 1 |  |  |  |
| ESReferenceNo | varchar | 19 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spEmailWebOrdersNotInSalesAudit](../../StoredProcedures/WebOrderProcessing/WM.spEmailWebOrdersNotInSalesAudit.md)

