# dbo.POS_Facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store_Key | int | 4 | 0 |  |  |  |
| Line_Object_Key | int | 4 | 1 |  |  |  |
| Transaction_Date_key | int | 4 | 0 |  |  |  |
| Transaction_Count | int | 4 | 0 |  |  |  |
| Units_Count | int | 4 | 1 |  |  |  |
| Total_Cost | money | 8 | 1 |  |  |  |
| ID | int | 4 | 0 | YES |  |  |
| Processed | datetime | 8 | 1 |  |  |  |
