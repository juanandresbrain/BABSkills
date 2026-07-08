# dbo.tblCommandDetails

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CommandDetailsID | int | 4 | 0 | YES |  |  |
| CommandID | int | 4 | 0 |  |  |  |
| DetailType | varchar | 1 | 0 |  |  |  |
| GroupID | decimal | 9 | 1 |  |  |  |
| QueueIDVersion | int | 4 | 1 |  |  |  |
| RemoteID | int | 4 | 1 |  |  |  |
