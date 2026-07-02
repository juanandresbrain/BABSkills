# dbo.sysdiagrams

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 |  |  |  |
| principal_id | int | 4 | 0 |  |  |  |
| diagram_id | int | 4 | 0 | YES |  |  |
| version | int | 4 | 1 |  |  |  |
| definition | varbinary | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWForgetMe_Restore: dbo.sp_alterdiagram](../../StoredProcedures/BABWForgetMe_Restore/dbo.sp_alterdiagram.md)
- [BABWForgetMe_Restore: dbo.sp_creatediagram](../../StoredProcedures/BABWForgetMe_Restore/dbo.sp_creatediagram.md)
- [BABWForgetMe_Restore: dbo.sp_dropdiagram](../../StoredProcedures/BABWForgetMe_Restore/dbo.sp_dropdiagram.md)
- [BABWForgetMe_Restore: dbo.sp_helpdiagramdefinition](../../StoredProcedures/BABWForgetMe_Restore/dbo.sp_helpdiagramdefinition.md)
- [BABWForgetMe_Restore: dbo.sp_helpdiagrams](../../StoredProcedures/BABWForgetMe_Restore/dbo.sp_helpdiagrams.md)
- [BABWForgetMe_Restore: dbo.sp_renamediagram](../../StoredProcedures/BABWForgetMe_Restore/dbo.sp_renamediagram.md)
- [BABWForgetMe_Restore: dbo.sp_upgraddiagrams](../../StoredProcedures/BABWForgetMe_Restore/dbo.sp_upgraddiagrams.md)
- [WebOrderProcessing: dbo.sp_alterdiagram](../../StoredProcedures/WebOrderProcessing/dbo.sp_alterdiagram.md)
- [WebOrderProcessing: dbo.sp_creatediagram](../../StoredProcedures/WebOrderProcessing/dbo.sp_creatediagram.md)
- [WebOrderProcessing: dbo.sp_dropdiagram](../../StoredProcedures/WebOrderProcessing/dbo.sp_dropdiagram.md)
- [WebOrderProcessing: dbo.sp_helpdiagramdefinition](../../StoredProcedures/WebOrderProcessing/dbo.sp_helpdiagramdefinition.md)
- [WebOrderProcessing: dbo.sp_helpdiagrams](../../StoredProcedures/WebOrderProcessing/dbo.sp_helpdiagrams.md)
- [WebOrderProcessing: dbo.sp_renamediagram](../../StoredProcedures/WebOrderProcessing/dbo.sp_renamediagram.md)
- [WebOrderProcessing: dbo.sp_upgraddiagrams](../../StoredProcedures/WebOrderProcessing/dbo.sp_upgraddiagrams.md)
- [BABWForgetMe: dbo.sp_alterdiagram](../../StoredProcedures/BABWForgetMe/dbo.sp_alterdiagram.md)
- [BABWForgetMe: dbo.sp_creatediagram](../../StoredProcedures/BABWForgetMe/dbo.sp_creatediagram.md)
- [BABWForgetMe: dbo.sp_dropdiagram](../../StoredProcedures/BABWForgetMe/dbo.sp_dropdiagram.md)
- [BABWForgetMe: dbo.sp_helpdiagramdefinition](../../StoredProcedures/BABWForgetMe/dbo.sp_helpdiagramdefinition.md)
- [BABWForgetMe: dbo.sp_helpdiagrams](../../StoredProcedures/BABWForgetMe/dbo.sp_helpdiagrams.md)
- [BABWForgetMe: dbo.sp_renamediagram](../../StoredProcedures/BABWForgetMe/dbo.sp_renamediagram.md)
- [BABWForgetMe: dbo.sp_upgraddiagrams](../../StoredProcedures/BABWForgetMe/dbo.sp_upgraddiagrams.md)
- [BABWeCommerce: dbo.sp_alterdiagram](../../StoredProcedures/BABWeCommerce/dbo.sp_alterdiagram.md)
- [BABWeCommerce: dbo.sp_creatediagram](../../StoredProcedures/BABWeCommerce/dbo.sp_creatediagram.md)
- [BABWeCommerce: dbo.sp_dropdiagram](../../StoredProcedures/BABWeCommerce/dbo.sp_dropdiagram.md)
- [BABWeCommerce: dbo.sp_helpdiagramdefinition](../../StoredProcedures/BABWeCommerce/dbo.sp_helpdiagramdefinition.md)
- [BABWeCommerce: dbo.sp_helpdiagrams](../../StoredProcedures/BABWeCommerce/dbo.sp_helpdiagrams.md)
- [BABWeCommerce: dbo.sp_renamediagram](../../StoredProcedures/BABWeCommerce/dbo.sp_renamediagram.md)
- [BABWeCommerce: dbo.sp_upgraddiagrams](../../StoredProcedures/BABWeCommerce/dbo.sp_upgraddiagrams.md)
- [ApplicationResources: dbo.sp_alterdiagram](../../StoredProcedures/ApplicationResources/dbo.sp_alterdiagram.md)
- [ApplicationResources: dbo.sp_creatediagram](../../StoredProcedures/ApplicationResources/dbo.sp_creatediagram.md)
- [ApplicationResources: dbo.sp_dropdiagram](../../StoredProcedures/ApplicationResources/dbo.sp_dropdiagram.md)
- [ApplicationResources: dbo.sp_helpdiagramdefinition](../../StoredProcedures/ApplicationResources/dbo.sp_helpdiagramdefinition.md)
- [ApplicationResources: dbo.sp_helpdiagrams](../../StoredProcedures/ApplicationResources/dbo.sp_helpdiagrams.md)
- [ApplicationResources: dbo.sp_renamediagram](../../StoredProcedures/ApplicationResources/dbo.sp_renamediagram.md)
- [ApplicationResources: dbo.sp_upgraddiagrams](../../StoredProcedures/ApplicationResources/dbo.sp_upgraddiagrams.md)
- [BABWPartyPlanner_Restore: dbo.sp_alterdiagram](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_alterdiagram.md)
- [BABWPartyPlanner_Restore: dbo.sp_creatediagram](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_creatediagram.md)
- [BABWPartyPlanner_Restore: dbo.sp_dropdiagram](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_dropdiagram.md)
- [BABWPartyPlanner_Restore: dbo.sp_helpdiagramdefinition](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_helpdiagramdefinition.md)
- [BABWPartyPlanner_Restore: dbo.sp_helpdiagrams](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_helpdiagrams.md)
- [BABWPartyPlanner_Restore: dbo.sp_renamediagram](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_renamediagram.md)
- [BABWPartyPlanner_Restore: dbo.sp_upgraddiagrams](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_upgraddiagrams.md)
- [BABWPartyPlanner: dbo.sp_alterdiagram](../../StoredProcedures/BABWPartyPlanner/dbo.sp_alterdiagram.md)
- [BABWPartyPlanner: dbo.sp_creatediagram](../../StoredProcedures/BABWPartyPlanner/dbo.sp_creatediagram.md)
- [BABWPartyPlanner: dbo.sp_dropdiagram](../../StoredProcedures/BABWPartyPlanner/dbo.sp_dropdiagram.md)
- [BABWPartyPlanner: dbo.sp_helpdiagramdefinition](../../StoredProcedures/BABWPartyPlanner/dbo.sp_helpdiagramdefinition.md)
- [BABWPartyPlanner: dbo.sp_helpdiagrams](../../StoredProcedures/BABWPartyPlanner/dbo.sp_helpdiagrams.md)
- [BABWPartyPlanner: dbo.sp_renamediagram](../../StoredProcedures/BABWPartyPlanner/dbo.sp_renamediagram.md)
- [BABWPartyPlanner: dbo.sp_upgraddiagrams](../../StoredProcedures/BABWPartyPlanner/dbo.sp_upgraddiagrams.md)

