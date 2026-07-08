# dbo.if_rejection_reassignment

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| reassign_line_object | smallint | 2 | 0 |  |  |  |
| reassign_line_action | tinyint | 1 | 0 |  |  |  |
