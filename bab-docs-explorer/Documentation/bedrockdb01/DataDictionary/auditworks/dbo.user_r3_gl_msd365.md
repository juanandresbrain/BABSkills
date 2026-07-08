# dbo.user_r3_gl_msd365

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_company | char | 4 | 0 |  |  |  |
| store_no | char | 10 | 0 |  |  |  |
| calendar_date | char | 8 | 0 |  |  |  |
| JOURNALBATCHNUMBER | nvarchar | 510 | 1 |  |  |  |
| GLCOMPNY | nvarchar | 8 | 0 |  |  |  |
| LINENUMBER | int | 4 | 1 |  |  |  |
| ACCOUNTDISPLAYVALUE | nvarchar | 320 | 1 |  |  |  |
| ACCOUNTTYPE | nvarchar | 12 | 0 |  |  |  |
| DFLTDIMENSIONDISPVALUE | nvarchar | 510 | 1 |  |  |  |
| BANKTRANSTYPE | nvarchar | 510 | 1 |  |  |  |
| PAYMENTREFERENCE | nvarchar | 510 | 1 |  |  |  |
| CREDITAMOUNT | nvarchar | 36 | 0 |  |  |  |
| CURRENCY | nvarchar | 10 | 0 |  |  |  |
| DEBITAMOUNT | nvarchar | 36 | 0 |  |  |  |
| DESCRIPTION | nvarchar | 60 | 1 |  |  |  |
| JOURNALNAME | nvarchar | 12 | 0 |  |  |  |
| TEXT | nvarchar | 100 | 1 |  |  |  |
| TRANSDATE | nvarchar | 20 | 1 |  |  |  |
| VOUCHER | nvarchar | 20 | 1 |  |  |  |
