# dbo.card_identification

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seq_id | numeric | 9 | 0 | YES |  |  |
| account_no_length | tinyint | 1 | 0 |  |  |  |
| from_account_no | numeric | 13 | 0 |  |  |  |
| to_account_no | numeric | 13 | 0 |  |  |  |
| card_type | nchar | 2 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
