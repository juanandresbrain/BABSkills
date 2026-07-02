# dbo.PriceChangeLT_Temp

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BaseID | nvarchar | 10 | 1 |  |  |  |
| StyleCode | nvarchar | 40 | 0 |  |  |  |
| Jurisdiction | varchar | 2 | 1 |  |  |  |
| AVAILB | varchar | 4 | 1 |  |  |  |
| OriginalRetailDecimal | decimal | 9 | 1 |  |  |  |
| CurrentRetailDecimal | decimal | 9 | 1 |  |  |  |
| OriginalRetail1200Decimal | decimal | 9 | 1 |  |  |  |
| StartDate | smalldatetime | 4 | 1 |  |  |  |
| ChangeType | int | 4 | 1 |  |  |  |
| CreateDate | datetime | 8 | 0 |  |  |  |
| UpdateDate | int | 4 | 1 |  |  |  |
| StopDate | smalldatetime | 4 | 1 |  |  |  |

