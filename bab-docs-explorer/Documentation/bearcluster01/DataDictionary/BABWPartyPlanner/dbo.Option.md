# dbo.Option

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OptionID | int | 4 | 0 | YES |  |  |
| OptionName | varchar | 128 | 0 |  |  |  |
| OptionCategoryID | int | 4 | 1 |  | YES |  |
| OptionStartDate | datetime | 8 | 1 |  |  |  |
| OptionEndDate | datetime | 8 | 1 |  |  |  |
| OptionDesc | varchar | 256 | 1 |  |  |  |
| DefaultIncluded | bit | 1 | 1 |  |  |  |
| DefaultCost | decimal | 5 | 1 |  |  |  |
| CostPer | varchar | 10 | 1 |  |  |  |
| OrderBy | int | 4 | 1 |  |  |  |
| Enabled | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetPartyChoicesByStore_V2.md)
- [BABWPartyPlanner: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetPartyChoicesByStore_V2.md)

