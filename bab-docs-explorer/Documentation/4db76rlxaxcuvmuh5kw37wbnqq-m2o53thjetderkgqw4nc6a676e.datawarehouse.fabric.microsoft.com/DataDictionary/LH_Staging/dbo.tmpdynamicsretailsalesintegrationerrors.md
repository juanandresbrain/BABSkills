# dbo.tmpdynamicsretailsalesintegrationerrors

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BABErrorCallStack | varchar | 8000 | 1 |  |  |  |
| BABErrorDateTime | datetime2 | 8 | 1 |  |  |  |
| BABErrorMessage | varchar | 8000 | 1 |  |  |  |
| BABErrorReferenceId | varchar | 8000 | 1 |  |  |  |
| BABErrorResolved | varchar | 8000 | 1 |  |  |  |
| BABErrorResolvedBy | varchar | 8000 | 1 |  |  |  |
| BABIntegrationDirection | varchar | 8000 | 1 |  |  |  |
| BABIntegrationEndpoint | varchar | 8000 | 1 |  |  |  |
| BABIntegrationExternalSystem | varchar | 8000 | 1 |  |  |  |
| IntegrationErrorsRecId | bigint | 8 | 1 |  |  |  |
