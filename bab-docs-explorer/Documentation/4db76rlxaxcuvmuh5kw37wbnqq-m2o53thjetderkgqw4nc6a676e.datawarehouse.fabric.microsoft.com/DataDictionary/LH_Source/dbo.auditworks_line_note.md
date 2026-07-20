# dbo.auditworks_line_note

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| line_id | decimal | 5 | 1 |  |  |  |
| note_type | int | 4 | 1 |  |  |  |
| line_note | varchar | 8000 | 1 |  |  |  |
