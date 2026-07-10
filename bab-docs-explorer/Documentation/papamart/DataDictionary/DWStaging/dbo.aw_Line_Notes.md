# dbo.aw_Line_Notes

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| note_type | smallint | 2 | 0 |  |  |  |
| line_note | nvarchar | 8000 | 1 |  |  |  |
