# dbo.Sv_Deleted

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| delete_id | int | 4 | 0 | YES |  |  |
| deleted_id | int | 4 | 0 |  |  |  |
| deleted_date | smalldatetime | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| created_date | smalldatetime | 4 | 1 |  |  |  |
| owner_id | int | 4 | 1 |  |  |  |
| modified_date | datetime | 8 | 1 |  |  |  |
| modified_id | int | 4 | 1 |  |  |  |
| last_used_date | smalldatetime | 4 | 1 |  |  |  |
| last_used_id | int | 4 | 1 |  |  |  |
| label_1 | varchar | 30 | 1 |  |  |  |
| label_2 | varchar | 30 | 1 |  |  |  |
| description_1 | varchar | 255 | 1 |  |  |  |
| description_2 | varchar | 255 | 1 |  |  |  |
| data | text | 16 | 1 |  |  |  |
| flags | char | 20 | 1 |  |  |  |
| permission | char | 6 | 1 |  |  |  |
| folder_id | int | 4 | 1 |  |  |  |
| item_sequence | smallint | 2 | 1 |  |  |  |
| output_data | varchar | 100 | 1 |  |  |  |
| crosstab_data | varchar | 100 | 1 |  |  |  |
| graph_data | varchar | 100 | 1 |  |  |  |
| default_data_view | char | 1 | 1 |  |  |  |
| object_code | varchar | 30 | 1 |  |  |  |
| built_by_version | varchar | 11 | 1 |  |  |  |
| version | int | 4 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_CleanDependency](../../StoredProcedures/fn_01/dbo.Sv_CleanDependency.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_CleanDependency](../../StoredProcedures/smartlook_01/dbo.Sv_CleanDependency.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

