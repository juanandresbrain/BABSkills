# WM.OrderItemOverride

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ItemOverrideId | int | 4 | 0 |  |  |  |
| OriginalSku | varchar | 50 | 0 |  |  |  |
| OverrideSku | varchar | 50 | 0 |  |  |  |
| OverrideDescription | varchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spUpdateOrderItemOverrideSounds](../../StoredProcedures/WebOrderProcessing/WM.spUpdateOrderItemOverrideSounds.md)

