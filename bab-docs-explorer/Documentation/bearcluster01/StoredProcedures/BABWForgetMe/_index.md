# Stored Procedures: BABWForgetMe

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [sp_alterdiagram](dbo.sp_alterdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_creatediagram](dbo.sp_creatediagram.md) | dbo.sysdiagrams |
| dbo | [sp_dropdiagram](dbo.sp_dropdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagramdefinition](dbo.sp_helpdiagramdefinition.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagrams](dbo.sp_helpdiagrams.md) | dbo.sysdiagrams |
| dbo | [sp_renamediagram](dbo.sp_renamediagram.md) | dbo.sysdiagrams |
| dbo | [sp_upgraddiagrams](dbo.sp_upgraddiagrams.md) | dbo.dtproperties, dbo.sysdiagrams |
| dbo | [spForgetMeNewRequestEmail](dbo.spForgetMeNewRequestEmail.md) | dbo.ActionRequest, dbo.ActionStatus, dbo.ApplicationDim, dbo.sp_send_dbmail, dbo.vwCurrentForgetMeStatus_V1_1 |
| dbo | [spForgetMeRequestEmail](dbo.spForgetMeRequestEmail.md) | dbo.ActionRequest, dbo.ActionStatus, dbo.ApplicationDim, dbo.sp_send_dbmail, dbo.vwCurrentForgetMeStatus |
| dbo | [spGetCompleteActionStatusByDate](dbo.spGetCompleteActionStatusByDate.md) | dbo.ActionRequest, dbo.ActionStatus |
| dbo | [spGetvwOutputData](dbo.spGetvwOutputData.md) | dbo.vwOutputData |
| dbo | [spGetvwOutputData_V1_1](dbo.spGetvwOutputData_V1_1.md) | dbo.vwOutputData |
| dbo | [spInsertNewForgetMe](dbo.spInsertNewForgetMe.md) | dbo.ActionLog, dbo.ActionStatus |
| dbo | [spInsertNewForgetMe_v2](dbo.spInsertNewForgetMe_v2.md) | dbo.ActionLog, dbo.ActionStatus |
