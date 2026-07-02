# dbo.babw_adyen_merchant

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seqNumber | int | 4 | 1 |  |  |  |
| MerchantAccount | varchar | 80 | 1 |  |  |  |
| lastBatchNum | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spAdyenFileControl](../../StoredProcedures/IntegrationStaging/dbo.spAdyenFileControl.md)

