# dbo.tblRequest

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RequestName | varchar | 80 | 0 |  |  |  |
| RequestID | numeric | 9 | 0 | YES |  |  |
| ReqDescription | varchar | 255 | 0 |  |  |  |
| DateCreated | datetime | 8 | 0 |  |  |  |
| Action | int | 4 | 1 |  |  |  |
| RequestText | text | 16 | 1 |  |  |  |
