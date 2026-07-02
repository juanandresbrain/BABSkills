# Views: BABWForgetMe

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [vwAdminManualSystemsStatus](dbo.vwAdminManualSystemsStatus.md) | dbo.ActionQuery, dbo.ActionStatus, dbo.ActionTables, dbo.ApplicationDim, dbo.RequestCompletionLog, dbo.TablesToAppsXref |
| dbo | [vwAllRequests](dbo.vwAllRequests.md) | dbo.ActionStatus, dbo.vwRequestsNeedingManualData, dbo.vwRequestsNeedingReview |
| dbo | [vwCurrentForgetMeStatus](dbo.vwCurrentForgetMeStatus.md) | dbo.ActionRequest, dbo.ActionStatus, dbo.ValidationResponse |
| dbo | [vwCurrentForgetMeStatus_V1_1](dbo.vwCurrentForgetMeStatus_V1_1.md) | dbo.ActionRequest, dbo.ActionStatus, dbo.ValidationResponse |
| dbo | [vwForgetMeAllSystemRequests](dbo.vwForgetMeAllSystemRequests.md) | dbo.ActionQuery, dbo.ActionRequest, dbo.ActionStatus, dbo.ActionTables, dbo.ApplicationDim, dbo.RequestCompletionLog, dbo.TablesToAppsXref |
| dbo | [vwForgetMeRequests](dbo.vwForgetMeRequests.md) | dbo.ActionStatus, dbo.vwRequestsNeedingManualData, dbo.vwRequestsNeedingReview |
| dbo | [vwForgetMeSystemRequests](dbo.vwForgetMeSystemRequests.md) | dbo.ActionQuery, dbo.ActionRequest, dbo.ActionStatus, dbo.ActionTables, dbo.ApplicationDim, dbo.Country, dbo.PrivacyPolicy, dbo.RequestCompletionLog, dbo.TablesToAppsXref |
| dbo | [vwOpenRequests](dbo.vwOpenRequests.md) | dbo.ActionStatus, dbo.vwRequestsNeedingManualData, dbo.vwRequestsNeedingReview |
| dbo | [vwOutputData](dbo.vwOutputData.md) | dbo.ActionLog, dbo.ActionQuery, DBO.ActionRequest, dbo.ActionStatus, dbo.ActionTables, dbo.ApplicationDim, dbo.OutputData, dbo.TablesToAppsXref |
| dbo | [vwRequestData](dbo.vwRequestData.md) | dbo.ActionLog, dbo.ActionQuery, dbo.ActionStatus, dbo.ActionTables, dbo.ApplicationDim, dbo.OutputData, dbo.TablesToAppsXref |
| dbo | [vwRequestsNeedingManualData](dbo.vwRequestsNeedingManualData.md) | dbo.ActionQuery, dbo.ActionStatus, dbo.RequestCompletionLog |
| dbo | [vwRequestsNeedingReview](dbo.vwRequestsNeedingReview.md) | dbo.ActionLog |
| dbo | [vwUncheckedRequests](dbo.vwUncheckedRequests.md) | dbo.ActionStatus |
