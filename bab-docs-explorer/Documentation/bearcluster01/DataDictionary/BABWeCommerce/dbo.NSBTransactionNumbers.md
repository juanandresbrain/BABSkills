# dbo.NSBTransactionNumbers

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sAppName | varchar | 50 | 0 | YES |  |  |
| iStoreNumber | int | 4 | 0 | YES |  |  |
| iNSBTransactionNumber | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [BABWeCommerce: dbo.spPostProductionService_GetAWTransId](../../StoredProcedures/BABWeCommerce/dbo.spPostProductionService_GetAWTransId.md)
- [BABWeCommerce: dbo.spPostProductionService_GetAWTransId_V2](../../StoredProcedures/BABWeCommerce/dbo.spPostProductionService_GetAWTransId_V2.md)
- [ApplicationResources: POS.spJMC_SAT_Service_GetAWTransId](../../StoredProcedures/ApplicationResources/POS.spJMC_SAT_Service_GetAWTransId.md)

