# dbo.Sales_GAAP_RawFromStoreServerPre2023Archive

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| TransactionDatetime | datetime | 8 | 0 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| location_name | varchar | 50 | 1 |  |  |  |
| net_sales | decimal | 17 | 1 |  |  |  |
| entry_date | datetime | 8 | 1 |  |  |  |
| source | varchar | 50 | 1 |  |  |  |
| RTL_TRN_ID | int | 4 | 1 |  |  |  |
| STORE_NO | int | 4 | 1 |  |  |  |
| WORKSTATION_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_NO | varchar | 52 | 1 |  |  |  |
| OPERATOR_NO | int | 4 | 1 |  |  |  |
| RTL_TRN_TYPE_CODE | varchar | 50 | 1 |  |  |  |
| ITEM_NO | varchar | 20 | 1 |  |  |  |
| VOID_FLG | smallint | 2 | 1 |  |  |  |
| WebOrderNumber | varchar | 50 | 1 |  |  |  |
| TransactionID | bigint | 8 | 1 |  |  |  |
| isBOSISorBOPIS | int | 4 | 1 |  |  |  |
| SalesAuditRegisterNumber | int | 4 | 1 |  |  |  |
| SalesAuditTransactionRemark | nvarchar | 2000 | 1 |  |  |  |
| GaapSalesDW | decimal | 17 | 1 |  |  |  |
| isGaapDW | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
