# dbo.cogs_archive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ACCOUNTDISPLAYVALUE | nvarchar | 70 | 1 |  |  |  |
| ACCOUNTTYPE | varchar | 6 | 0 |  |  |  |
| CREDITAMOUNT | decimal | 17 | 1 |  |  |  |
| CURRENCYCODE | varchar | 3 | 0 |  |  |  |
| DEBITAMOUNT | decimal | 17 | 1 |  |  |  |
| DEFAULTDIMENSIONDISPLAYVALUE | varchar | 1 | 0 |  |  |  |
| DESCRIPTION | varchar | 27 | 0 |  |  |  |
| EXCHANGERATE | numeric | 9 | 1 |  |  |  |
| JOURNALBATCHNUMBER | varchar | 8 | 0 |  |  |  |
| JOURNALNAME | varchar | 2 | 0 |  |  |  |
| OFFSETACCOUNTDISPLAYVALUE | nvarchar | 74 | 1 |  |  |  |
| OFFSETACCOUNTTYPE | varchar | 6 | 0 |  |  |  |
| OFFSETDEFAULTDIMENSIONDISPLAYVALUE | varchar | 1 | 0 |  |  |  |
| OFFSETTEXT | nvarchar | 512 | 1 |  |  |  |
| TEXT | nvarchar | 512 | 1 |  |  |  |
| TRANSDATE | date | 3 | 1 |  |  |  |
| VOUCHER | varchar | 65 | 1 |  |  |  |
| COMPANY | varchar | 4 | 1 |  |  |  |
| OFFSETCOMPANY | varchar | 4 | 1 |  |  |  |

