# Accounting.Sales_GAAP_RawFromStoreServer_Staging

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| location_name | varchar | 50 | 1 |  |  |  |
| RTL_TRN_ID | int | 4 | 1 |  |  |  |
| STORE_NO | int | 4 | 1 |  |  |  |
| WORKSTATION_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_NO | int | 4 | 1 |  |  |  |
| OPERATOR_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_TYPE_CODE | char | 50 | 1 |  |  |  |
| ITEM_NO | varchar | 20 | 1 |  |  |  |
| VOID_FLG | smallint | 2 | 1 |  |  |  |
| TransactionDatetime | datetime | 8 | 1 |  |  |  |
| net_sales | decimal | 9 | 1 |  |  |  |
| entry_date | datetime | 8 | 1 |  |  |  |
| source | varchar | 50 | 1 |  |  |  |
| WebOrderNumber | varchar | 50 | 1 |  |  |  |
| TransactionID | numeric | 9 | 1 |  |  |  |
| net_units | int | 4 | 1 |  |  |  |
| tran_units | int | 4 | 1 |  |  |  |
