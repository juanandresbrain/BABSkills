# dbo.security_user

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | varchar | 25 | 0 |  |  |  |
| class_id | smallint | 2 | 0 |  |  |  |
| first_name | varchar | 20 | 1 |  |  |  |
| last_name | varchar | 20 | 1 |  |  |  |
| department | tinyint | 1 | 1 |  |  |  |
| phone_extension | int | 4 | 1 |  |  |  |
| exception_edit_access | tinyint | 1 | 0 |  |  |  |
| feature_code | char | 4 | 1 |  |  |  |
| language_id | smallint | 2 | 1 |  |  |  |
| current_exe | varchar | 20 | 1 |  |  |  |
| email_address | varchar | 255 | 1 |  |  |  |
