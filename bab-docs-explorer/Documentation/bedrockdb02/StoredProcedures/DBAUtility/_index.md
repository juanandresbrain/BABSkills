# Stored Procedures: DBAUtility

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [CommandExecute](dbo.CommandExecute.md) | dbo.CommandLog |
| dbo | [CreateBackUpFromJob_DELETE20141203](dbo.CreateBackUpFromJob_DELETE20141203.md) | dbo.sysalerts, dbo.sysjobs, dbo.sysjobschedules, dbo.sysjobsteps, dbo.sysnotifications, dbo.sysoperators, dbo.sysschedules |
| dbo | [DatabaseBackup](dbo.DatabaseBackup.md) | dbo.backupset, dbo.CommandExecute, dbo.log_shipping_primary_databases, dbo.log_shipping_secondary_databases, dbo.xp_fileexist, dbo.xp_instance_regread |
| dbo | [DatabaseIntegrityCheck](dbo.DatabaseIntegrityCheck.md) | dbo.CommandExecute |
| dbo | [IndexOptimize](dbo.IndexOptimize.md) | dbo.CommandExecute |
| dbo | [kk_SP_DeleteBackupHistory](dbo.kk_SP_DeleteBackupHistory.md) | dbo.backupfile, dbo.backupmediafamily, dbo.backupmediaset, dbo.backupset, dbo.restorefile, dbo.restorefilegroup, dbo.restorehistory |
| dbo | [report_running_jobs](dbo.report_running_jobs.md) | dbo.report_job_running, dbo.syscategories, dbo.sysjobs_view, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_AskBrent](dbo.sp_AskBrent.md) | dbo.fNow, dbo.pNow, record.value |
| dbo | [sp_blocker_pss08](dbo.sp_blocker_pss08.md) |  |
| dbo | [sp_checksize](dbo.sp_checksize.md) |  |
| dbo | [sp_CompareDB](dbo.sp_CompareDB.md) |  |
| dbo | [sp_ExecResultSet](dbo.sp_ExecResultSet.md) | mydata.value |
| dbo | [spCapacityPlanning](dbo.spCapacityPlanning.md) | dbo.backupset, dbo.CapacityPlanning |
| dbo | [spDBA_Blitz](dbo.spDBA_Blitz.md) | dbo.backupmediafamily, dbo.backupset, dbo.br, dbo.r, dbo.restorehistory, dbo.sp_send_dbmail, dbo.sysalerts, dbo.sysjobactivity, dbo.sysjobs, dbo.sysjobschedules, dbo.sysjobsteps, dbo.sysoperators, dbo.sysschedules, dbo.tblDBA_SQLBlitzResults |
| dbo | [spDBA_CheckBackups](dbo.spDBA_CheckBackups.md) | dbo.backupset |
| dbo | [spDBA_CommandExecute](dbo.spDBA_CommandExecute.md) | dbo.tblDBA_CommandLog |
| dbo | [spDBA_ConfigurationVariable_PopulateErrorAndAgentLogPath](dbo.spDBA_ConfigurationVariable_PopulateErrorAndAgentLogPath.md) | dbo.sp_get_sqlagent_properties, dbo.tblDBA_ConfigurationVariable, dbo.tblDBA_ConfigurationVariableValue |
| dbo | [spDBA_CPUUtilizationCapture](dbo.spDBA_CPUUtilizationCapture.md) | dbo.sp_send_dbmail, dbo.spDBA_WhoIsActive |
| dbo | [spDBA_DatabaseBackup](dbo.spDBA_DatabaseBackup.md) | dbo.backupset, dbo.fnDBA_DatabaseSelect, dbo.spDBA_CommandExecute, dbo.spDBA_GetListOfFileWithSize, dbo.spDBA_SendEmail, dbo.tblDBA_BackupHistory, dbo.tblDBA_FileSize, dbo.xp_fileexist, dbo.xp_instance_regread, dbo.xp_msver |
| dbo | [spDBA_DatabaseBackup_2000](dbo.spDBA_DatabaseBackup_2000.md) | dbo.backupset, dbo.fnDBA_DatabaseSelect2000, dbo.spDBA_CommandExecute, dbo.spDBA_GetListOfFileWithSize, dbo.spDBA_SendEmail, dbo.tblDBA_BackupHistory |
| dbo | [spDBA_DatabaseIntegrityCheck](dbo.spDBA_DatabaseIntegrityCheck.md) | dbo.fnDBA_DatabaseSelect, dbo.fnDBA_DatabaseSelect2000, dbo.spDBA_CommandExecute, dbo.tblDBA_DatabaseIntegrityRepository |
| dbo | [spDBA_Delete_JobHistory](dbo.spDBA_Delete_JobHistory.md) | dbo.sysjobhistory |
| dbo | [spDBA_DeleteBackupHistory_SQLExpress](dbo.spDBA_DeleteBackupHistory_SQLExpress.md) | dbo.sp_delete_backuphistory |
| dbo | [spDBA_DeleteOldFiles](dbo.spDBA_DeleteOldFiles.md) |  |
| dbo | [spDBA_Diskspace](dbo.spDBA_Diskspace.md) | dbo.tblDBA_DriveHistoryRepository |
| dbo | [spDBA_DisplaySQLMetaData](dbo.spDBA_DisplaySQLMetaData.md) |  |
| dbo | [spDBA_GetListOfFileWithSize](dbo.spDBA_GetListOfFileWithSize.md) | dbo.tblDBA_FileSize |
| dbo | [spDBA_IndexOptimize](dbo.spDBA_IndexOptimize.md) | dbo.fnDBA_DatabaseSelect, dbo.spDBA_CommandExecute, dbo.sysjobs, dbo.sysjobsteps, dbo.tblDBA_IndexMaintenance_LargeTable_Repository |
| dbo | [spDBA_IndexOptimize_IntermediateNodes](dbo.spDBA_IndexOptimize_IntermediateNodes.md) | dbo.fnDBA_DatabaseSelect, dbo.ltr, dbo.spDBA_CommandExecute, dbo.sysjobs, dbo.sysjobsteps, dbo.tblDBA_IndexMaintenance_LargeTable_OverRide, dbo.tblDBA_IndexMaintenance_LargeTable_Repository, dbo.tmpIndexesStatistics |
| dbo | [spDBA_JobStatus](dbo.spDBA_JobStatus.md) | BAB\Poll.JobStatus, dbo.spPOLL_ReloadJobHistoryDataPipeLineSalesPosting |
| dbo | [spDBA_JobStatusCheck](dbo.spDBA_JobStatusCheck.md) | dbo.sysjobhistory, dbo.sysjobs, dbo.sysjobsteps, dbo.tblDBA_JobHistoryRepository |
| dbo | [spDBA_LockInfo](dbo.spDBA_LockInfo.md) | dbo.l, dbo.l1, dbo.spt_values |
| dbo | [spDBA_ObjectVersionLog](dbo.spDBA_ObjectVersionLog.md) | dbo.sysjobs, dbo.tblDBA_ObjectVersionLog |
| dbo | [spDBA_PurgeTmpTables](dbo.spDBA_PurgeTmpTables.md) | dbo.fnDBA_DatabaseSelect, dbo.fnDBA_DatabaseSelect2000 |
| dbo | [spDBA_ReadErrorLog](dbo.spDBA_ReadErrorLog.md) | dbo.sp_cycle_agent_errorlog, dbo.spDBA_ConfigurationVariable_PopulateErrorAndAgentLogPath, dbo.spDBA_GetListOfFileWithSize, dbo.spDBA_SendEmail, dbo.tblDBA_ConfigurationVariable, dbo.tblDBA_ConfigurationVariableValue, dbo.tblDBA_ErrorLogHistoryRepository, dbo.tblDBA_FileSize |
| dbo | [spDBA_RebuildIndexes_TableList_2000](dbo.spDBA_RebuildIndexes_TableList_2000.md) | dbo.INDEX_MAINT_HIST |
| dbo | [spDBA_replDistributorStatusGet](dbo.spDBA_replDistributorStatusGet.md) | dbo.sp_send_dbmail, dbo.sysjobs, dbo.sysjobsteps |
| dbo | [spDBA_replLogReaderStatusGet](dbo.spDBA_replLogReaderStatusGet.md) | dbo.MSlogreader_agents, dbo.MSlogreader_history, dbo.sp_send_dbmail, dbo.sysjobs |
| dbo | [spDBA_SearchObjectsForText](dbo.spDBA_SearchObjectsForText.md) | dbo.mat |
| dbo | [spDBA_SearchThroughAllCode](dbo.spDBA_SearchThroughAllCode.md) |  |
| dbo | [spDBA_SecurityReport](dbo.spDBA_SecurityReport.md) | dbo.fnDBA_DatabaseSelect, dbo.fnDBA_DatabaseSelect2000, dbo.tblDBA_SecurityReport |
| dbo | [spDBA_SecurityReport_DBRoleMembers](dbo.spDBA_SecurityReport_DBRoleMembers.md) | dbo.fnDBA_DatabaseSelect, dbo.fnDBA_DatabaseSelect2000, dbo.tblDBA_SecurityReport_DBRoleMembers |
| dbo | [spDBA_SecurityReport_ServerReadModExec](dbo.spDBA_SecurityReport_ServerReadModExec.md) | dbo.fnDBA_DatabaseSelect, dbo.fnDBA_DatabaseSelect2000, dbo.tblDBA_SecurityReport_ServerReadModExec |
| dbo | [spDBA_SendEmail](dbo.spDBA_SendEmail.md) | dbo.sp_send_dbmail |
| dbo | [spDBA_SendEmail_FixMe](dbo.spDBA_SendEmail_FixMe.md) | dbo.sp_send_dbmail, dbo.usp_delete_old_files |
| dbo | [spDBA_StartAgentJobAndWait](dbo.spDBA_StartAgentJobAndWait.md) | dbo.sp_start_job, dbo.sysjobhistory, dbo.sysjobs |
| dbo | [spDBA_Transfer_BackupHistoryRepository](dbo.spDBA_Transfer_BackupHistoryRepository.md) | dbo.tblDBA_BackupHistory, dbo.tblDBA_BackupHistoryRepository |
| dbo | [spDBA_Transfer_DDLChangesRepository](dbo.spDBA_Transfer_DDLChangesRepository.md) | dbo.tblDBA_DDLChangesLog, dbo.tblDBA_DDLChangesRepository |
| dbo | [spDBA_Transfer_ObjectVersionRepository](dbo.spDBA_Transfer_ObjectVersionRepository.md) | dbo.tblDBA_ObjectVersionLog, dbo.tblDBA_ObjectVersionRepository |
| dbo | [spDBA_WhoIsActive](dbo.spDBA_WhoIsActive.md) | agent_node.value, dbo.s, dbo.sysjobs, dbo.sysjobsteps, trans_node.value |
| dbo | [spDM_MaintainProducts](dbo.spDM_MaintainProducts.md) | dbo.hierarchy_group, dbo.ib_price, dbo.InitCap, dbo.jurisdiction, dbo.merch_group_parent, dbo.sku, dbo.style, dbo.style_color, dbo.style_group, dbo.style_retail, dbo.tblDM_MaintainProducts, dbo.upc |
| dbo | [spDV_ActiveProducts](dbo.spDV_ActiveProducts.md) | dbo.attribute_set, dbo.color, dbo.entity_attribute_set, dbo.entity_custom_property, dbo.hierarchy_group, dbo.sku, dbo.style, dbo.style_color, dbo.style_group, dbo.tblDV_ActiveProducts, dbo.upc |
| dbo | [spEsellEmailAckOrdersNotPickedUp](dbo.spEsellEmailAckOrdersNotPickedUp.md) | dbo.sp_send_dbmail, dbo.vwEsell__pickpack, dbo.vwEsell_OrderCustomerData |
| dbo | [spFindReferencesToTable](dbo.spFindReferencesToTable.md) | dbo.PIIConnections, dbo.sysjobs, dbo.sysjobsteps |
| dbo | [spMerchStyleValidation_GetProductByStyle](dbo.spMerchStyleValidation_GetProductByStyle.md) | dbo.style, dbo.style_description, dbo.style_retail |
| dbo | [spMerchStyleValidation_GetProductForValidationByStyle](dbo.spMerchStyleValidation_GetProductForValidationByStyle.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.style, dbo.style_group |
| dbo | [spMerchStyleValidation_GetProductForValidationByStyle_V1_1](dbo.spMerchStyleValidation_GetProductForValidationByStyle_V1_1.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.style, dbo.style_group |
| dbo | [spMerchStyleValidation_GetProductForValidationByStyle_V1_2](dbo.spMerchStyleValidation_GetProductForValidationByStyle_V1_2.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.style, dbo.style_group |
| dbo | [spMerchStyleValidation_GetStyleBySku](dbo.spMerchStyleValidation_GetStyleBySku.md) | dbo.sku, dbo.style, dbo.style_detail, dbo.upc |
| dbo | [spPFTGetOpenToByRollingCountsAndAttributes](dbo.spPFTGetOpenToByRollingCountsAndAttributes.md) | dbo.hierarchy_group, dbo.hist_oh_style_loc_li, dbo.hist_style_loc_pd, dbo.location, dbo.oo_all_style_loc_pd, dbo.style, dbo.style_parent, dbo.tmpPFTStyleRollingCountsAndAttributes, dbo.view_oh_style_loctype_li, dbo.view_oh_style_loctype_pd, dbo.view_style_attribute_outer, dbo.view_style_cust_prop_outer |
| dbo | [spPLM_GetMerchandingData](dbo.spPLM_GetMerchandingData.md) | dbo.calendar_year, dbo.color, dbo.fnDBA_StringToTable, dbo.hierarchy_group, dbo.ib_activity_date, dbo.jurisdiction, dbo.season, dbo.sku, dbo.style, dbo.style_color, dbo.style_description, dbo.style_group, dbo.style_retail, dbo.style_vendor, dbo.tblPLM_Merchandising, dbo.upc, dbo.user_def_adj_detail, dbo.user_defined_adjustment, dbo.vendor |
| dbo | [spPLM_GetMerchandingData_dev](dbo.spPLM_GetMerchandingData_dev.md) | dbo.calendar_year, dbo.color, dbo.fnDBA_StringToTable, dbo.hierarchy_group, dbo.ib_activity_date, dbo.jurisdiction, dbo.season, dbo.sku, dbo.style, dbo.style_color, dbo.style_description, dbo.style_group, dbo.style_retail, dbo.style_vendor, dbo.tblPLM_Merchandising, dbo.upc, dbo.user_def_adj_detail, dbo.user_defined_adjustment, dbo.vendor |
| dbo | [spPOLL_DisablePipeLineSalesPosting](dbo.spPOLL_DisablePipeLineSalesPosting.md) | dbo.spPOLL_StatusPipeLineSalesPosting, dbo.xp_cmdshell |
| dbo | [spPOLL_EnablePipeLineSalesPosting](dbo.spPOLL_EnablePipeLineSalesPosting.md) | dbo.spPOLL_StatusPipeLineSalesPosting, dbo.xp_cmdshell |
| dbo | [spPOLL_ExecutePipeLineSalesPosting](dbo.spPOLL_ExecutePipeLineSalesPosting.md) | dbo.sp_start_job, dbo.spPOLL_StatusPipeLineSalesPosting |
| dbo | [spPOLL_ReloadJobHistoryDataPipeLineSalesPosting](dbo.spPOLL_ReloadJobHistoryDataPipeLineSalesPosting.md) | dbo.sp_start_job |
| dbo | [spPOLL_StatusPipeLineSalesPosting](dbo.spPOLL_StatusPipeLineSalesPosting.md) | dbo.sysjobhistory, dbo.sysjobs, dbo.xp_cmdshell |
| dbo | [spRPT_SOXAuditReportPopulate](dbo.spRPT_SOXAuditReportPopulate.md) | dbo.tblDBA_SOXReport_GroupMembership, dbo.tblDBA_SOXReport_ServerRolesAndLogins, dbo.xp_logininfo |
| dbo | [spZebraBarcode_GetStyles](dbo.spZebraBarcode_GetStyles.md) | dbo.hierarchy_group, dbo.style, dbo.style_description, dbo.style_group, dbo.style_retail |
| dbo | [spZebraBarcode_GetStylesWithUPC](dbo.spZebraBarcode_GetStylesWithUPC.md) | dbo.hierarchy_group, dbo.sku, dbo.style, dbo.style_description, dbo.style_group, dbo.style_retail, dbo.upc |
| dbo | [usp_diskspace_dave](dbo.usp_diskspace_dave.md) |  |
