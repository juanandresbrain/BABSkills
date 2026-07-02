# dbo.NSBTranslate_LogTrans

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| iAWTransID | int | 4 | 0 | YES |  |  |
| sBatchID | varchar | 50 | 0 |  |  |  |
| sOrderNumber | varchar | 50 | 0 |  |  |  |
| dTimeStamp | datetime | 8 | 0 |  |  |  |
| mAmount | money | 8 | 1 |  |  |  |
| iUnits | int | 4 | 1 |  |  |  |
| sStore | varchar | 10 | 1 |  |  |  |
| iStoreID | int | 4 | 0 | YES |  |  |
| mCcAmount | money | 8 | 1 |  |  |  |
| mGcTenderAmount | money | 8 | 1 |  |  |  |
| mVoucherAmount | money | 8 | 1 |  |  |  |
| sSiteCode | varchar | 10 | 1 |  |  |  |
| mGAAP | money | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spUpdateWMItemStatus_to_SalesAuditComplete](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMItemStatus_to_SalesAuditComplete.md)
- [WebOrderProcessing: WM.spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715.md)
- [BABWeCommerce: dbo.spCountNSBLogTransOrders](../../StoredProcedures/BABWeCommerce/dbo.spCountNSBLogTransOrders.md)

