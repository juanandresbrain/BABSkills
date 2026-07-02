# Stored Procedures: ReportServerBIRPT02

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [AddAlertSubscription](dbo.AddAlertSubscription.md) | dbo.AlertSubscribers |
| dbo | [AddBatchRecord](dbo.AddBatchRecord.md) | dbo.Batch |
| dbo | [AddDataModelDataSource](dbo.AddDataModelDataSource.md) | dbo.DataModelDataSource |
| dbo | [AddDataSet](dbo.AddDataSet.md) | dbo.Catalog, dbo.DataSets, dbo.ExtendEditSessionLifetime, dbo.SecData, dbo.TempDataSets |
| dbo | [AddDataSource](dbo.AddDataSource.md) | dbo.Catalog, dbo.DataSource, dbo.ExtendEditSessionLifetime, dbo.SecData, dbo.TempDataSources |
| dbo | [AddEvent](dbo.AddEvent.md) | dbo.Event |
| dbo | [AddExecutionLogEntry](dbo.AddExecutionLogEntry.md) | dbo.Catalog, dbo.ConfigurationInfo, dbo.ExecutionLogStorage |
| dbo | [AddHistoryRecord](dbo.AddHistoryRecord.md) | dbo.History, dbo.SnapshotData |
| dbo | [AddItemToFavorites](dbo.AddItemToFavorites.md) | dbo.Favorites, dbo.GetUserID |
| dbo | [AddModelPerspective](dbo.AddModelPerspective.md) | dbo.ModelPerspective |
| dbo | [AddPersistedStream](dbo.AddPersistedStream.md) | dbo.PersistedStream, dbo.SessionData |
| dbo | [AddProductInfo](dbo.AddProductInfo.md) | dbo.ProductInfoHistory |
| dbo | [AddReportSchedule](dbo.AddReportSchedule.md) | dbo.ReportSchedule, dbo.Schedule |
| dbo | [AddReportToCache](dbo.AddReportToCache.md) | dbo.CachePolicy, dbo.EnforceCacheLimits, dbo.ExecutionCache, dbo.ReportSchedule, dbo.Schedule, dbo.SnapshotData |
| dbo | [AddRunningJob](dbo.AddRunningJob.md) | dbo.GetUserID, dbo.RunningJobs |
| dbo | [AddSubscriptionToBeingDeleted](dbo.AddSubscriptionToBeingDeleted.md) | dbo.SubscriptionsBeingDeleted |
| dbo | [AnnounceOrGetKey](dbo.AnnounceOrGetKey.md) | dbo.Keys |
| dbo | [ChangeStateOfDataSource](dbo.ChangeStateOfDataSource.md) | dbo.DataSource |
| dbo | [CheckSessionLock](dbo.CheckSessionLock.md) | dbo.SessionLock |
| dbo | [CleanAllHistories](dbo.CleanAllHistories.md) | dbo.Catalog, dbo.History |
| dbo | [CleanBatchRecords](dbo.CleanBatchRecords.md) | dbo.Batch |
| dbo | [CleanBrokenSnapshots](dbo.CleanBrokenSnapshots.md) | dbo.ChunkData, dbo.SnapshotData |
| dbo | [CleanEventRecords](dbo.CleanEventRecords.md) | dbo.Event |
| dbo | [CleanExpiredCache](dbo.CleanExpiredCache.md) | dbo.ExecutionCache, dbo.SnapshotData |
| dbo | [CleanExpiredContentCache](dbo.CleanExpiredContentCache.md) | dbo.ContentCache |
| dbo | [CleanExpiredEditSessions](dbo.CleanExpiredEditSessions.md) | dbo.ExecutionCache, dbo.SessionData, dbo.SnapshotData, dbo.TempCatalog, dbo.TempDataSets, dbo.TempDataSources |
| dbo | [CleanExpiredJobs](dbo.CleanExpiredJobs.md) | dbo.RunningJobs |
| dbo | [CleanExpiredServerParameters](dbo.CleanExpiredServerParameters.md) | dbo.ServerParametersInstance |
| dbo | [CleanExpiredSessions](dbo.CleanExpiredSessions.md) | dbo.l, dbo.PersistedStream, dbo.ps, dbo.s, dbo.SessionData, dbo.SessionLock, dbo.sl, dbo.SN, dbo.SnapshotData |
| dbo | [CleanHistoryForReport](dbo.CleanHistoryForReport.md) | dbo.History |
| dbo | [CleanNotificationRecords](dbo.CleanNotificationRecords.md) | dbo.Notifications |
| dbo | [CleanOrphanedPolicies](dbo.CleanOrphanedPolicies.md) | dbo.Catalog, dbo.ModelItemPolicy, dbo.Policies |
| dbo | [CleanOrphanedSnapshots](dbo.CleanOrphanedSnapshots.md) | dbo.ChunkData, dbo.ChunkSegmentMapping, dbo.Segment, dbo.SegmentedChunk, dbo.SnapshotData |
| dbo | [ClearScheduleConsistancyFlags](dbo.ClearScheduleConsistancyFlags.md) | dbo.Schedule |
| dbo | [ClearSessionSnapshot](dbo.ClearSessionSnapshot.md) | dbo.DereferenceSessionSnapshot, dbo.GetUserID, dbo.SessionData |
| dbo | [CommentBelongsToUser](dbo.CommentBelongsToUser.md) | dbo.Comments, dbo.GetUserID |
| dbo | [CopyChunks](dbo.CopyChunks.md) | dbo.ChunkData, dbo.SegmentedChunk |
| dbo | [CopyChunksOfType](dbo.CopyChunksOfType.md) | dbo.ChunkData, dbo.ChunkSegmentMapping, dbo.Segment, dbo.SegmentedChunk, dbo.SnapshotData |
| dbo | [CreateCacheUpdateNotifications](dbo.CreateCacheUpdateNotifications.md) | dbo.Catalog, dbo.Event, dbo.Notifications, dbo.Subscriptions |
| dbo | [CreateChunkAndGetPointer](dbo.CreateChunkAndGetPointer.md) | dbo.ChunkData |
| dbo | [CreateChunkSegment](dbo.CreateChunkSegment.md) | dbo.ChunkSegmentMapping, dbo.Segment |
| dbo | [CreateDataDrivenNotification](dbo.CreateDataDrivenNotification.md) | dbo.GetUserID, dbo.Notifications, dbo.Subscriptions, dbo.SubscriptionsBeingDeleted |
| dbo | [CreateEditSession](dbo.CreateEditSession.md) | dbo.GetUserID, dbo.SnapshotData, dbo.TempCatalog |
| dbo | [CreateNewActiveSubscription](dbo.CreateNewActiveSubscription.md) | dbo.ActiveSubscriptions |
| dbo | [CreateNewSnapshotVersion](dbo.CreateNewSnapshotVersion.md) | dbo.CopyChunks, dbo.SnapshotData |
| dbo | [CreateObject](dbo.CreateObject.md) | dbo.Catalog, dbo.GetUserID, dbo.SnapshotData |
| dbo | [CreateOrUpdateContentCache](dbo.CreateOrUpdateContentCache.md) | dbo.ContentCache, dbo.ExecutionCache |
| dbo | [CreateRdlChunk](dbo.CreateRdlChunk.md) | dbo.Catalog, dbo.CreateChunkSegment, dbo.CreateSegmentedChunk, dbo.SegmentedChunk |
| dbo | [CreateRole](dbo.CreateRole.md) | dbo.Roles |
| dbo | [CreateSegmentedChunk](dbo.CreateSegmentedChunk.md) | dbo.ChunkData, dbo.SegmentedChunk |
| dbo | [CreateSession](dbo.CreateSession.md) | dbo.GetUserID, dbo.PersistedStream, dbo.SessionData, dbo.SessionLock, dbo.SnapshotData |
| dbo | [CreateSnapShotNotifications](dbo.CreateSnapShotNotifications.md) | dbo.Event, dbo.History, dbo.Notifications, dbo.Subscriptions |
| dbo | [CreateSubscription](dbo.CreateSubscription.md) | dbo.Catalog, dbo.GetUserID, dbo.Subscriptions |
| dbo | [CreateTask](dbo.CreateTask.md) | dbo.GetUserID, dbo.Schedule |
| dbo | [CreateTimeBasedSubscriptionNotification](dbo.CreateTimeBasedSubscriptionNotification.md) | dbo.Event, dbo.Notifications, dbo.Subscriptions |
| dbo | [CreateTimeBasedSubscriptionSchedule](dbo.CreateTimeBasedSubscriptionSchedule.md) | dbo.AddReportSchedule, dbo.Catalog, dbo.CreateTask |
| dbo | [DecreaseTransientSnapshotRefcount](dbo.DecreaseTransientSnapshotRefcount.md) | dbo.SnapshotData |
| dbo | [DeepCopySegment](dbo.DeepCopySegment.md) | dbo.ChunkSegmentMapping, dbo.Segment |
| dbo | [DeleteActiveSubscription](dbo.DeleteActiveSubscription.md) | dbo.ActiveSubscriptions |
| dbo | [DeleteAlertSubscription](dbo.DeleteAlertSubscription.md) | dbo.AlertSubscribers |
| dbo | [DeleteAllHistoryForReport](dbo.DeleteAllHistoryForReport.md) | dbo.Catalog, dbo.History |
| dbo | [DeleteAllModelItemPolicies](dbo.DeleteAllModelItemPolicies.md) | dbo.Catalog, dbo.ModelItemPolicy, dbo.Policies |
| dbo | [DeleteBatchRecords](dbo.DeleteBatchRecords.md) | dbo.Batch |
| dbo | [DeleteComment](dbo.DeleteComment.md) | dbo.Catalog, dbo.Comments |
| dbo | [DeleteDataSets](dbo.DeleteDataSets.md) | dbo.DataSets, dbo.TempDataSets |
| dbo | [DeleteDataSources](dbo.DeleteDataSources.md) | dbo.DataSource, dbo.TempDataSources |
| dbo | [DeleteDrillthroughReports](dbo.DeleteDrillthroughReports.md) | dbo.ModelDrill |
| dbo | [DeleteEncryptedContent](dbo.DeleteEncryptedContent.md) | dbo.Catalog, dbo.ConfigurationInfo, dbo.DataModelDataSource, dbo.DataSource, dbo.EncryptedConfigList, dbo.keys, dbo.Users |
| dbo | [DeleteEvent](dbo.DeleteEvent.md) | dbo.Event |
| dbo | [DeleteExpiredPersistedStreams](dbo.DeleteExpiredPersistedStreams.md) | dbo.PersistedStream |
| dbo | [DeleteHistoriesWithNoPolicy](dbo.DeleteHistoriesWithNoPolicy.md) | dbo.Catalog, dbo.History |
| dbo | [DeleteHistoryRecord](dbo.DeleteHistoryRecord.md) | dbo.History |
| dbo | [DeleteHistoryRecordByHistoryId](dbo.DeleteHistoryRecordByHistoryId.md) | dbo.History |
| dbo | [DeleteKey](dbo.DeleteKey.md) | dbo.keys |
| dbo | [DeleteModelItemPolicy](dbo.DeleteModelItemPolicy.md) | dbo.ModelItemPolicy, dbo.Policies |
| dbo | [DeleteModelPerspectives](dbo.DeleteModelPerspectives.md) | dbo.ModelPerspective |
| dbo | [DeleteNotification](dbo.DeleteNotification.md) | dbo.Notifications |
| dbo | [DeleteObject](dbo.DeleteObject.md) | dbo.Catalog, dbo.CleanOrphanedPolicies, dbo.DataSets, dbo.DataSource, dbo.ExecutionCache, dbo.Favorites, dbo.GetUserID, dbo.History, dbo.ModelDrill, dbo.ModelItemPolicy, dbo.SnapshotData, dbo.TempCatalog, dbo.TempDataSets, dbo.TempDataSources |
| dbo | [DeleteOneChunk](dbo.DeleteOneChunk.md) | dbo.ChunkData, dbo.SegmentedChunk |
| dbo | [DeletePersistedStream](dbo.DeletePersistedStream.md) | dbo.PersistedStream |
| dbo | [DeletePersistedStreams](dbo.DeletePersistedStreams.md) | dbo.PersistedStream |
| dbo | [DeletePolicy](dbo.DeletePolicy.md) | dbo.Catalog, dbo.Policies |
| dbo | [DeleteReportSchedule](dbo.DeleteReportSchedule.md) | dbo.ReportSchedule |
| dbo | [DeleteRole](dbo.DeleteRole.md) | dbo.Roles |
| dbo | [DeleteSnapshotAndChunks](dbo.DeleteSnapshotAndChunks.md) | dbo.ChunkData, dbo.SegmentedChunk, dbo.SnapshotData |
| dbo | [DeleteSubscription](dbo.DeleteSubscription.md) | dbo.RemoveSubscriptionFromBeingDeleted, dbo.Subscriptions |
| dbo | [DeleteTask](dbo.DeleteTask.md) | dbo.Schedule |
| dbo | [DeleteTimeBasedSubscriptionSchedule](dbo.DeleteTimeBasedSubscriptionSchedule.md) | dbo.ReportSchedule, dbo.Subscriptions |
| dbo | [DeliveryRemovedInactivateSubscription](dbo.DeliveryRemovedInactivateSubscription.md) | dbo.Subscriptions |
| dbo | [DereferenceSessionSnapshot](dbo.DereferenceSessionSnapshot.md) | dbo.SessionData, dbo.SnapshotData |
| dbo | [EnforceCacheLimits](dbo.EnforceCacheLimits.md) | dbo.ExecutionCache, dbo.SnapshotData |
| dbo | [ExpireExecutionLogEntries](dbo.ExpireExecutionLogEntries.md) | dbo.ConfigurationInfo, dbo.ExecutionLogStorage |
| dbo | [ExtendEditSessionLifetime](dbo.ExtendEditSessionLifetime.md) | dbo.ConfigurationInfo, dbo.TempCatalog |
| dbo | [FindFavoriteableItemsNonRecursive](dbo.FindFavoriteableItemsNonRecursive.md) | dbo.Catalog, dbo.Favorites, dbo.GetUserIDWithNoCreate, dbo.SecData, dbo.Users |
| dbo | [FindFavoriteableItemsRecursive](dbo.FindFavoriteableItemsRecursive.md) | dbo.Catalog, dbo.Favorites, dbo.GetUserIDWithNoCreate, dbo.SecData, dbo.Users |
| dbo | [FindItemsByDataSet](dbo.FindItemsByDataSet.md) | dbo.Catalog, dbo.DataSets, dbo.SecData, dbo.Users |
| dbo | [FindItemsByDataSource](dbo.FindItemsByDataSource.md) | dbo.Catalog, dbo.DataSource, dbo.SecData, dbo.Users |
| dbo | [FindItemsByDataSourceRecursive](dbo.FindItemsByDataSourceRecursive.md) | dbo.Catalog, dbo.DataSets, dbo.DataSource, dbo.SecData, dbo.Users |
| dbo | [FindItemsToUpdateByDataSet](dbo.FindItemsToUpdateByDataSet.md) | dbo.Catalog, dbo.DataSets, dbo.ReportSchedule |
| dbo | [FindObjectsByLink](dbo.FindObjectsByLink.md) | dbo.Catalog, dbo.SecData, dbo.Users |
| dbo | [FindObjectsNonRecursive](dbo.FindObjectsNonRecursive.md) | dbo.Catalog, dbo.SecData, dbo.Users |
| dbo | [FindObjectsRecursive](dbo.FindObjectsRecursive.md) | dbo.Catalog, dbo.SecData, dbo.Users |
| dbo | [FindParents](dbo.FindParents.md) | dbo.Catalog, dbo.SecData, dbo.Users |
| dbo | [FlushCacheByID](dbo.FlushCacheByID.md) | dbo.ExecutionCache, dbo.SnapshotData |
| dbo | [FlushContentCache](dbo.FlushContentCache.md) | dbo.Catalog, dbo.ContentCache |
| dbo | [FlushReportFromCache](dbo.FlushReportFromCache.md) | dbo.Catalog, dbo.EC, dbo.ExecutionCache, dbo.SN, dbo.SnapshotData |
| dbo | [Get_sqlagent_job_status](dbo.Get_sqlagent_job_status.md) | dbo.sp_verify_job_identifiers, dbo.sysjobs, dbo.xp_sqlagent_enum_jobs |
| dbo | [GetAlertSubscribers](dbo.GetAlertSubscribers.md) | dbo.AlertSubscribers, dbo.UserContactInfo |
| dbo | [GetAlertSubscriptionID](dbo.GetAlertSubscriptionID.md) | dbo.AlertSubscribers |
| dbo | [GetAllConfigurationInfo](dbo.GetAllConfigurationInfo.md) | dbo.ConfigurationInfo |
| dbo | [GetAllFavoriteItems](dbo.GetAllFavoriteItems.md) | dbo.Catalog, dbo.Favorites, dbo.GetUserIDWithNoCreate, dbo.SecData, dbo.Users |
| dbo | [GetAllProperties](dbo.GetAllProperties.md) | dbo.ExtendedCatalog, dbo.GetUserID, dbo.SecData, dbo.Users |
| dbo | [GetAnnouncedKey](dbo.GetAnnouncedKey.md) | dbo.Keys |
| dbo | [GetAReportsReportAction](dbo.GetAReportsReportAction.md) | dbo.Catalog, dbo.ReportSchedule |
| dbo | [GetBatchRecords](dbo.GetBatchRecords.md) | dbo.Batch |
| dbo | [GetCacheOptions](dbo.GetCacheOptions.md) | dbo.CachePolicy, dbo.Catalog, dbo.reportschedule, dbo.Schedule, dbo.Users |
| dbo | [GetCacheSchedule](dbo.GetCacheSchedule.md) | dbo.ReportSchedule, dbo.Schedule, dbo.Users |
| dbo | [GetCatalogItemContent](dbo.GetCatalogItemContent.md) | dbo.Catalog |
| dbo | [GetCatalogItemProperties](dbo.GetCatalogItemProperties.md) | dbo.Catalog, dbo.Users |
| dbo | [GetChildrenBeforeDelete](dbo.GetChildrenBeforeDelete.md) | dbo.Catalog, dbo.SecData |
| dbo | [GetChunkInformation](dbo.GetChunkInformation.md) | dbo.ChunkData |
| dbo | [GetChunkPointerAndLength](dbo.GetChunkPointerAndLength.md) | dbo.ChunkData |
| dbo | [GetCommentByCommentID](dbo.GetCommentByCommentID.md) | dbo.Catalog, dbo.Comments, dbo.Users |
| dbo | [GetCommentsByItemID](dbo.GetCommentsByItemID.md) | dbo.Catalog, dbo.Comments, dbo.Users |
| dbo | [GetCompiledDefinition](dbo.GetCompiledDefinition.md) | dbo.Catalog, dbo.ExtendedCatalog, dbo.GetUserID, dbo.SecData |
| dbo | [GetContentCache](dbo.GetContentCache.md) | dbo.ContentCache |
| dbo | [GetContentCacheDetails](dbo.GetContentCacheDetails.md) | dbo.ContentCache |
| dbo | [GetCurrentProductInfo](dbo.GetCurrentProductInfo.md) | dbo.ProductInfoHistory |
| dbo | [GetDataModelDatasourceForReencryption](dbo.GetDataModelDatasourceForReencryption.md) | dbo.DataModelDataSource |
| dbo | [GetDataModelDataSourcesByItemID](dbo.GetDataModelDataSourcesByItemID.md) | dbo.DataModelDataSource |
| dbo | [GetDataSetForExecution](dbo.GetDataSetForExecution.md) | dbo.CachePolicy, dbo.Catalog, dbo.ExecutionCache, dbo.SnapshotData |
| dbo | [GetDataSets](dbo.GetDataSets.md) | dbo.Catalog, dbo.ExtendedDataSets, dbo.SecData |
| dbo | [GetDataSourceForUpgrade](dbo.GetDataSourceForUpgrade.md) | dbo.DataSource |
| dbo | [GetDatasourceInfoForReencryption](dbo.GetDatasourceInfoForReencryption.md) | dbo.DataSource |
| dbo | [GetDataSources](dbo.GetDataSources.md) | dbo.Catalog, dbo.DataSource, dbo.ExtendedDataSources, dbo.ModelItemPolicy, dbo.SecData |
| dbo | [GetDBVersion](dbo.GetDBVersion.md) | dbo.ServerUpgradeHistory |
| dbo | [GetDefaultEmail](dbo.GetDefaultEmail.md) | dbo.UserContactInfo |
| dbo | [GetDrillthroughReport](dbo.GetDrillthroughReport.md) | dbo.Catalog, dbo.ModelDrill |
| dbo | [GetDrillthroughReports](dbo.GetDrillthroughReports.md) | dbo.Catalog, dbo.ModelDrill |
| dbo | [GetExecutionOptions](dbo.GetExecutionOptions.md) | dbo.Catalog, dbo.ReportSchedule, dbo.Schedule, dbo.Users |
| dbo | [GetFirstPortionPersistedStream](dbo.GetFirstPortionPersistedStream.md) | dbo.PersistedStream |
| dbo | [GetIDPairsByLink](dbo.GetIDPairsByLink.md) | dbo.Catalog |
| dbo | [GetInvalidPolicies](dbo.GetInvalidPolicies.md) | dbo.Catalog, dbo.ModelItemPolicy, dbo.Policies, dbo.PolicyUserRole, dbo.Roles, dbo.SecData |
| dbo | [GetModelDefinition](dbo.GetModelDefinition.md) | dbo.Catalog |
| dbo | [GetModelItemInfo](dbo.GetModelItemInfo.md) | dbo.Catalog, dbo.ModelItemPolicy, dbo.SecData |
| dbo | [GetModelPerspectives](dbo.GetModelPerspectives.md) | dbo.Catalog, dbo.ModelPerspective, dbo.SecData |
| dbo | [GetModelsAndPerspectives](dbo.GetModelsAndPerspectives.md) | dbo.Catalog, dbo.ModelPerspective, dbo.SecData |
| dbo | [GetMyRunningJobs](dbo.GetMyRunningJobs.md) | dbo.RunningJobs, dbo.Users |
| dbo | [GetNameById](dbo.GetNameById.md) | dbo.Catalog |
| dbo | [GetNextPortionPersistedStream](dbo.GetNextPortionPersistedStream.md) | dbo.PersistedStream |
| dbo | [GetObjectContent](dbo.GetObjectContent.md) | dbo.Catalog, dbo.SecData |
| dbo | [GetOneConfigurationInfo](dbo.GetOneConfigurationInfo.md) | dbo.ConfigurationInfo |
| dbo | [GetParameters](dbo.GetParameters.md) | dbo.Catalog, dbo.SecData |
| dbo | [GetPoliciesForRole](dbo.GetPoliciesForRole.md) | dbo.Catalog, dbo.ModelItemPolicy, dbo.Policies, dbo.PolicyUserRole, dbo.Roles, dbo.SecData |
| dbo | [GetPolicy](dbo.GetPolicy.md) | dbo.Catalog, dbo.Policies, dbo.SecData |
| dbo | [GetPolicyRoots](dbo.GetPolicyRoots.md) | dbo.Catalog |
| dbo | [GetPrincipalID](dbo.GetPrincipalID.md) | dbo.Users |
| dbo | [GetReportForExecution](dbo.GetReportForExecution.md) | dbo.CachePolicy, dbo.Catalog, dbo.ExecutionCache, dbo.ExtendedCatalog, dbo.GetUserID, dbo.ReportSchedule, dbo.Schedule, dbo.SecData, dbo.SnapshotData |
| dbo | [GetReportParametersForExecution](dbo.GetReportParametersForExecution.md) | dbo.Catalog, dbo.ExtendedCatalog, dbo.GetUserID, dbo.History, dbo.SecData |
| dbo | [GetRoles](dbo.GetRoles.md) | dbo.Roles |
| dbo | [GetSchedulesReports](dbo.GetSchedulesReports.md) | dbo.Catalog, dbo.ReportSchedule |
| dbo | [GetServerParameters](dbo.GetServerParameters.md) | dbo.ServerParametersInstance |
| dbo | [GetSessionData](dbo.GetSessionData.md) | dbo.CheckSessionLock, dbo.GetUserID, dbo.SessionData, dbo.SnapshotData |
| dbo | [GetSharePointPathsForUpgrade](dbo.GetSharePointPathsForUpgrade.md) | dbo.Catalog |
| dbo | [GetSharePointSchedulePathsForUpgrade](dbo.GetSharePointSchedulePathsForUpgrade.md) | dbo.Schedule |
| dbo | [GetSnapshotChunks](dbo.GetSnapshotChunks.md) | dbo.ChunkData |
| dbo | [GetSnapshotFromHistory](dbo.GetSnapshotFromHistory.md) | dbo.Catalog, dbo.History, dbo.SecData, dbo.SnapshotData |
| dbo | [GetSnapshotPromotedInfo](dbo.GetSnapshotPromotedInfo.md) | dbo.SnapshotData |
| dbo | [GetSnapShotSchedule](dbo.GetSnapShotSchedule.md) | dbo.ReportSchedule, dbo.Schedule, dbo.Users |
| dbo | [GetSubscription](dbo.GetSubscription.md) | dbo.ActiveSubscriptions, dbo.Catalog, dbo.SecData, dbo.Subscriptions, dbo.Users |
| dbo | [GetSubscriptionInfoForReencryption](dbo.GetSubscriptionInfoForReencryption.md) | dbo.Subscriptions |
| dbo | [GetSubscriptionsForUpgrade](dbo.GetSubscriptionsForUpgrade.md) | dbo.Subscriptions |
| dbo | [GetSystemPolicy](dbo.GetSystemPolicy.md) | dbo.Policies, dbo.SecData |
| dbo | [GetTaskProperties](dbo.GetTaskProperties.md) | dbo.Schedule, dbo.Users |
| dbo | [GetTimeBasedSubscriptionReportAction](dbo.GetTimeBasedSubscriptionReportAction.md) | dbo.Catalog, dbo.ReportSchedule |
| dbo | [GetTimeBasedSubscriptionSchedule](dbo.GetTimeBasedSubscriptionSchedule.md) | dbo.ReportSchedule, dbo.Schedule, dbo.Users |
| dbo | [GetUpgradeItems](dbo.GetUpgradeItems.md) | dbo.UpgradeInfo |
| dbo | [GetUserID](dbo.GetUserID.md) | dbo.GetUserIDByName, dbo.GetUserIDBySid |
| dbo | [GetUserIDByName](dbo.GetUserIDByName.md) | dbo.Users |
| dbo | [GetUserIDBySid](dbo.GetUserIDBySid.md) | dbo.Users |
| dbo | [GetUserIDWithNoCreate](dbo.GetUserIDWithNoCreate.md) | dbo.Users |
| dbo | [GetUserServiceToken](dbo.GetUserServiceToken.md) | dbo.GetUserID, dbo.Users |
| dbo | [GetUserServiceTokenForReencryption](dbo.GetUserServiceTokenForReencryption.md) | dbo.Users |
| dbo | [GetUserSettings](dbo.GetUserSettings.md) | dbo.GetUserID, dbo.Users |
| dbo | [IncreaseTransientSnapshotRefcount](dbo.IncreaseTransientSnapshotRefcount.md) | dbo.SnapshotData |
| dbo | [InsertComment](dbo.InsertComment.md) | dbo.Catalog, dbo.Comments, dbo.GetCommentByCommentID, dbo.GetUserID |
| dbo | [InsertUnreferencedSnapshot](dbo.InsertUnreferencedSnapshot.md) | dbo.SnapshotData |
| dbo | [InvalidateSubscription](dbo.InvalidateSubscription.md) | dbo.Subscriptions |
| dbo | [IsFavoriteItem](dbo.IsFavoriteItem.md) | dbo.Favorites, dbo.GetUserIDWithNoCreate |
| dbo | [IsSegmentedChunk](dbo.IsSegmentedChunk.md) | dbo.ChunkData, dbo.SegmentedChunk |
| dbo | [ListHistory](dbo.ListHistory.md) | dbo.ChunkData, dbo.ChunkSegmentMapping, dbo.History, dbo.Segment, dbo.SegmentedChunk |
| dbo | [ListHistorySnapshots](dbo.ListHistorySnapshots.md) | dbo.ChunkData, dbo.ChunkSegmentMapping, dbo.History, dbo.Segment, dbo.SegmentedChunk |
| dbo | [ListInfoForReencryption](dbo.ListInfoForReencryption.md) | dbo.ConfigurationInfo, dbo.DataModelDataSource, dbo.DataSource, dbo.EncryptedConfigList, dbo.Keys, dbo.Subscriptions, dbo.Users |
| dbo | [ListInstallations](dbo.ListInstallations.md) | dbo.Keys |
| dbo | [ListRunningJobs](dbo.ListRunningJobs.md) | dbo.RunningJobs, dbo.Users |
| dbo | [ListScheduledReports](dbo.ListScheduledReports.md) | dbo.Catalog, dbo.ReportSchedule, dbo.Schedule, dbo.SecData, dbo.Subscriptions, dbo.Users |
| dbo | [ListSubscriptionIDs](dbo.ListSubscriptionIDs.md) | dbo.Subscriptions |
| dbo | [ListSubscriptionsUsingDataSource](dbo.ListSubscriptionsUsingDataSource.md) | dbo.ActiveSubscriptions, dbo.Catalog, dbo.DataSource, dbo.SecData, dbo.Subscriptions, dbo.Users |
| dbo | [ListTasks](dbo.ListTasks.md) | dbo.ReportSchedule, dbo.Schedule, dbo.Users |
| dbo | [ListTasksForMaintenance](dbo.ListTasksForMaintenance.md) | dbo.Schedule |
| dbo | [ListUsedDeliveryProviders](dbo.ListUsedDeliveryProviders.md) | dbo.Subscriptions |
| dbo | [LoadForDefinitionCheck](dbo.LoadForDefinitionCheck.md) | dbo.Catalog, dbo.SecData, dbo.SnapshotData |
| dbo | [LoadForRepublishing](dbo.LoadForRepublishing.md) | dbo.Catalog, dbo.SnapshotData |
| dbo | [LockPersistedStream](dbo.LockPersistedStream.md) | dbo.PersistedStream |
| dbo | [LockSnapshotForUpgrade](dbo.LockSnapshotForUpgrade.md) | dbo.ChunkData |
| dbo | [MarkSnapshotAsDependentOnUser](dbo.MarkSnapshotAsDependentOnUser.md) | dbo.SnapshotData |
| dbo | [MigrateExecutionLog](dbo.MigrateExecutionLog.md) | dbo.ExecutionLog_Old, dbo.ExecutionLogStorage |
| dbo | [MoveObject](dbo.MoveObject.md) | dbo.Catalog |
| dbo | [ObjectExists](dbo.ObjectExists.md) | dbo.ExtendedCatalog, dbo.GetUserID, dbo.SecData |
| dbo | [OpenSegmentedChunk](dbo.OpenSegmentedChunk.md) | dbo.ChunkSegmentMapping, dbo.SegmentedChunk |
| dbo | [PollEventsForRSProcess](dbo.PollEventsForRSProcess.md) | dbo.Event |
| dbo | [PromoteSnapshotInfo](dbo.PromoteSnapshotInfo.md) | dbo.SnapshotData |
| dbo | [ReadChunkPortion](dbo.ReadChunkPortion.md) | dbo.ChunkData |
| dbo | [ReadChunkSegment](dbo.ReadChunkSegment.md) | dbo.ChunkSegmentMapping, dbo.Segment |
| dbo | [ReadRoleProperties](dbo.ReadRoleProperties.md) | dbo.Roles |
| dbo | [RebindDataSet](dbo.RebindDataSet.md) | dbo.DataSets |
| dbo | [RebindDataSource](dbo.RebindDataSource.md) | dbo.DataSource |
| dbo | [RemoveItemFromFavorites](dbo.RemoveItemFromFavorites.md) | dbo.Favorites, dbo.GetUserIDWithNoCreate |
| dbo | [RemoveReportFromSession](dbo.RemoveReportFromSession.md) | dbo.DereferenceSessionSnapshot, dbo.GetUserID, dbo.PersistedStream, dbo.SessionData, dbo.SessionLock |
| dbo | [RemoveRunningJob](dbo.RemoveRunningJob.md) | dbo.RunningJobs |
| dbo | [RemoveSegment](dbo.RemoveSegment.md) | dbo.ChunkSegmentMapping, dbo.Segment |
| dbo | [RemoveSegmentedMapping](dbo.RemoveSegmentedMapping.md) | dbo.ChunkSegmentMapping, dbo.SegmentedChunk, dbo.SnapshotData |
| dbo | [RemoveSubscriptionFromBeingDeleted](dbo.RemoveSubscriptionFromBeingDeleted.md) | dbo.SubscriptionsBeingDeleted |
| dbo | [SetAllProperties](dbo.SetAllProperties.md) | dbo.Catalog, dbo.GetUserID, dbo.TempCatalog |
| dbo | [SetCacheLastUsed](dbo.SetCacheLastUsed.md) | dbo.ExecutionCache |
| dbo | [SetCacheOptions](dbo.SetCacheOptions.md) | dbo.CachePolicy, dbo.Catalog, dbo.FlushContentCache, dbo.FlushReportFromCache |
| dbo | [SetConfigurationInfo](dbo.SetConfigurationInfo.md) | dbo.ConfigurationInfo |
| dbo | [SetConfigurationInfoValue](dbo.SetConfigurationInfoValue.md) | dbo.ConfigurationInfo |
| dbo | [SetDefaultEmail](dbo.SetDefaultEmail.md) | dbo.UserContactInfo |
| dbo | [SetDrillthroughReports](dbo.SetDrillthroughReports.md) | dbo.ModelDrill |
| dbo | [SetExecutionOptions](dbo.SetExecutionOptions.md) | dbo.CachePolicy, dbo.Catalog, dbo.FlushReportFromCache, dbo.SnapshotData |
| dbo | [SetHistoryLimit](dbo.SetHistoryLimit.md) | dbo.Catalog |
| dbo | [SetKeysForInstallation](dbo.SetKeysForInstallation.md) | dbo.Keys |
| dbo | [SetLastModified](dbo.SetLastModified.md) | dbo.Catalog, dbo.GetUserID |
| dbo | [SetMachineName](dbo.SetMachineName.md) | dbo.Keys |
| dbo | [SetModelItemPolicy](dbo.SetModelItemPolicy.md) | dbo.ModelItemPolicy, dbo.Policies, dbo.PolicyUserRole, dbo.SecData |
| dbo | [SetNotificationAttempt](dbo.SetNotificationAttempt.md) | dbo.Notifications |
| dbo | [SetObjectContent](dbo.SetObjectContent.md) | dbo.Catalog, dbo.ExtendEditSessionLifetime, dbo.FlushCacheById, dbo.FlushReportFromCache, dbo.SnapshotData, dbo.TempCatalog |
| dbo | [SetParameters](dbo.SetParameters.md) | dbo.Catalog, dbo.FlushReportFromCache |
| dbo | [SetPersistedStreamError](dbo.SetPersistedStreamError.md) | dbo.PersistedStream |
| dbo | [SetPolicy](dbo.SetPolicy.md) | dbo.Catalog, dbo.Policies, dbo.PolicyUserRole, dbo.SecData |
| dbo | [SetReencryptedDataModelDataSource](dbo.SetReencryptedDataModelDataSource.md) | dbo.DataModelDataSource |
| dbo | [SetReencryptedDatasourceInfo](dbo.SetReencryptedDatasourceInfo.md) | dbo.DataSource |
| dbo | [SetReencryptedSubscriptionInfo](dbo.SetReencryptedSubscriptionInfo.md) | dbo.Subscriptions |
| dbo | [SetReencryptedUserServiceToken](dbo.SetReencryptedUserServiceToken.md) | dbo.Users |
| dbo | [SetRoleProperties](dbo.SetRoleProperties.md) | dbo.Roles |
| dbo | [SetRolePropertiesAndInvalidatePolicies](dbo.SetRolePropertiesAndInvalidatePolicies.md) | dbo.Catalog, dbo.PolicyUserRole, dbo.Roles, dbo.SecData, dbo.SetRoleProperties |
| dbo | [SetSessionCredentials](dbo.SetSessionCredentials.md) | dbo.DereferenceSessionSnapshot, dbo.GetUserID, dbo.SessionData |
| dbo | [SetSessionData](dbo.SetSessionData.md) | dbo.DereferenceSessionSnapshot, dbo.GetUserID, dbo.PersistedStream, dbo.SessionData, dbo.SnapshotData |
| dbo | [SetSessionParameters](dbo.SetSessionParameters.md) | dbo.GetUserID, dbo.SessionData |
| dbo | [SetSnapshotChunksVersion](dbo.SetSnapshotChunksVersion.md) | dbo.ChunkData, dbo.SegmentedChunk |
| dbo | [SetSnapshotProcessingFlags](dbo.SetSnapshotProcessingFlags.md) | dbo.SnapshotData |
| dbo | [SetSystemPolicy](dbo.SetSystemPolicy.md) | dbo.Policies, dbo.PolicyUserRole, dbo.SecData |
| dbo | [SetUpgradeItemStatus](dbo.SetUpgradeItemStatus.md) | dbo.UpgradeInfo |
| dbo | [SetUserServiceToken](dbo.SetUserServiceToken.md) | dbo.GetUserID, dbo.Users |
| dbo | [SetUserSettings](dbo.SetUserSettings.md) | dbo.GetUserID, dbo.Users |
| dbo | [ShallowCopyChunk](dbo.ShallowCopyChunk.md) | dbo.ChunkSegmentMapping, dbo.SegmentedChunk |
| dbo | [StoreServerParameters](dbo.StoreServerParameters.md) | dbo.ServerParametersInstance |
| dbo | [TakeEventFromQueue](dbo.TakeEventFromQueue.md) | dbo.Event |
| dbo | [TempChunkExists](dbo.TempChunkExists.md) | dbo.SegmentedChunk |
| dbo | [TryAcquireCleanupLock](dbo.TryAcquireCleanupLock.md) | dbo.CleanupLock |
| dbo | [UpdateActiveSubscription](dbo.UpdateActiveSubscription.md) | dbo.ActiveSubscriptions |
| dbo | [UpdateComment](dbo.UpdateComment.md) | dbo.Comments |
| dbo | [UpdateCompiledDefinition](dbo.UpdateCompiledDefinition.md) | dbo.Catalog, dbo.SnapshotData |
| dbo | [UpdatePolicy](dbo.UpdatePolicy.md) | dbo.SecData |
| dbo | [UpdatePolicyPrincipal](dbo.UpdatePolicyPrincipal.md) | dbo.GetPrincipalID, dbo.PolicyUserRole, dbo.Roles |
| dbo | [UpdatePolicyRole](dbo.UpdatePolicyRole.md) | dbo.PolicyUserRole, dbo.Roles |
| dbo | [UpdatePolicyStatus](dbo.UpdatePolicyStatus.md) | dbo.SecData |
| dbo | [UpdateRunningJob](dbo.UpdateRunningJob.md) | dbo.RunningJobs |
| dbo | [UpdateScheduleNextRunTime](dbo.UpdateScheduleNextRunTime.md) | dbo.Schedule |
| dbo | [UpdateSnapshot](dbo.UpdateSnapshot.md) | dbo.Catalog, dbo.SnapshotData |
| dbo | [UpdateSnapshotPaginationInfo](dbo.UpdateSnapshotPaginationInfo.md) | dbo.SnapshotData |
| dbo | [UpdateSnapshotReferences](dbo.UpdateSnapshotReferences.md) | dbo.Catalog, dbo.ExecutionCache, dbo.History, dbo.SnapshotData |
| dbo | [UpdateSubscription](dbo.UpdateSubscription.md) | dbo.GetUserID, dbo.Subscriptions |
| dbo | [UpdateSubscriptionLastRunInfo](dbo.UpdateSubscriptionLastRunInfo.md) | dbo.Subscriptions |
| dbo | [UpdateSubscriptionResult](dbo.UpdateSubscriptionResult.md) | dbo.SubscriptionResults |
| dbo | [UpdateSubscriptionStatus](dbo.UpdateSubscriptionStatus.md) | dbo.Subscriptions |
| dbo | [UpdateTask](dbo.UpdateTask.md) | dbo.Schedule |
| dbo | [UpdateUsernameFromSID](dbo.UpdateUsernameFromSID.md) | dbo.Users |
| dbo | [UpgradeSharePointPaths](dbo.UpgradeSharePointPaths.md) | dbo.Catalog |
| dbo | [UpgradeSharePointSchedulePaths](dbo.UpgradeSharePointSchedulePaths.md) | dbo.Schedule |
| dbo | [WriteChunkPortion](dbo.WriteChunkPortion.md) | dbo.ChunkData |
| dbo | [WriteChunkSegment](dbo.WriteChunkSegment.md) | dbo.ChunkSegmentMapping, dbo.Segment |
| dbo | [WriteFirstPortionPersistedStream](dbo.WriteFirstPortionPersistedStream.md) | dbo.PersistedStream |
| dbo | [WriteLockSession](dbo.WriteLockSession.md) | dbo.SessionLock |
| dbo | [WriteNextPortionPersistedStream](dbo.WriteNextPortionPersistedStream.md) | dbo.PersistedStream |
