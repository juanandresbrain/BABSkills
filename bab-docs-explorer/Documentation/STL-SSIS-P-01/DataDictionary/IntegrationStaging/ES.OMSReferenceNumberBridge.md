# ES.OMSReferenceNumberBridge

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BridgeID | int | 4 | 0 | YES |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| EnterpriseSellingID | varchar | 20 | 1 |  |  |  |
| ReferenceNumber | varchar | 50 | 1 |  |  |  |
| ReferenceNumberTypeID | int | 4 | 1 |  | YES |  |
| ErrorCount | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ES.spGetEndlessAisleOrdersNotInEsell](../../StoredProcedures/IntegrationStaging/ES.spGetEndlessAisleOrdersNotInEsell.md)
- [IntegrationStaging: ES.spMergeOMSReferenceNumberBridge](../../StoredProcedures/IntegrationStaging/ES.spMergeOMSReferenceNumberBridge.md)

