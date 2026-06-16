# dbo.tmpERPItemsMissingDimensionData

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 20 | 1 |  |  |  |
| ProductNumber | varchar | 50 | 1 |  |  |  |
| VendorAccountNumber | nvarchar | 1000 | 1 |  |  |  |
| VendorSearchName | nvarchar | 1000 | 1 |  |  |  |
| HasOrganizationPhoneticName | varchar | 3 | 0 |  |  |  |
| HasVendorCode | varchar | 3 | 0 |  |  |  |
| HasUOM | varchar | 3 | 0 |  |  |  |
| HasHTS | varchar | 3 | 0 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spEmailItemsMissingDimensionData](../../StoredProcedures/IntegrationStaging/ERP.spEmailItemsMissingDimensionData.md)

