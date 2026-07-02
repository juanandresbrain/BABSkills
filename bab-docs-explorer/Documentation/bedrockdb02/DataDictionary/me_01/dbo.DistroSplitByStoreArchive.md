# dbo.DistroSplitByStoreArchive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ArchiveDate | datetime | 8 | 0 |  |  |  |
| Store_num | int | 4 | 1 |  |  |  |
| CartonsPerSplit | int | 4 | 0 |  |  |  |
| NumberOfSplits | decimal | 5 | 0 |  |  |  |
| StoreType | nvarchar | 100 | 0 |  |  |  |
| isSmallStockRoom | bit | 1 | 1 |  |  |  |
| Warehouse_num | int | 4 | 0 |  |  |  |

