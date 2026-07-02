# dbo.DepositLevel

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DepositLevelID | int | 4 | 0 | YES |  |  |
| NumGuests | int | 4 | 0 |  |  |  |
| Amount | decimal | 5 | 0 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetPartyChoicesByStore_V2.md)
- [BABWPartyPlanner: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetPartyChoicesByStore_V2.md)

