# Accounting.WebFlashGaapStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 10 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 1 |  |  |  |
| isBOSISorBOPIS | int | 4 | 1 |  |  |  |
| TransactionType | varchar | 50 | 1 |  |  |  |
| Tax | numeric | 17 | 1 |  |  |  |
| TransactionAmount | money | 8 | 1 |  |  |  |
| FlashGaapSales | numeric | 17 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| FulfillmentLocation | varchar | 4 | 1 |  |  |  |
| FulfillmentLocationName | varchar | 15 | 1 |  |  |  |
| SalesAuditTransactionID | int | 4 | 1 |  |  |  |
| SalesAuditTransactionNumber | int | 4 | 1 |  |  |  |
| SalesAuditRegisterNumber | smallint | 2 | 1 |  |  |  |
| SalesAuditTransactionRemark | nvarchar | 2000 | 1 |  |  |  |
| GaapSalesDW | numeric | 17 | 1 |  |  |  |
| isGaapDW | tinyint | 1 | 1 |  |  |  |
