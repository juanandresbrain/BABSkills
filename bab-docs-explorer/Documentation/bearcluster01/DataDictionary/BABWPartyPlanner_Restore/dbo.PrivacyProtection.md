# dbo.PrivacyProtection

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PrivacyProtectionID | int | 4 | 0 | YES |  |  |
| EventID | int | 4 | 0 |  |  |  |
| PrivacyPolicyRead | bit | 1 | 1 |  |  |  |
| PrivacyPolicyReadDate | datetime | 8 | 1 |  |  |  |
| PrivacyRegulationID | int | 4 | 0 |  |  |  |
| PrivacyRegulationRead | bit | 1 | 1 |  |  |  |
| PrivacyRegulationReadDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_InsertNewPrivacyProtection](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_InsertNewPrivacyProtection.md)
- [BABWPartyPlanner: dbo.sp_InsertNewPrivacyProtection](../../StoredProcedures/BABWPartyPlanner/dbo.sp_InsertNewPrivacyProtection.md)

