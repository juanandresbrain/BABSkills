# dbo.FNDTN_SCRTY_PROD_INFO

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PROD_INFO_ID | int | 4 | 0 |  |  |  |
| APP_ID | int | 4 | 0 |  |  |  |
| DB_GRP_ID | int | 4 | 0 |  |  |  |
| PROD_ID | varchar | 30 | 0 |  |  |  |
| CNCTN_INFO | varchar | 255 | 0 |  |  |  |
| INSTNC_ID | int | 4 | 1 |  |  |  |
| INSTNC_NAME | nvarchar | 60 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_RPRT_APP_ASSIGN](../../StoredProcedures/fn_01/dbo.FNDTN_RPRT_APP_ASSIGN.md)

