# ERP.ItemVendorLoadtoD365Stage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FactoryCode | nvarchar | 12 | 1 |  |  |  |
| VendorAccountNumber | nvarchar | 1000 | 1 |  |  |  |
| ITEMNUMBER | nvarchar | 40 | 1 |  |  |  |
| EFFECTIVEDATE | datetime | 8 | 1 |  |  |  |
| VendorProductNumber | nvarchar | 80 | 1 |  |  |  |
| DataAreaID | nvarchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeItemVendorLoadtoD365](../../StoredProcedures/IntegrationStaging/ERP.spMergeItemVendorLoadtoD365.md)

