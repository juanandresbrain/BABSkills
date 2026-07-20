# dbo.accounting_webflashgaapstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| TransactionDate | datetime2 | 8 | 1 |  |  |  |
| isBOSISorBOPIS | int | 4 | 1 |  |  |  |
| TransactionType | varchar | 8000 | 1 |  |  |  |
| Tax | decimal | 17 | 1 |  |  |  |
| TransactionAmount | decimal | 9 | 1 |  |  |  |
| FlashGaapSales | decimal | 17 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| FulfillmentLocation | varchar | 8000 | 1 |  |  |  |
| FulfillmentLocationName | varchar | 8000 | 1 |  |  |  |
| SalesAuditTransactionID | int | 4 | 1 |  |  |  |
| SalesAuditTransactionNumber | int | 4 | 1 |  |  |  |
| SalesAuditRegisterNumber | int | 4 | 1 |  |  |  |
| SalesAuditTransactionRemark | varchar | 8000 | 1 |  |  |  |
| GaapSalesDW | decimal | 17 | 1 |  |  |  |
| isGaapDW | int | 4 | 1 |  |  |  |
