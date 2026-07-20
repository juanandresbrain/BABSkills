# dbo.accounting_sales_gaap_rawfromstoreserver

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| TransactionDatetime | datetime2 | 8 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| location_name | varchar | 8000 | 1 |  |  |  |
| net_sales | decimal | 9 | 1 |  |  |  |
| entry_date | datetime2 | 8 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| RTL_TRN_ID | int | 4 | 1 |  |  |  |
| STORE_NO | int | 4 | 1 |  |  |  |
| WORKSTATION_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_NO | int | 4 | 1 |  |  |  |
| OPERATOR_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_TYPE_CODE | varchar | 8000 | 1 |  |  |  |
| ITEM_NO | varchar | 8000 | 1 |  |  |  |
| VOID_FLG | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| WebOrderNumber | varchar | 8000 | 1 |  |  |  |
| TransactionID | decimal | 9 | 1 |  |  |  |
| isBOSISorBOPIS | int | 4 | 1 |  |  |  |
| SalesAuditRegisterNumber | int | 4 | 1 |  |  |  |
| SalesAuditTransactionRemark | varchar | 8000 | 1 |  |  |  |
| GaapSalesDW | decimal | 9 | 1 |  |  |  |
| isGaapDW | int | 4 | 1 |  |  |  |
