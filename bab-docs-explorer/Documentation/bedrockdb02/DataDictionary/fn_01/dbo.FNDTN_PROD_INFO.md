# dbo.FNDTN_PROD_INFO

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PROD_INFO_ID | int | 4 | 0 | YES |  |  |
| APP_ID | int | 4 | 0 |  |  |  |
| CMPNY_ID | int | 4 | 0 |  |  |  |
| PROD_ID | varchar | 30 | 0 |  |  |  |
| CNCTN_INFO | varchar | 255 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_PROD_INFO_PR](../../StoredProcedures/fn_01/dbo.FNDTN_PROD_INFO_PR.md)

