# dbo.plan_version

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_version_id | smallint | 2 | 0 | YES |  |  |
| plan_version_code | nvarchar | 40 | 0 |  |  |  |
| plan_version_label | nvarchar | 120 | 0 |  |  |  |
| current_plan_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.rpt_otb_cost_retail_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_cost_retail_$sp.md)

