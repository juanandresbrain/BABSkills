# WM.OrdersNotInWM

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 10 | 1 |  |  |  |
| OrderFileName | varchar | 100 | 1 |  |  |  |
| OrderImportDateTime | datetime | 8 | 1 |  |  |  |
| WMFileName | varchar | 50 | 1 |  |  |  |
| SendTime | datetime | 8 | 1 |  |  |  |
| ErrorMessage | nvarchar | -1 | 1 |  |  |  |
| LogDateTime | datetime | 8 | 1 |  |  |  |
| Attempts | int | 4 | 1 |  |  |  |
| OrderStatus | varchar | 25 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spWMPickticketXMLOnDemand](../../StoredProcedures/WebOrderProcessing/WM.spWMPickticketXMLOnDemand.md)

