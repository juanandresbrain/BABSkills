# dbo.tblShipmentFilePostSummary

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PROCESS_START | varchar | 30 | 1 |  |  |  |
| WHSE | varchar | 20 | 0 |  |  |  |
| SHIPMENT | varchar | 20 | 0 |  |  |  |
| DISTRO | varchar | 20 | 0 |  |  |  |
| STYLE | varchar | 20 | 0 |  |  |  |
| CARTON | varchar | 20 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| DESTINATION | varchar | 20 | 0 |  |  |  |
| POSTED | varchar | 3 | 0 |  |  |  |
| POSTED_DATE | varchar | 30 | 0 |  |  |  |
| ERROR | varchar | 3 | 0 |  |  |  |
| ERROR_MSG | varchar | 1000 | 0 |  |  |  |
| IMPORT_FILE | varchar | 200 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectShipmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShipmentSummary.md)

