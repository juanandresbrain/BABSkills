# dbo.imat_batch

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_batch_id | decimal | 9 | 0 | YES |  |  |
| batch_number | nvarchar | 60 | 0 |  |  |  |
| gl_posting_date | smalldatetime | 4 | 0 |  |  |  |
| batch_status | smallint | 2 | 0 |  |  |  |
| entry_mode | smallint | 2 | 1 |  |  |  |
| invoice_quality_control | int | 4 | 1 |  |  |  |
| gross_amount_payable_control | int | 4 | 1 |  |  |  |
| start_entry_datetime | smalldatetime | 4 | 0 |  |  |  |
| end_entry_datetime | smalldatetime | 4 | 0 |  |  |  |
| entry_duration_seconds | int | 4 | 0 |  |  |  |
| edi_control_number | nvarchar | 18 | 1 |  |  |  |
| employee_id | decimal | 9 | 0 |  |  |  |

