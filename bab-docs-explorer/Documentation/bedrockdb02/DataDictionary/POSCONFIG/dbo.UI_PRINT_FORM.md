# dbo.UI_PRINT_FORM

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FORM_ID | int | 4 | 0 | YES |  |  |
| FORM_NAME | nvarchar | 100 | 0 |  |  |  |
| TYPE | char | 4 | 1 |  |  |  |
| NUM_COPIES | int | 4 | 1 |  |  |  |
| PRINT_ROTATION | smallint | 2 | 1 |  |  |  |
| WIDTH | int | 4 | 1 |  |  |  |
| LENGTH | int | 4 | 1 |  |  |  |
| SCRIPT | ntext | 16 | 1 |  |  |  |
| KNIFE_CUT | smallint | 2 | 1 |  |  |  |
| CONTINUATION_HEADER | ntext | 16 | 1 |  |  |  |
| CONTINUATION_FOOTER | ntext | 16 | 1 |  |  |  |
| WRITE_TO_EJ_FLG | smallint | 2 | 1 |  |  |  |
| PRINTING_TIME | smallint | 2 | 1 |  |  |  |
| REPRINT_FLG | smallint | 2 | 1 |  |  |  |
| EMAIL_FLG | smallint | 2 | 1 |  |  |  |
| PRINTER_LOGICAL_NAME | nvarchar | 100 | 1 |  |  |  |

