# WMS.VendorMasterTo3PL

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| city | nvarchar | 60 | 1 |  |  |  |
| vendor_name | nvarchar | 200 | 1 |  |  |  |
| address_name | nvarchar | 200 | 1 |  |  |  |
| port | nvarchar | 200 | 1 |  |  |  |
| address | nvarchar | 200 | 1 |  |  |  |
| province | nvarchar | 200 | 1 |  |  |  |
| country | nvarchar | 200 | 1 |  |  |  |
| phone_number | nvarchar | 200 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeVendorMasterTo3PL](../../StoredProcedures/IntegrationStaging/WMS.spMergeVendorMasterTo3PL.md)

