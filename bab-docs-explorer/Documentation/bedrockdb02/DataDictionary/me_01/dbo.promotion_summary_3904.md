# dbo.promotion_summary_3904

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Number | nvarchar | 40 | 0 |  |  |  |
| StoreNum | bigint | 8 | 1 |  |  |  |
| Name | nvarchar | 60 | 1 |  |  |  |
| Description | nvarchar | 510 | 1 |  |  |  |
| ScheduleBeginDate | datetime | 8 | 1 |  |  |  |
| ScheduleEndDate | datetime | 8 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| new_price | decimal | 9 | 1 |  |  |  |
| calculation_method | smallint | 2 | 1 |  |  |  |
| calculation_value | decimal | 9 | 1 |  |  |  |

