# dbo.uda_data_retr_defn

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| data_retriever_id | T_ID | 16 | 0 | YES |  |  |
| name | nvarchar | 510 | 0 |  |  |  |
| res_description | nvarchar | 510 | 0 |  |  |  |
| retriever_type | nvarchar | -1 | 0 |  |  |  |
| data_type | int | 4 | 0 |  |  |  |
| category_id | smallint | 2 | 1 |  | YES |  |

