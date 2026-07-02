# dbo.StoreSalesCheck_Diff

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 0 |  |  |  |
| aw_units | varchar | 20 | 0 |  |  |  |
| store_units | varchar | 20 | 0 |  |  |  |
| diff_units | varchar | 20 | 0 |  |  |  |
| issue | varchar | 20 | 0 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spStoreSalesCheck_EmailAlerts](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_EmailAlerts.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_EmailAlerts_NotifyBusiness](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_EmailAlerts_NotifyBusiness.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_Backup20230417](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_Backup20230417.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_backup20240131](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_backup20240131.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_Bak20230815](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_Bak20230815.md)

