# dbo.PrivacyRegulation

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PrivacyRegulationID | int | 4 | 0 | YES |  |  |
| PrivacyRegulationKeyword | varchar | 50 | 1 |  |  |  |
| PrivacyRegulationDescription | varchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_InsertNewPrivacyProtection](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_InsertNewPrivacyProtection.md)
- [BABWPartyPlanner: dbo.sp_InsertNewPrivacyProtection](../../StoredProcedures/BABWPartyPlanner/dbo.sp_InsertNewPrivacyProtection.md)

