# dbo.imp_ap_plan_po

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ap_plan_style_id | decimal | 9 | 0 | YES |  |  |
| ap_plan_id | decimal | 9 | 0 | YES |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 | YES |  |  |
| po_no | nvarchar | 40 | 0 | YES |  |  |
| external_po_flag | bit | 1 | 0 |  |  |  |
| in_use_id | binary | 16 | 1 |  |  |  |

