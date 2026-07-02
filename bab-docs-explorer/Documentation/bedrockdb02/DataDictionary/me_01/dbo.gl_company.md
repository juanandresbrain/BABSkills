# dbo.gl_company

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_company_id | tinyint | 1 | 0 | YES |  |  |
| gl_company_no | tinyint | 1 | 0 |  |  |  |
| gl_company_name | nvarchar | 120 | 0 |  |  |  |
| gl_destination_type | smallint | 2 | 0 |  |  |  |
| gl_destination | nvarchar | 510 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| export_currency_id | decimal | 9 | 1 |  |  |  |
| default_gl_company_flag | bit | 1 | 0 |  |  |  |

