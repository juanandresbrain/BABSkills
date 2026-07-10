# dbo.HR_StoreforceCustomerMetricsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreNo | int | 4 | 1 |  |  |  |
| StoreCode | int | 4 | 1 |  |  |  |
| StoreCodeRaw | int | 4 | 1 |  |  |  |
| Date | varchar | 30 | 1 |  |  |  |
| TransactionDateRaw | date | 3 | 1 |  |  |  |
| Slot | varchar | 5 | 1 |  |  |  |
| MobileCaptureCount | int | 4 | 1 |  |  |  |
| MobileEmailOptInCount | int | 4 | 1 |  |  |  |
