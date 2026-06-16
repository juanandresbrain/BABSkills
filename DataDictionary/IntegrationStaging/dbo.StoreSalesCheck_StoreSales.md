# dbo.StoreSalesCheck_StoreSales

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| sales_date | datetime | 8 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| sales | int | 4 | 1 |  |  |  |
| datestamp | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_Backup20230417](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_Backup20230417.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_backup20240131](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_backup20240131.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Find_SalesDiff_Bak20230815](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Find_SalesDiff_Bak20230815.md)
- [IntegrationStaging: dbo.spStoreSalesCheck_Insert_WebSales](../../StoredProcedures/IntegrationStaging/dbo.spStoreSalesCheck_Insert_WebSales.md)

