# BSRLog.Agents

**Database:** BABWCallLogger  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| agent_id | int | 4 | 0 |  |  |  |
| firstname | varchar | 30 | 1 |  |  |  |
| lastname | varchar | 30 | 1 |  |  |  |
| emailaddress | varchar | 50 | 0 |  |  |  |
| username | varchar | 30 | 0 |  |  |  |
| userpass | char | 40 | 1 |  |  |  |
| salt | char | 4 | 1 |  |  |  |
| accesslevel | smallint | 2 | 1 |  |  |  |
| disabled | bit | 1 | 1 |  |  |  |
| creationdate | datetime | 8 | 1 |  |  |  |
| country_code | nvarchar | 400 | 1 |  |  |  |
| locale | char | 5 | 1 |  |  |  |

