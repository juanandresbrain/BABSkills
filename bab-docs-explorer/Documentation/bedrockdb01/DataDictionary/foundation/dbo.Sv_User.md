# dbo.Sv_User

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | int | 4 | 0 |  |  |  |
| user_name | nvarchar | 60 | 0 |  |  |  |
| user_fullname | nvarchar | 60 | 1 |  |  |  |
| user_level | smallint | 2 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| flags | char | 20 | 0 |  |  |  |
| mail_user_name | nvarchar | 300 | 1 |  |  |  |
| mail_password | varchar | 30 | 1 |  |  |  |
| logo_filename | varchar | 255 | 1 |  |  |  |
| check_mail_interval | smallint | 2 | 0 |  |  |  |
| user_password | varchar | 60 | 1 |  |  |  |
| user_status | smallint | 2 | 1 |  |  |  |
| email_address | nvarchar | 160 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
| pc_language_id | int | 4 | 1 |  |  |  |
