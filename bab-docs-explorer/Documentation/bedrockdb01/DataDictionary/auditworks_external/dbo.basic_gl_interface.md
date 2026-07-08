# dbo.basic_gl_interface

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| record_type | char | 2 | 0 |  |  |  |
| journal_entry_description | char | 29 | 0 |  |  |  |
| detail_type_indicator | char | 1 | 0 |  |  |  |
| gl_account_no | char | 14 | 0 |  |  |  |
| amount | numeric | 9 | 0 |  |  |  |
| gl_period_no | char | 2 | 0 |  |  |  |
| period_ending_date | char | 5 | 0 |  |  |  |
| gl_company_no | char | 2 | 0 |  |  |  |
