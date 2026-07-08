# dbo.Sv_OutputNote

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| output_id | int | 4 | 0 |  |  |  |
| page_number | int | 4 | 0 |  |  |  |
| note_text | varchar | 255 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| created_date | smalldatetime | 4 | 0 |  |  |  |
| positionX | float | 8 | 0 |  |  |  |
| positionY | float | 8 | 0 |  |  |  |
| note_id | int | 4 | 1 |  |  |  |
