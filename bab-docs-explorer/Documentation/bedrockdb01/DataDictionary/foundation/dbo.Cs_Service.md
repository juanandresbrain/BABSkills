# dbo.Cs_Service

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| service_id | int | 4 | 0 |  |  |  |
| label | varchar | 30 | 1 |  |  |  |
| file_name | varchar | 30 | 0 |  |  |  |
| allow_multiple_files | smallint | 2 | 0 |  |  |  |
| expect_confirmation | smallint | 2 | 0 |  |  |  |
| contact_info | varchar | 255 | 1 |  |  |  |
