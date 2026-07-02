# dbo.FNDTN_RPRT_ITEM_CRTRN_DFLT_VAL

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RPRT_ITEM_ID | T_ID | 16 | 0 | YES | YES |  |
| CRTRN_FORM_ID | T_ID | 16 | 0 | YES | YES |  |
| CRTRN_FORM_ID | T_ID | 16 | 0 | YES | YES |  |
| CRTRN_ID | T_ID | 16 | 0 | YES | YES |  |
| DFLT_VAL | varchar | 255 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.insert_report_criteria_form_default_merch_$sp](../../StoredProcedures/fn_01/dbo.insert_report_criteria_form_default_merch_$sp.md)
- [fn_01: dbo.insert_report_criteria_form_default_webim_$sp](../../StoredProcedures/fn_01/dbo.insert_report_criteria_form_default_webim_$sp.md)
- [fn_01: dbo.insert_report_item_merch_$sp](../../StoredProcedures/fn_01/dbo.insert_report_item_merch_$sp.md)
- [fn_01: dbo.insert_report_item_webim_$sp](../../StoredProcedures/fn_01/dbo.insert_report_item_webim_$sp.md)
- [fn_01: dbo.remove_report_item_merch_$sp](../../StoredProcedures/fn_01/dbo.remove_report_item_merch_$sp.md)
- [fn_01: dbo.remove_report_item_webim_$sp](../../StoredProcedures/fn_01/dbo.remove_report_item_webim_$sp.md)

