# dbo.ServiceTransactionNumbers

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServiceID | int | 4 | 0 | YES | YES |  |
| StoreNumber | int | 4 | 0 | YES |  |  |
| TransactionNumber | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.spPostProductionService_GetTransactionNumber_1_1](../../StoredProcedures/ApplicationResources/dbo.spPostProductionService_GetTransactionNumber_1_1.md)

