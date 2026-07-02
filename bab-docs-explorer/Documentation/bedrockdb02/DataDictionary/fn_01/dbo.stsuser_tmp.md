# dbo.stsuser_tmp

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | numeric | 9 | 0 |  |  |  |
| user_name | varchar | 50 | 0 |  |  |  |
| user_fullname | varchar | 50 | 0 |  |  |  |
| user_description | varchar | 255 | 1 |  |  |  |
| user_password | varchar | 50 | 1 |  |  |  |
| user_domain | varchar | 255 | 1 |  |  |  |
| user_lockout | bit | 1 | 0 |  |  |  |
| user_sid | varchar | 255 | 1 |  |  |  |
| user_guid | varchar | 255 | 1 |  |  |  |
| can_encrypt | bit | 1 | 1 |  |  |  |
| can_decrypt | bit | 1 | 1 |  |  |  |
| expiry_date | datetime | 8 | 1 |  |  |  |

