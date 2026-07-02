# dbo.wrk_rpt_run_no

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_id | smallint | 2 | 0 | YES |  |  |
| table_name | nvarchar | 60 | 1 |  |  |  |
| last_run_no | int | 4 | 0 |  |  |  |
| max_run_no | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_next_run_no_$sp](../../StoredProcedures/me_01/dbo.rpt_get_next_run_no_$sp.md)

