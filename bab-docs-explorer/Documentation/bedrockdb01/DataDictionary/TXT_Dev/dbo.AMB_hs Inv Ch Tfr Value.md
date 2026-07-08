# dbo.AMB_hs Inv Ch Tfr Value

**Database:** TXT_Dev  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WEEK | nvarchar | 80 | 0 |  |  |  |
| STORE | nvarchar | 80 | 0 |  |  |  |
| STYLE COLOR | nvarchar | 80 | 0 |  |  |  |
| Value | decimal | 9 | 0 |  |  |  |
| USERID | nvarchar | 72 | 1 |  |  |  |
| A_TMSTP | datetime | 8 | 1 |  |  |  |
| A_CHK_FL | int | 4 | 1 |  |  |  |
| A_CHK_MSG | varchar | 1000 | 1 |  |  |  |
| A_DEL_FLAG | varchar | 1 | 1 |  |  |  |
