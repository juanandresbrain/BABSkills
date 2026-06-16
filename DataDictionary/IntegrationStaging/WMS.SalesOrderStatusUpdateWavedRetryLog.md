# WMS.SalesOrderStatusUpdateWavedRetryLog

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveId | varchar | 50 | 0 | YES |  |  |
| ReleasedDateAndTime | datetime | 8 | 0 | YES |  |  |
| RetryCount | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spRetryReleasedOutOfOrderWaves](../../StoredProcedures/IntegrationStaging/WMS.spRetryReleasedOutOfOrderWaves.md)

