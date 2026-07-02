# dbo.parameter_core

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_core_id | tinyint | 1 | 0 | YES |  |  |
| pack_code_mask | nvarchar | 40 | 0 |  |  |  |
| first_pack_code_no | nvarchar | 40 | 0 |  |  |  |
| last_pack_code_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_pack_code_no | nvarchar | 40 | 1 |  |  |  |
| pack_code_no_rec_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| concept_code_mask | nvarchar | 40 | 0 |  |  |  |
| first_concept_code_no | nvarchar | 40 | 0 |  |  |  |
| last_concept_code_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_concept_code_no | nvarchar | 40 | 1 |  |  |  |
| concept_code_no_rec_flag | bit | 1 | 0 |  |  |  |

