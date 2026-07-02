# dbo.SIGNATURES

**Database:** EJ  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TILLNO | int | 4 | 0 | YES |  |  |
| TRANNO | int | 4 | 0 | YES |  |  |
| DATETIME | datetime | 8 | 0 | YES |  |  |
| SEQNO | smallint | 2 | 0 | YES |  |  |
| STORENO | int | 4 | 0 | YES |  |  |
| TRANCAT | char | 3 | 1 |  |  |  |
| CUSTOMER_SIGNATURE | text | 16 | 1 |  |  |  |
| CUSTOMER_SIGNATURE_TOP | int | 4 | 1 |  |  |  |
| CUSTOMER_SIGNATURE_BOTTOM | int | 4 | 1 |  |  |  |
| CUSTOMER_SIGNATURE_LEFT | int | 4 | 1 |  |  |  |
| CUSTOMER_SIGNATURE_RIGHT | int | 4 | 1 |  |  |  |
| CUSTOMER_SIGNATURE_CODE | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [EJ: dbo.spTruncateEJHistory](../../StoredProcedures/EJ/dbo.spTruncateEJHistory.md)

