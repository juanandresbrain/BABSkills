# dbo.AMM_hs Store Status

**Database:** TXT_Dev  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STORE | nvarchar | 80 | 1 |  |  |  |
| MONTH | nvarchar | 80 | 1 |  |  |  |
| Value | decimal | 9 | 1 |  |  |  |
| USERID | nvarchar | 72 | 1 |  |  |  |
| A_TMSTP | datetime | 8 | 1 |  |  |  |
| A_CHK_FL | int | 4 | 1 |  |  |  |
| A_CHK_MSG | varchar | 1000 | 1 |  |  |  |
| A_DEL_FLAG | varchar | 1 | 1 |  |  |  |
