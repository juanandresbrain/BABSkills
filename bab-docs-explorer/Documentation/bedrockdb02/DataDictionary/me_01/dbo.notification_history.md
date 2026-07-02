# dbo.notification_history

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | int | 4 | 0 | YES |  |  |
| stored_proc_name | varchar | 100 | 1 |  |  |  |
| record_logged_datetime | datetime | 8 | 1 |  |  |  |
| issues_found | varchar | 5 | 1 |  |  |  |
| action_required | varchar | 5 | 1 |  |  |  |
| notification_sent | varchar | 5 | 1 |  |  |  |
| email_type | varchar | 20 | 1 |  |  |  |
| email_to | varchar | 300 | 1 |  |  |  |
| email_cc | varchar | 300 | 1 |  |  |  |
| email_subject | varchar | 150 | 1 |  |  |  |
| comment | varchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailInactiveSkusValidation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailInactiveSkusValidation.md)
- [me_01: dbo.spMerchandisingEmailMerchToStorePriceValidation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMerchToStorePriceValidation.md)
- [me_01: dbo.spMerchandisingEmailShipmentErrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailShipmentErrors.md)
- [me_01: dbo.spMerchandisingReportUpcomingPriceChanges](../../StoredProcedures/me_01/dbo.spMerchandisingReportUpcomingPriceChanges.md)
- [me_01: dbo.spNewStoreSetupCheckMerch](../../StoredProcedures/me_01/dbo.spNewStoreSetupCheckMerch.md)
- [esell: dbo.spES_Aged_Orders_Check](../../StoredProcedures/esell/dbo.spES_Aged_Orders_Check.md)
- [esell: dbo.spES_Rejected_Files_Check](../../StoredProcedures/esell/dbo.spES_Rejected_Files_Check.md)
- [EJ: dbo.spNewStoreSetupCheckWebEJ](../../StoredProcedures/EJ/dbo.spNewStoreSetupCheckWebEJ.md)
- [USICOAL: dbo.spUSICOALTransCountCheck](../../StoredProcedures/USICOAL/dbo.spUSICOALTransCountCheck.md)

