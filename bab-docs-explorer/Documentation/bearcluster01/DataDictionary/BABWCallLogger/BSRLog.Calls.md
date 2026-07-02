# BSRLog.Calls

**Database:** BABWCallLogger  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| calls_id | int | 4 | 0 |  |  |  |
| agent_id | int | 4 | 1 |  |  |  |
| guestfirstname | varchar | 30 | 1 |  |  |  |
| guestlastname | varchar | 30 | 1 |  |  |  |
| guestemailaddress | varchar | 50 | 1 |  |  |  |
| creationdate | datetime | 8 | 1 |  |  |  |
| category_id | int | 4 | 1 |  |  |  |
| type_id | int | 4 | 1 |  |  |  |
| type_note | varchar | 50 | 1 |  |  |  |
| call_note | varchar | -1 | 1 |  |  |  |
| resolved | bit | 1 | 1 |  |  |  |
| call_rating | int | 4 | 1 |  |  |  |
| survey_received | int | 4 | 1 |  |  |  |

