# dbo.ld_awtodwprep

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| Date | datetime2 | 8 | 1 |  |  |  |
| aw_units | decimal | 17 | 1 |  |  |  |
| dm_units | int | 4 | 1 |  |  |  |
| aw_sales | decimal | 17 | 1 |  |  |  |
| dm_sales | decimal | 17 | 1 |  |  |  |
| UnitDiff | decimal | 17 | 1 |  |  |  |
| UnitPctDiff | decimal | 17 | 1 |  |  |  |
| SalesDiff | decimal | 17 | 1 |  |  |  |
| SalesPctDiff | decimal | 17 | 1 |  |  |  |
