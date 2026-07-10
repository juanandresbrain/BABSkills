# dbo.WebOrderTrueAttachmentConcatenatedSKUs

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNum | varchar | 10 | 1 |  |  |  |
| OrderDate | date | 3 | 1 |  |  |  |
| SkuString | nvarchar | -1 | 1 |  |  |  |
| DescriptionString | nvarchar | -1 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| KeyStoryString | nvarchar | -1 | 1 |  |  |  |
| MstatString | nvarchar | -1 | 1 |  |  |  |
| Country | varchar | 10 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
