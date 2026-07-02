# WM.Transactions

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 | YES |  |  |
| TransactionNum | varchar | 22 | 0 |  |  |  |
| ClientID | varchar | 64 | 0 |  |  |  |
| TransactionDateTime | datetime | 8 | 0 |  |  |  |
| TaxAmount | money | 8 | 1 |  |  |  |
| TaxJurisdiction | varchar | 50 | 1 |  |  |  |
| TaxAuthority | varchar | 50 | 1 |  |  |  |
| TaxType | int | 4 | 1 |  |  |  |
| tmpTransID | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWOrderManagement: WM.RemoveOldTransactionData](../../StoredProcedures/BABWOrderManagement/WM.RemoveOldTransactionData.md)
- [WebOrderProcessing: WM.spGetReturnWMOrdersTaxes_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrdersTaxes_V2.md)
- [WebOrderProcessing: WM.spGetReturnWMOrdersTaxes_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrdersTaxes_V3.md)
- [WebOrderProcessing: WM.spGetReturnWMOrdersTaxes_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrdersTaxes_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V2_BJB20200430](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V2_BJB20200430.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V3_2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V3_2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrdersTaxes](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrdersTaxes.md)
- [WebOrderProcessing: WM.spGetShippedWMOrdersTaxes_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrdersTaxes_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrdersTaxes_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrdersTaxes_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrdersTaxes_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrdersTaxes_V3_1.md)
- [WebOrderProcessing: WM.spUpdateWMItemStatus_to_SalesAuditComplete](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMItemStatus_to_SalesAuditComplete.md)
- [WebOrderProcessing: WM.spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715.md)

