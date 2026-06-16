# Stored Procedures: DBAUtility

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [CommandExecute](dbo.CommandExecute.md) | dbo.CommandLog |
| dbo | [IndexOptimize](dbo.IndexOptimize.md) | dbo.CommandExecute |
| dbo | [sp_BlitzCache](dbo.sp_BlitzCache.md) | c.exist, c.value, cg.query, cg.value, dbo.b, dbo.bbcp, dbo.p, dbo.s, dbo.sp, fn.exist, fn.value, mg.query, mg.value, mi.query, mi.value, n.exist, n.query, n.value, o.value, query_plan.exist, query_plan.value, relop.exist, relop.value, statement.exist, statement.value, x.exist, x.value |
| dbo | [sp_BlitzFirst](dbo.sp_BlitzFirst.md) | c.value, dbo.fNow, dbo.pNow, dbo.sp_BlitzCache, record.value, sys.dm_db_resource_stats |
| dbo | [spDBA_WhoIsActive](dbo.spDBA_WhoIsActive.md) | agent_node.value, dbo.s, dbo.sysjobs, dbo.sysjobsteps, trans_node.value |
| dbo | [spRPT_SOXAuditReportPopulate](dbo.spRPT_SOXAuditReportPopulate.md) | dbo.tblDBA_SOXReport_GroupMembership, dbo.tblDBA_SOXReport_ServerRolesAndLogins, dbo.xp_logininfo |
| dbo | [spRunJob_StoreSalesCheck](dbo.spRunJob_StoreSalesCheck.md) | dbo.sp_start_job |
| dbo | [spSqlAgentJobStatus](dbo.spSqlAgentJobStatus.md) | dbo.sp_send_dbmail, dbo.sysjobactivity, dbo.sysjobhistory, dbo.sysjobs, dbo.sysjobsteps, dbo.syssessions |
| dbo | [spStopJob_StoreSalesCheck](dbo.spStopJob_StoreSalesCheck.md) | dbo.sp_stop_job |
