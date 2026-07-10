# Accounting.Sales_GAAP_RawFromStoreServer_Save20150903

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| TransactionDatetime | datetime | 8 | 0 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| location_name | varchar | 50 | 1 |  |  |  |
| net_sales | decimal | 9 | 1 |  |  |  |
| entry_date | datetime | 8 | 1 |  |  |  |
| source | varchar | 50 | 1 |  |  |  |
| RTL_TRN_ID | int | 4 | 1 |  |  |  |
| STORE_NO | int | 4 | 1 |  |  |  |
| WORKSTATION_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_NO | int | 4 | 1 |  |  |  |
| OPERATOR_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_TYPE_CODE | char | 4 | 1 |  |  |  |
| ITEM_NO | varchar | 20 | 1 |  |  |  |
| VOID_FLG | smallint | 2 | 1 |  |  |  |
