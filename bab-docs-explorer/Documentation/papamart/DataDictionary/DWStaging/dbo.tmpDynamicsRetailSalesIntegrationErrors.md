# dbo.tmpDynamicsRetailSalesIntegrationErrors

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BABErrorCallStack | nvarchar | 8000 | 1 |  |  |  |
| BABErrorDateTime | datetime | 8 | 1 |  |  |  |
| BABErrorMessage | nvarchar | 8000 | 1 |  |  |  |
| BABErrorReferenceId | nvarchar | 8000 | 1 |  |  |  |
| BABErrorResolved | nvarchar | 510 | 1 |  |  |  |
| BABErrorResolvedBy | nvarchar | 8000 | 1 |  |  |  |
| BABIntegrationDirection | nvarchar | 510 | 1 |  |  |  |
| BABIntegrationEndpoint | nvarchar | 510 | 1 |  |  |  |
| BABIntegrationExternalSystem | nvarchar | 510 | 1 |  |  |  |
| IntegrationErrorsRecId | bigint | 8 | 1 |  |  |  |
