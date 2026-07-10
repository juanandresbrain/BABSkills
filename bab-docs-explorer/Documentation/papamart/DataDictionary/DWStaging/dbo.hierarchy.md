# dbo.hierarchy

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_id | smallint | 2 | 0 |  |  |  |
| hierarchy_label | nvarchar | 60 | 0 |  |  |  |
| hierarchy_type | tinyint | 1 | 0 |  |  |  |
| alternate_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
