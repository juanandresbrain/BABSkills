# dbo.ActionStatus

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RecordKey | varchar | 26 | 0 | YES |  |  |
| EmailAddress | varchar | 128 | 0 |  |  |  |
| FirstName | varchar | 64 | 1 |  |  |  |
| LastName | varchar | 64 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| ValidationDate | datetime | 8 | 1 |  |  |  |
| ValidationResponseID | tinyint | 1 | 0 |  | YES |  |
| CompletionDate | datetime | 8 | 1 |  |  |  |
| ActionRequestID | tinyint | 1 | 0 |  | YES |  |
| RecordsFlaggedDate | date | 3 | 1 |  |  |  |
| ForgetMeAdminRecordsFlaggedDate | datetime | 8 | 1 |  |  |  |
| ForgetMeAdminValidationDate | datetime | 8 | 1 |  |  |  |
| Address1 | varchar | 64 | 1 |  |  |  |
| Address2 | varchar | 64 | 1 |  |  |  |
| City | varchar | 64 | 1 |  |  |  |
| State | varchar | 64 | 1 |  |  |  |
| PostalCode | varchar | 16 | 1 |  |  |  |
| PrivacyPolicyID | int | 4 | 1 |  | YES |  |
| CountryID | int | 4 | 1 |  | YES |  |
| PhoneNumber | varchar | 30 | 1 |  |  |  |
| ForgetMeAdminCancelledDate | datetime | 8 | 1 |  |  |  |
| ForgetMeAdminHoldDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWForgetMe_Restore: dbo.spForgetMeNewRequestEmail](../../StoredProcedures/BABWForgetMe_Restore/dbo.spForgetMeNewRequestEmail.md)
- [BABWForgetMe_Restore: dbo.spForgetMeRequestEmail](../../StoredProcedures/BABWForgetMe_Restore/dbo.spForgetMeRequestEmail.md)
- [BABWForgetMe_Restore: dbo.spGetCompleteActionStatusByDate](../../StoredProcedures/BABWForgetMe_Restore/dbo.spGetCompleteActionStatusByDate.md)
- [BABWForgetMe: dbo.spForgetMeNewRequestEmail](../../StoredProcedures/BABWForgetMe/dbo.spForgetMeNewRequestEmail.md)
- [BABWForgetMe: dbo.spForgetMeRequestEmail](../../StoredProcedures/BABWForgetMe/dbo.spForgetMeRequestEmail.md)
- [BABWForgetMe: dbo.spGetCompleteActionStatusByDate](../../StoredProcedures/BABWForgetMe/dbo.spGetCompleteActionStatusByDate.md)
- [BABWForgetMe: dbo.spInsertNewForgetMe](../../StoredProcedures/BABWForgetMe/dbo.spInsertNewForgetMe.md)
- [BABWForgetMe: dbo.spInsertNewForgetMe_v2](../../StoredProcedures/BABWForgetMe/dbo.spInsertNewForgetMe_v2.md)

