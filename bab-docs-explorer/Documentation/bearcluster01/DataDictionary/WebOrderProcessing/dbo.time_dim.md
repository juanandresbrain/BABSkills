# dbo.time_dim

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| time_key | int | 4 | 0 |  |  |  |
| hour | int | 4 | 1 |  |  |  |
| minute | int | 4 | 1 |  |  |  |
| daypart | varchar | 20 | 1 |  |  |  |
| half_hour_id | int | 4 | 1 |  |  |  |
| qtr_hour_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spStoreforceBopis](../../StoredProcedures/WebOrderProcessing/dbo.spStoreforceBopis.md)

