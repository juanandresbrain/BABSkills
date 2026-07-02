# dbo.uda_input_editor_defn

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| editor_id | T_ID | 16 | 0 | YES |  |  |
| typename | nvarchar | 512 | 0 |  |  |  |
| res_description | nvarchar | 256 | 1 |  |  |  |
| res_name | nvarchar | 100 | 1 |  |  |  |
| data_type | smallint | 2 | 0 |  |  |  |
| assemblyname | nvarchar | 512 | 0 |  |  |  |
| internal | bit | 1 | 1 |  |  |  |

