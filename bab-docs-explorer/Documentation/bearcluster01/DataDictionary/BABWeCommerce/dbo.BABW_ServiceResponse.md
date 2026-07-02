# dbo.BABW_ServiceResponse

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ServiceName | varchar | 50 | 0 |  |  |  |
| Value | xml | -1 | 1 |  |  |  |
| CreatedDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWeCommerce: dbo.spBABW_ServiceResponse_Add](../../StoredProcedures/BABWeCommerce/dbo.spBABW_ServiceResponse_Add.md)

