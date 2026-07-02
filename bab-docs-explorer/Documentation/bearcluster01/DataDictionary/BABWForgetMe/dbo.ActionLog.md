# dbo.ActionLog

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogKey | bigint | 8 | 0 | YES |  |  |
| RecordKey | varchar | 26 | 0 |  | YES |  |
| ActionTableKey | int | 4 | 0 |  | YES |  |
| ATKeyValue | varchar | 250 | 1 |  |  |  |
| ActionDate | datetime | 8 | 0 |  |  |  |
| AQKey | int | 4 | 0 |  |  |  |
| RemoveData | bit | 1 | 1 |  |  |  |
| RemoveDate | date | 3 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWForgetMe: dbo.spInsertNewForgetMe](../../StoredProcedures/BABWForgetMe/dbo.spInsertNewForgetMe.md)
- [BABWForgetMe: dbo.spInsertNewForgetMe_v2](../../StoredProcedures/BABWForgetMe/dbo.spInsertNewForgetMe_v2.md)

