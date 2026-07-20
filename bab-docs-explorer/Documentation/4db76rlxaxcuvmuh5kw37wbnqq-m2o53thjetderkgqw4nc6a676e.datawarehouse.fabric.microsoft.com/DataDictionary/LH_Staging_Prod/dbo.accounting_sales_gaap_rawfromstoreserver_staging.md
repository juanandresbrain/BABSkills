# dbo.accounting_sales_gaap_rawfromstoreserver_staging

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 8000 | 1 |  |  |  |
| location_name | varchar | 8000 | 1 |  |  |  |
| RTL_TRN_ID | int | 4 | 1 |  |  |  |
| STORE_NO | int | 4 | 1 |  |  |  |
| WORKSTATION_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_NO | int | 4 | 1 |  |  |  |
| OPERATOR_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_TYPE_CODE | varchar | 8000 | 1 |  |  |  |
| ITEM_NO | varchar | 8000 | 1 |  |  |  |
| VOID_FLG | int | 4 | 1 |  |  |  |
| TransactionDatetime | datetime2 | 8 | 1 |  |  |  |
| net_sales | decimal | 9 | 1 |  |  |  |
| entry_date | datetime2 | 8 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| WebOrderNumber | varchar | 8000 | 1 |  |  |  |
| TransactionID | decimal | 9 | 1 |  |  |  |
| net_units | int | 4 | 1 |  |  |  |
| tran_units | int | 4 | 1 |  |  |  |
