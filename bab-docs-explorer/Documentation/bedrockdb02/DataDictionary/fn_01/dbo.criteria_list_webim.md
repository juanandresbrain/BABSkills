# dbo.criteria_list_webim

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| criteriaformid | T_ID | 16 | 0 |  |  |  |
| sequence_number | smallint | 2 | 1 |  |  |  |
| criterionid | T_ID | 16 | 1 |  |  |  |
| defaultvalue | nvarchar | 510 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.insert_report_criteria_form_assoc_webim_$sp](../../StoredProcedures/fn_01/dbo.insert_report_criteria_form_assoc_webim_$sp.md)
- [fn_01: dbo.insert_report_criteria_form_default_webim_$sp](../../StoredProcedures/fn_01/dbo.insert_report_criteria_form_default_webim_$sp.md)
- [fn_01: dbo.insert_report_item_webim_$sp](../../StoredProcedures/fn_01/dbo.insert_report_item_webim_$sp.md)

