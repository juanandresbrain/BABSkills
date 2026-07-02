# dbo.distrosplitbystore

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store_num | int | 4 | 1 |  |  |  |
| CartonsPerSplit | int | 4 | 0 |  |  |  |
| NumberOfSplits | decimal | 5 | 0 |  |  |  |
| StoreType | nvarchar | 100 | 0 |  |  |  |
| isSmallStockRoom | bit | 1 | 1 |  |  |  |
| Warehouse_num | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_SelectDistroSplitDetailsByStore](../../StoredProcedures/me_01/dbo.sp_SelectDistroSplitDetailsByStore.md)
- [me_01: dbo.sp_SelectDistroSplitDetailsByStore_rpt](../../StoredProcedures/me_01/dbo.sp_SelectDistroSplitDetailsByStore_rpt.md)
- [me_01: dbo.sp_SelectDynamicsDistroSplitDetailsByStore](../../StoredProcedures/me_01/dbo.sp_SelectDynamicsDistroSplitDetailsByStore.md)
- [me_01: dbo.spDistroSplitSummaryList](../../StoredProcedures/me_01/dbo.spDistroSplitSummaryList.md)
- [me_01: dbo.spMerchandisingToWmDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWmDistroExportNotification.md)

