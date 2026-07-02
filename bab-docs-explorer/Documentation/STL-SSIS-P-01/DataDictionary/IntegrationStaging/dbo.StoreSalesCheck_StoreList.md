# dbo.StoreSalesCheck_StoreList

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 0 |  |  |  |
| store_ip | varchar | 20 | 1 |  |  |  |
| store_group | int | 4 | 1 |  |  |  |
| server_name | varchar | 52 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_Backup20230417](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_Backup20230417.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_backup20240131](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_backup20240131.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_Bak20230815](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_Bak20230815.md)

