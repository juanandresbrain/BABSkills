# dbo.Ex_Command

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_id | int | 4 | 0 |  |  |  |
| command_id | int | 4 | 0 |  |  |  |
| command_label1 | varchar | 255 | 1 |  |  |  |
| command_label2 | varchar | 255 | 1 |  |  |  |
| command_type | smallint | 2 | 0 |  |  |  |
| command_text | text | 16 | 0 |  |  |  |
| dependant_commands | varchar | 255 | 1 |  |  |  |
| required_tran_commit | bit | 1 | 0 |  |  |  |
