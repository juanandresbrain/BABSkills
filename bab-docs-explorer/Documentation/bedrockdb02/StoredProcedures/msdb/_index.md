# Stored Procedures: msdb

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [sp_add_alert](dbo.sp_add_alert.md) | dbo.sp_add_alert_internal |
| dbo | [sp_add_alert_internal](dbo.sp_add_alert_internal.md) | dbo.sp_is_sqlagent_starting, dbo.sp_sqlagent_notify, dbo.sp_verify_alert, dbo.sysalerts, dbo.syscategories |
| dbo | [sp_add_category](dbo.sp_add_category.md) | dbo.sp_verify_category, dbo.syscategories |
| dbo | [sp_add_job](dbo.sp_add_job.md) | dbo.sp_verify_category_identifiers, dbo.sp_verify_job, dbo.sysjobs, dbo.sysoriginatingservers_view |
| dbo | [sp_add_jobschedule](dbo.sp_add_jobschedule.md) | dbo.sp_add_schedule, dbo.sp_attach_schedule, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.SQLAGENT_SUSER_SNAME, dbo.sysjobs |
| dbo | [sp_add_jobserver](dbo.sp_add_jobserver.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_has_server_access, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.SQLAGENT_SUSER_SNAME, dbo.syscategories, dbo.sysjobs, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_add_jobstep](dbo.sp_add_jobstep.md) | dbo.sp_add_jobstep_internal |
| dbo | [sp_add_jobstep_internal](dbo.sp_add_jobstep_internal.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sp_verify_jobstep, dbo.sp_verify_proxy_identifiers, dbo.sysjobs, dbo.sysjobservers, dbo.sysjobsteps |
| dbo | [sp_add_log_shipping_monitor_jobs](dbo.sp_add_log_shipping_monitor_jobs.md) | dbo.sp_add_job, dbo.sp_add_jobschedule, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sysjobs |
| dbo | [sp_add_log_shipping_primary](dbo.sp_add_log_shipping_primary.md) | dbo.log_shipping_primaries, dbo.sp_add_log_shipping_monitor_jobs |
| dbo | [sp_add_log_shipping_secondary](dbo.sp_add_log_shipping_secondary.md) | dbo.log_shipping_primaries, dbo.log_shipping_secondaries |
| dbo | [sp_add_maintenance_plan](dbo.sp_add_maintenance_plan.md) | dbo.sysdbmaintplans |
| dbo | [sp_add_maintenance_plan_db](dbo.sp_add_maintenance_plan_db.md) | dbo.sysdbmaintplan_databases, dbo.sysdbmaintplans |
| dbo | [sp_add_maintenance_plan_job](dbo.sp_add_maintenance_plan_job.md) | dbo.sysdbmaintplan_jobs, dbo.sysdbmaintplans, dbo.sysjobs, dbo.sysjobsteps |
| dbo | [sp_add_notification](dbo.sp_add_notification.md) | dbo.sp_sqlagent_notify, dbo.sp_verify_notification, dbo.sysalerts, dbo.sysnotifications |
| dbo | [sp_add_operator](dbo.sp_add_operator.md) | dbo.sp_verify_operator, dbo.syscategories, dbo.sysoperators |
| dbo | [sp_add_proxy](dbo.sp_add_proxy.md) | dbo.sp_verify_credential_identifiers, dbo.sp_verify_proxy, dbo.sysproxies |
| dbo | [sp_add_schedule](dbo.sp_add_schedule.md) | dbo.sp_verify_schedule, dbo.SQLAGENT_SUSER_SID, dbo.sysoriginatingservers_view, dbo.sysschedules |
| dbo | [sp_add_targetservergroup](dbo.sp_add_targetservergroup.md) | dbo.systargetservergroups |
| dbo | [sp_add_targetsvrgrp_member](dbo.sp_add_targetsvrgrp_member.md) | dbo.systargetservergroupmembers, dbo.systargetservergroups, dbo.systargetservers |
| dbo | [sp_addtask](dbo.sp_addtask.md) | dbo.MSdistpublishers, dbo.sp_add_job, dbo.sp_add_jobschedule, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_start_job, dbo.syscategories, dbo.sysjobsteps, dbo.systaskids |
| dbo | [sp_apply_job_to_targets](dbo.sp_apply_job_to_targets.md) | dbo.sp_add_jobserver, dbo.sp_delete_jobserver, dbo.sp_verify_job_identifiers, dbo.sysjobservers, dbo.systargetservergroupmembers, dbo.systargetservergroups, dbo.systargetservers |
| dbo | [sp_attach_schedule](dbo.sp_attach_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysmaintplan_subplans |
| dbo | [sp_change_monitor_role](dbo.sp_change_monitor_role.md) | dbo.log_shipping_primaries, dbo.log_shipping_secondaries |
| dbo | [sp_check_for_owned_jobs](dbo.sp_check_for_owned_jobs.md) |  |
| dbo | [sp_check_for_owned_jobsteps](dbo.sp_check_for_owned_jobsteps.md) | dbo.sysjobs_view, dbo.sysjobsteps |
| dbo | [sp_clear_dbmaintplan_by_db](dbo.sp_clear_dbmaintplan_by_db.md) | dbo.sp_delete_job, dbo.sysdbmaintplan_databases, dbo.sysdbmaintplan_history, dbo.sysdbmaintplan_jobs, dbo.sysdbmaintplans |
| dbo | [sp_convert_jobid_to_char](dbo.sp_convert_jobid_to_char.md) |  |
| dbo | [sp_create_log_shipping_monitor_account](dbo.sp_create_log_shipping_monitor_account.md) |  |
| dbo | [sp_cycle_agent_errorlog](dbo.sp_cycle_agent_errorlog.md) | dbo.sp_sqlagent_notify |
| dbo | [sp_delete_alert](dbo.sp_delete_alert.md) | dbo.sp_is_sqlagent_starting, dbo.sp_sqlagent_notify, dbo.sysalerts, dbo.sysnotifications |
| dbo | [sp_delete_all_msx_jobs](dbo.sp_delete_all_msx_jobs.md) | dbo.sp_delete_job_references, dbo.sysjobhistory, dbo.sysjobs, dbo.sysjobs_view, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoriginatingservers_view, dbo.sysschedules |
| dbo | [sp_delete_backuphistory](dbo.sp_delete_backuphistory.md) | dbo.backupfile, dbo.backupfilegroup, dbo.backupmediafamily, dbo.backupmediaset, dbo.backupset, dbo.restorefile, dbo.restorefilegroup, dbo.restorehistory |
| dbo | [sp_delete_category](dbo.sp_delete_category.md) | dbo.sp_verify_category, dbo.sysalerts, dbo.syscategories, dbo.sysjobs, dbo.sysoperators |
| dbo | [sp_delete_database_backuphistory](dbo.sp_delete_database_backuphistory.md) | dbo.backupfile, dbo.backupfilegroup, dbo.backupmediafamily, dbo.backupmediaset, dbo.backupset, dbo.restorefile, dbo.restorefilegroup, dbo.restorehistory |
| dbo | [sp_delete_job](dbo.sp_delete_job.md) | dbo.sp_delete_all_msx_jobs, dbo.sp_delete_job_references, dbo.sp_post_msx_operation, dbo.sp_verify_job_identifiers, dbo.sysdownloadlist, dbo.sysjobhistory, dbo.sysjobs, dbo.sysjobs_view, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysschedules, dbo.xp_getnetname, dbo.xp_instance_regread, dbo.xp_sqlagent_notify |
| dbo | [sp_delete_job_references](dbo.sp_delete_job_references.md) | dbo.sp_maintplan_delete_subplan, dbo.sp_sqlagent_notify, dbo.sp_ssis_deletepackage, dbo.sp_update_alert, dbo.sysalerts, dbo.sysdbmaintplan_jobs, dbo.sysjobs_view, dbo.sysmaintplan_plans, dbo.sysmaintplan_subplans, dbo.systaskids |
| dbo | [sp_delete_jobschedule](dbo.sp_delete_jobschedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sysjobs, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysoriginatingservers_view, dbo.sysschedules, dbo.sysschedules_localserver_view |
| dbo | [sp_delete_jobserver](dbo.sp_delete_jobserver.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sysjobservers, dbo.systargetservers, dbo.xp_getnetname |
| dbo | [sp_delete_jobstep](dbo.sp_delete_jobstep.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sysjobs, dbo.sysjobservers, dbo.sysjobsteps |
| dbo | [sp_delete_jobsteplog](dbo.sp_delete_jobsteplog.md) | dbo.sp_verify_job_identifiers, dbo.sysjobs_view, dbo.sysjobsteps, dbo.sysjobstepslogs |
| dbo | [sp_delete_log_shipping_monitor_info](dbo.sp_delete_log_shipping_monitor_info.md) | dbo.log_shipping_primaries, dbo.log_shipping_secondaries |
| dbo | [sp_delete_log_shipping_monitor_jobs](dbo.sp_delete_log_shipping_monitor_jobs.md) | dbo.sp_delete_job, dbo.sysjobs |
| dbo | [sp_delete_log_shipping_primary](dbo.sp_delete_log_shipping_primary.md) | dbo.log_shipping_primaries, dbo.log_shipping_secondaries, dbo.sp_delete_log_shipping_monitor_jobs |
| dbo | [sp_delete_log_shipping_secondary](dbo.sp_delete_log_shipping_secondary.md) | dbo.log_shipping_secondaries |
| dbo | [sp_delete_maintenance_plan](dbo.sp_delete_maintenance_plan.md) | dbo.sysdbmaintplan_databases, dbo.sysdbmaintplan_jobs, dbo.sysdbmaintplans |
| dbo | [sp_delete_maintenance_plan_db](dbo.sp_delete_maintenance_plan_db.md) | dbo.sysdbmaintplan_databases |
| dbo | [sp_delete_maintenance_plan_job](dbo.sp_delete_maintenance_plan_job.md) | dbo.sysdbmaintplan_jobs |
| dbo | [sp_delete_notification](dbo.sp_delete_notification.md) | dbo.sp_sqlagent_notify, dbo.sp_verify_notification, dbo.sysalerts, dbo.sysnotifications |
| dbo | [sp_delete_operator](dbo.sp_delete_operator.md) | dbo.sysjobs, dbo.sysnotifications, dbo.sysoperators, dbo.systargetservers, dbo.xp_instance_regread |
| dbo | [sp_delete_proxy](dbo.sp_delete_proxy.md) | dbo.sp_verify_proxy_identifiers, dbo.sysjobsteps, dbo.sysproxies, dbo.sysproxylogin, dbo.sysproxysubsystem |
| dbo | [sp_delete_schedule](dbo.sp_delete_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysschedules |
| dbo | [sp_delete_targetserver](dbo.sp_delete_targetserver.md) | dbo.sp_post_msx_operation, dbo.sysdownloadlist, dbo.sysjobservers, dbo.systargetservergroupmembers, dbo.systargetservers |
| dbo | [sp_delete_targetservergroup](dbo.sp_delete_targetservergroup.md) | dbo.systargetservergroupmembers, dbo.systargetservergroups |
| dbo | [sp_delete_targetsvrgrp_member](dbo.sp_delete_targetsvrgrp_member.md) | dbo.systargetservergroupmembers, dbo.systargetservergroups, dbo.systargetservers |
| dbo | [sp_detach_schedule](dbo.sp_detach_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sp_verify_schedule_identifiers, dbo.sysjobs, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysmaintplan_subplans, dbo.sysschedules |
| dbo | [sp_downloaded_row_limiter](dbo.sp_downloaded_row_limiter.md) | dbo.sysdownloadlist, dbo.xp_instance_regread, dbo.xp_instance_regwrite |
| dbo | [sp_droptask](dbo.sp_droptask.md) | dbo.sp_delete_job, dbo.sp_manage_jobs_by_login, dbo.sysjobs_view, dbo.systaskids |
| dbo | [sp_DTA_add_session](dbo.sp_DTA_add_session.md) | dbo.DTA_input, dbo.DTA_progress, dbo.DTA_reports_database, dbo.fn_DTA_unquote_dbname, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_check_permission](dbo.sp_DTA_check_permission.md) | dbo.DTA_reports_database |
| dbo | [sp_DTA_column_access_helper_relational](dbo.sp_DTA_column_access_helper_relational.md) | dbo.DTA_reports_column, dbo.DTA_reports_database, dbo.DTA_reports_query, dbo.DTA_reports_querycolumn, dbo.DTA_reports_table |
| dbo | [sp_DTA_column_access_helper_xml](dbo.sp_DTA_column_access_helper_xml.md) | dbo.DTA_reports_column, dbo.DTA_reports_database, dbo.DTA_reports_query, dbo.DTA_reports_querycolumn, dbo.DTA_reports_table |
| dbo | [sp_DTA_database_access_helper_relational](dbo.sp_DTA_database_access_helper_relational.md) | dbo.DTA_reports_database, dbo.DTA_reports_query, dbo.DTA_reports_querydatabase |
| dbo | [sp_DTA_database_access_helper_xml](dbo.sp_DTA_database_access_helper_xml.md) | dbo.DTA_reports_database, dbo.DTA_reports_query, dbo.DTA_reports_querydatabase |
| dbo | [sp_DTA_delete_session](dbo.sp_DTA_delete_session.md) | dbo.DTA_input, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_end_xmlprefix](dbo.sp_DTA_end_xmlprefix.md) |  |
| dbo | [sp_DTA_event_weight_helper_relational](dbo.sp_DTA_event_weight_helper_relational.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_event_weight_helper_xml](dbo.sp_DTA_event_weight_helper_xml.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_get_columntableids](dbo.sp_DTA_get_columntableids.md) | dbo.DTA_reports_column, dbo.DTA_reports_database, dbo.DTA_reports_table, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_databasetableids](dbo.sp_DTA_get_databasetableids.md) | dbo.DTA_reports_database, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_indexableids](dbo.sp_DTA_get_indexableids.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_table, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_interactivestatus](dbo.sp_DTA_get_interactivestatus.md) | dbo.DTA_input, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_pftableids](dbo.sp_DTA_get_pftableids.md) | dbo.DTA_reports_database, dbo.DTA_reports_partitionfunction, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_pstableids](dbo.sp_DTA_get_pstableids.md) | dbo.DTA_reports_database, dbo.DTA_reports_partitionfunction, dbo.DTA_reports_partitionscheme, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_session_report](dbo.sp_DTA_get_session_report.md) | dbo.sp_DTA_check_permission, dbo.sp_DTA_column_access_helper_relational, dbo.sp_DTA_column_access_helper_xml, dbo.sp_DTA_database_access_helper_relational, dbo.sp_DTA_database_access_helper_xml, dbo.sp_DTA_event_weight_helper_relational, dbo.sp_DTA_event_weight_helper_xml, dbo.sp_DTA_index_current_detail_helper_xml, dbo.sp_DTA_index_detail_current_helper_relational, dbo.sp_DTA_index_detail_recommended_helper_relational, dbo.sp_DTA_index_recommended_detail_helper_xml, dbo.sp_DTA_index_usage_helper_relational, dbo.sp_DTA_index_usage_helper_xml, dbo.sp_DTA_query_cost_helper_relational, dbo.sp_DTA_query_cost_helper_xml, dbo.sp_DTA_query_costrange_helper_relational, dbo.sp_DTA_query_costrange_helper_xml, dbo.sp_DTA_query_detail_helper_relational, dbo.sp_DTA_query_detail_helper_xml, dbo.sp_DTA_query_indexrelations_helper_relational, dbo.sp_DTA_query_indexrelations_helper_xml, dbo.sp_DTA_table_access_helper_relational, dbo.sp_DTA_table_access_helper_xml, dbo.sp_DTA_view_table_helper_relational, dbo.sp_DTA_view_table_helper_xml, dbo.sp_DTA_wkld_analysis_helper_relational, dbo.sp_DTA_wkld_analysis_helper_xml |
| dbo | [sp_DTA_get_session_tuning_results](dbo.sp_DTA_get_session_tuning_results.md) | dbo.DTA_output, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_tableids](dbo.sp_DTA_get_tableids.md) | dbo.DTA_reports_database, dbo.DTA_reports_table, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_tuninglog](dbo.sp_DTA_get_tuninglog.md) | dbo.DTA_input, dbo.DTA_tuninglog, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_tuningoptions](dbo.sp_DTA_get_tuningoptions.md) | dbo.DTA_input, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_help_session](dbo.sp_DTA_help_session.md) | dbo.DTA_input, dbo.DTA_output, dbo.DTA_progress, dbo.DTA_reports_database, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_index_current_detail_helper_xml](dbo.sp_DTA_index_current_detail_helper_xml.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_table |
| dbo | [sp_DTA_index_detail_current_helper_relational](dbo.sp_DTA_index_detail_current_helper_relational.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_table |
| dbo | [sp_DTA_index_detail_recommended_helper_relational](dbo.sp_DTA_index_detail_recommended_helper_relational.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_table |
| dbo | [sp_DTA_index_recommended_detail_helper_xml](dbo.sp_DTA_index_recommended_detail_helper_xml.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_table |
| dbo | [sp_DTA_index_usage_helper_relational](dbo.sp_DTA_index_usage_helper_relational.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_query, dbo.DTA_reports_queryindex, dbo.DTA_reports_table |
| dbo | [sp_DTA_index_usage_helper_xml](dbo.sp_DTA_index_usage_helper_xml.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_query, dbo.DTA_reports_queryindex, dbo.DTA_reports_table |
| dbo | [sp_DTA_insert_DTA_tuninglog](dbo.sp_DTA_insert_DTA_tuninglog.md) | dbo.DTA_tuninglog, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_progressinformation](dbo.sp_DTA_insert_progressinformation.md) | dbo.DTA_progress, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_column](dbo.sp_DTA_insert_reports_column.md) | dbo.DTA_reports_column, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_database](dbo.sp_DTA_insert_reports_database.md) | dbo.DTA_reports_database, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_index](dbo.sp_DTA_insert_reports_index.md) | dbo.DTA_reports_index, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_indexcolumn](dbo.sp_DTA_insert_reports_indexcolumn.md) | dbo.DTA_reports_indexcolumn, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_partitionfunction](dbo.sp_DTA_insert_reports_partitionfunction.md) | dbo.DTA_reports_partitionfunction, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_partitionscheme](dbo.sp_DTA_insert_reports_partitionscheme.md) | dbo.DTA_reports_partitionscheme, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_query](dbo.sp_DTA_insert_reports_query.md) | dbo.DTA_reports_query, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_querycolumn](dbo.sp_DTA_insert_reports_querycolumn.md) | dbo.DTA_reports_querycolumn, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_querydatabase](dbo.sp_DTA_insert_reports_querydatabase.md) | dbo.DTA_reports_querydatabase, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_queryindex](dbo.sp_DTA_insert_reports_queryindex.md) | dbo.DTA_reports_queryindex, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_querytable](dbo.sp_DTA_insert_reports_querytable.md) | dbo.DTA_reports_querytable, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_table](dbo.sp_DTA_insert_reports_table.md) | dbo.DTA_reports_table, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_insert_reports_tableview](dbo.sp_DTA_insert_reports_tableview.md) | dbo.DTA_reports_tableview, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_query_cost_helper_relational](dbo.sp_DTA_query_cost_helper_relational.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_query_cost_helper_xml](dbo.sp_DTA_query_cost_helper_xml.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_query_costrange_helper_relational](dbo.sp_DTA_query_costrange_helper_relational.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_query_costrange_helper_xml](dbo.sp_DTA_query_costrange_helper_xml.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_query_detail_helper_relational](dbo.sp_DTA_query_detail_helper_relational.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_query_detail_helper_xml](dbo.sp_DTA_query_detail_helper_xml.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_query_indexrelations_helper_relational](dbo.sp_DTA_query_indexrelations_helper_relational.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_query, dbo.DTA_reports_queryindex, dbo.DTA_reports_table |
| dbo | [sp_DTA_query_indexrelations_helper_xml](dbo.sp_DTA_query_indexrelations_helper_xml.md) | dbo.DTA_reports_database, dbo.DTA_reports_index, dbo.DTA_reports_query, dbo.DTA_reports_queryindex, dbo.DTA_reports_table |
| dbo | [sp_DTA_set_interactivestatus](dbo.sp_DTA_set_interactivestatus.md) | dbo.DTA_input, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_set_outputinformation](dbo.sp_DTA_set_outputinformation.md) | dbo.DTA_output, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_set_progressinformation](dbo.sp_DTA_set_progressinformation.md) | dbo.DTA_progress, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_set_tuninglogtablename](dbo.sp_DTA_set_tuninglogtablename.md) | dbo.DTA_input, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_start_xmlprefix](dbo.sp_DTA_start_xmlprefix.md) |  |
| dbo | [sp_DTA_table_access_helper_relational](dbo.sp_DTA_table_access_helper_relational.md) | dbo.DTA_reports_database, dbo.DTA_reports_query, dbo.DTA_reports_querytable, dbo.DTA_reports_table |
| dbo | [sp_DTA_table_access_helper_xml](dbo.sp_DTA_table_access_helper_xml.md) | dbo.DTA_reports_database, dbo.DTA_reports_query, dbo.DTA_reports_querytable, dbo.DTA_reports_table |
| dbo | [sp_DTA_update_session](dbo.sp_DTA_update_session.md) | dbo.DTA_input, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_update_tuninglog_errorfrequency](dbo.sp_DTA_update_tuninglog_errorfrequency.md) | dbo.DTA_tuninglog, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_view_table_helper_relational](dbo.sp_DTA_view_table_helper_relational.md) | dbo.DTA_reports_database, dbo.DTA_reports_table, dbo.DTA_reports_tableview |
| dbo | [sp_DTA_view_table_helper_xml](dbo.sp_DTA_view_table_helper_xml.md) | dbo.DTA_reports_database, dbo.DTA_reports_table, dbo.DTA_reports_tableview |
| dbo | [sp_DTA_wkld_analysis_helper_relational](dbo.sp_DTA_wkld_analysis_helper_relational.md) | dbo.DTA_reports_query |
| dbo | [sp_DTA_wkld_analysis_helper_xml](dbo.sp_DTA_wkld_analysis_helper_xml.md) | dbo.DTA_reports_query |
| dbo | [sp_enlist_tsx](dbo.sp_enlist_tsx.md) | dbo.sp_delete_targetserver, dbo.sysdownloadlist, dbo.sysoperators, dbo.systargetservers, dbo.xp_instance_regread |
| dbo | [sp_enum_login_for_proxy](dbo.sp_enum_login_for_proxy.md) | dbo.get_principal_id, dbo.sp_verify_proxy_identifiers, dbo.sysproxies, dbo.sysproxylogin |
| dbo | [sp_enum_proxy_for_subsystem](dbo.sp_enum_proxy_for_subsystem.md) | dbo.sp_verify_proxy_identifiers, dbo.sp_verify_subsystem_identifiers, dbo.sysproxies, dbo.sysproxysubsystem, dbo.syssubsystems |
| dbo | [sp_enum_sqlagent_subsystems](dbo.sp_enum_sqlagent_subsystems.md) | dbo.sp_enum_sqlagent_subsystems_internal |
| dbo | [sp_enum_sqlagent_subsystems_internal](dbo.sp_enum_sqlagent_subsystems_internal.md) | dbo.sp_verify_subsystems, dbo.syssubsystems, dbo.xp_instance_regread |
| dbo | [sp_ExternalMailQueueListener](dbo.sp_ExternalMailQueueListener.md) | dbo.InternalMailQueue, dbo.sysmail_logmailevent_sp, dbo.sysmail_mailitems, Properties.value |
| dbo | [sp_generate_server_description](dbo.sp_generate_server_description.md) | dbo.xp_msver |
| dbo | [sp_generate_target_server_job_assignment_sql](dbo.sp_generate_target_server_job_assignment_sql.md) | dbo.sysjobservers, dbo.systargetservers |
| dbo | [sp_get_chunked_jobstep_params](dbo.sp_get_chunked_jobstep_params.md) | dbo.sp_verify_job_identifiers, dbo.sysjobsteps |
| dbo | [sp_get_composite_job_info](dbo.sp_get_composite_job_info.md) | dbo.SQLAGENT_SUSER_SID, dbo.SQLAGENT_SUSER_SNAME, dbo.syscategories, dbo.sysjobs_view, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoperators, dbo.systargetservers, dbo.xp_sqlagent_enum_jobs |
| dbo | [sp_get_job_alerts](dbo.sp_get_job_alerts.md) | dbo.sp_verify_job_identifiers, dbo.sysalerts |
| dbo | [sp_get_jobstep_db_username](dbo.sp_get_jobstep_db_username.md) |  |
| dbo | [sp_get_log_shipping_monitor_info](dbo.sp_get_log_shipping_monitor_info.md) | dbo.log_shipping_primaries, dbo.log_shipping_secondaries, dbo.sp_log_shipping_get_date_from_file, dbo.sp_log_shipping_in_sync |
| dbo | [sp_get_message_description](dbo.sp_get_message_description.md) |  |
| dbo | [sp_get_proxy_properties](dbo.sp_get_proxy_properties.md) | dbo.sp_verify_proxy_identifiers, dbo.sysproxies |
| dbo | [sp_get_schedule_description](dbo.sp_get_schedule_description.md) | dbo.xp_instance_regread |
| dbo | [sp_get_script](dbo.sp_get_script.md) | dbo.xp_get_script |
| dbo | [sp_get_sqlagent_properties](dbo.sp_get_sqlagent_properties.md) | dbo.systargetservers, dbo.xp_instance_regread, dbo.xp_regread |
| dbo | [sp_GetAttachmentData](dbo.sp_GetAttachmentData.md) | dbo.ConvertToInt, dbo.sp_isprohibited, dbo.sysmail_help_configure_value_sp |
| dbo | [sp_grant_login_to_proxy](dbo.sp_grant_login_to_proxy.md) | dbo.sp_sqlagent_is_srvrolemember, dbo.sp_verify_login_identifiers, dbo.sp_verify_proxy_identifiers, dbo.sysproxylogin |
| dbo | [sp_grant_proxy_to_subsystem](dbo.sp_grant_proxy_to_subsystem.md) | dbo.sp_verify_credential_identifiers, dbo.sp_verify_proxy_identifiers, dbo.sp_verify_subsystem_identifiers, dbo.sysproxies, dbo.sysproxysubsystem |
| dbo | [sp_help_alert](dbo.sp_help_alert.md) | dbo.sysalerts |
| dbo | [sp_help_category](dbo.sp_help_category.md) | dbo.sp_verify_category, dbo.syscategories |
| dbo | [sp_help_downloadlist](dbo.sp_help_downloadlist.md) | dbo.sp_verify_job_identifiers, dbo.sysdownloadlist, dbo.sysjobs_view, dbo.systargetservers |
| dbo | [sp_help_job](dbo.sp_help_job.md) | dbo.sp_get_composite_job_info, dbo.sp_verify_job_identifiers, dbo.sp_verify_subsystem, dbo.syscategories |
| dbo | [sp_help_jobactivity](dbo.sp_help_jobactivity.md) | dbo.sp_verify_job_identifiers, dbo.sysjobactivity, dbo.sysjobhistory, dbo.sysjobs_view, dbo.syssessions |
| dbo | [sp_help_jobcount](dbo.sp_help_jobcount.md) | dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules |
| dbo | [sp_help_jobhistory](dbo.sp_help_jobhistory.md) | dbo.sp_help_jobhistory_full, dbo.sp_help_jobhistory_sem, dbo.sp_help_jobhistory_summary, dbo.sp_verify_job_date, dbo.sp_verify_job_identifiers, dbo.sp_verify_job_time, dbo.sysjobs, dbo.sysjobservers |
| dbo | [sp_help_jobhistory_full](dbo.sp_help_jobhistory_full.md) | dbo.sysjobhistory, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_help_jobhistory_sem](dbo.sp_help_jobhistory_sem.md) | dbo.sysjobhistory, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_help_jobhistory_summary](dbo.sp_help_jobhistory_summary.md) | dbo.sysjobhistory, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_help_jobs_in_schedule](dbo.sp_help_jobs_in_schedule.md) | dbo.sp_get_composite_job_info, dbo.sp_verify_schedule_identifiers |
| dbo | [sp_help_jobschedule](dbo.sp_help_jobschedule.md) | dbo.sp_get_schedule_description, dbo.sp_verify_job_identifiers, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysschedules |
| dbo | [sp_help_jobserver](dbo.sp_help_jobserver.md) | dbo.sp_verify_job_identifiers, dbo.sysjobservers, dbo.systargetservers_view |
| dbo | [sp_help_jobstep](dbo.sp_help_jobstep.md) | dbo.sp_verify_job_identifiers, dbo.sysjobsteps |
| dbo | [sp_help_jobsteplog](dbo.sp_help_jobsteplog.md) | dbo.sp_verify_job_identifiers, dbo.sysjobs_view, dbo.sysjobsteps, dbo.sysjobstepslogs |
| dbo | [sp_help_maintenance_plan](dbo.sp_help_maintenance_plan.md) | dbo.sysdbmaintplan_databases, dbo.sysdbmaintplan_jobs, dbo.sysdbmaintplans |
| dbo | [sp_help_notification](dbo.sp_help_notification.md) | dbo.sysalerts, dbo.sysoperators |
| dbo | [sp_help_operator](dbo.sp_help_operator.md) | dbo.syscategories, dbo.sysoperators |
| dbo | [sp_help_operator_jobs](dbo.sp_help_operator_jobs.md) | dbo.sysjobs_view, dbo.sysoperators |
| dbo | [sp_help_proxy](dbo.sp_help_proxy.md) | dbo.sp_verify_proxy_identifiers, dbo.sp_verify_proxy_permissions, dbo.sp_verify_subsystem_identifiers, dbo.sp_verify_subsystems, dbo.sysproxies, dbo.syssubsystems |
| dbo | [sp_help_schedule](dbo.sp_help_schedule.md) | dbo.sp_get_schedule_description, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysschedules_localserver_view |
| dbo | [sp_help_targetserver](dbo.sp_help_targetserver.md) | dbo.sysdownloadlist, dbo.systargetservers |
| dbo | [sp_help_targetservergroup](dbo.sp_help_targetservergroup.md) | dbo.systargetservergroupmembers, dbo.systargetservergroups, dbo.systargetservers |
| dbo | [sp_is_sqlagent_starting](dbo.sp_is_sqlagent_starting.md) | dbo.xp_sqlagent_is_starting |
| dbo | [sp_isprohibited](dbo.sp_isprohibited.md) |  |
| dbo | [sp_jobhistory_row_limiter](dbo.sp_jobhistory_row_limiter.md) | dbo.sysjobhistory, dbo.xp_instance_regread, dbo.xp_instance_regwrite |
| dbo | [sp_log_shipping_get_date_from_file](dbo.sp_log_shipping_get_date_from_file.md) |  |
| dbo | [sp_log_shipping_in_sync](dbo.sp_log_shipping_in_sync.md) |  |
| dbo | [sp_log_shipping_monitor_backup](dbo.sp_log_shipping_monitor_backup.md) | dbo.log_shipping_primaries, dbo.sp_log_shipping_in_sync |
| dbo | [sp_log_shipping_monitor_restore](dbo.sp_log_shipping_monitor_restore.md) | dbo.log_shipping_primaries, dbo.log_shipping_secondaries, dbo.sp_log_shipping_get_date_from_file, dbo.sp_log_shipping_in_sync |
| dbo | [sp_MailItemResultSets](dbo.sp_MailItemResultSets.md) | dbo.sysmail_account, dbo.sysmail_attachments, dbo.sysmail_mailitems, dbo.sysmail_profile, dbo.sysmail_profileaccount, dbo.sysmail_send_retries |
| dbo | [sp_maintplan_close_logentry](dbo.sp_maintplan_close_logentry.md) | dbo.sysmaintplan_log |
| dbo | [sp_maintplan_delete_log](dbo.sp_maintplan_delete_log.md) | dbo.sysmaintplan_log, dbo.sysmaintplan_logdetail |
| dbo | [sp_maintplan_delete_plan](dbo.sp_maintplan_delete_plan.md) | dbo.sp_maintplan_delete_subplan, dbo.sysmaintplan_subplans |
| dbo | [sp_maintplan_delete_subplan](dbo.sp_maintplan_delete_subplan.md) | dbo.sp_delete_job, dbo.sp_maintplan_delete_log, dbo.sysmaintplan_subplans |
| dbo | [sp_maintplan_open_logentry](dbo.sp_maintplan_open_logentry.md) | dbo.sysmaintplan_log |
| dbo | [sp_maintplan_start](dbo.sp_maintplan_start.md) | dbo.sp_start_job, dbo.sysmaintplan_subplans |
| dbo | [sp_maintplan_subplans_by_job](dbo.sp_maintplan_subplans_by_job.md) | dbo.sysmaintplan_plans, dbo.sysmaintplan_subplans |
| dbo | [sp_maintplan_update_log](dbo.sp_maintplan_update_log.md) | dbo.sysmaintplan_logdetail |
| dbo | [sp_maintplan_update_subplan](dbo.sp_maintplan_update_subplan.md) | dbo.sysmaintplan_subplans |
| dbo | [sp_maintplan_update_subplan_tsx](dbo.sp_maintplan_update_subplan_tsx.md) | dbo.sp_maintplan_update_subplan, dbo.sysjobschedules, dbo.sysmaintplan_subplans |
| dbo | [sp_manage_jobs_by_login](dbo.sp_manage_jobs_by_login.md) | dbo.sp_delete_job, dbo.sp_sqlagent_has_server_access, dbo.SQLAGENT_SUSER_SID, dbo.sysjobs, dbo.sysjobservers |
| dbo | [sp_msx_defect](dbo.sp_msx_defect.md) | dbo.sp_delete_all_msx_jobs, dbo.sp_delete_operator, dbo.sqlagent_info, dbo.sysoperators, dbo.sysoriginatingservers, dbo.xp_cmdshell, dbo.xp_getnetname, dbo.xp_instance_regdeletevalue, dbo.xp_instance_regread, dbo.xp_instance_regwrite, dbo.xp_msx_enlist |
| dbo | [sp_msx_enlist](dbo.sp_msx_enlist.md) | dbo.sp_delete_all_msx_jobs, dbo.sp_generate_server_description, dbo.sp_msx_defect, dbo.sqlagent_info, dbo.sysoriginatingservers, dbo.systargetservers, dbo.xp_instance_regread, dbo.xp_instance_regwrite, dbo.xp_msx_enlist, dbo.xp_regread |
| dbo | [sp_msx_get_account](dbo.sp_msx_get_account.md) | dbo.xp_instance_regread |
| dbo | [sp_msx_set_account](dbo.sp_msx_set_account.md) | dbo.sp_verify_credential_identifiers, dbo.xp_instance_regwrite |
| dbo | [sp_multi_server_job_summary](dbo.sp_multi_server_job_summary.md) | dbo.sp_verify_job_identifiers, dbo.syscategories, dbo.sysdownloadlist, dbo.sysjobs, dbo.sysjobservers |
| dbo | [sp_notify_operator](dbo.sp_notify_operator.md) | dbo.sp_verify_operator_identifiers, dbo.sysoperators |
| dbo | [sp_post_msx_operation](dbo.sp_post_msx_operation.md) | dbo.sp_downloaded_row_limiter, dbo.sysdownloadlist, dbo.sysjobs_view, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysschedules, dbo.sysschedules_localserver_view, dbo.systargetservers, dbo.xp_getnetname, dbo.xp_regread |
| dbo | [sp_process_DialogTimer](dbo.sp_process_DialogTimer.md) | dbo.ConvertToInt, dbo.sp_MailItemResultSets, dbo.sysmail_help_configure_value_sp, dbo.sysmail_logmailevent_sp, dbo.sysmail_mailitems, dbo.sysmail_send_retries |
| dbo | [sp_ProcessResponse](dbo.sp_ProcessResponse.md) | dbo.ConvertToInt, dbo.sysmail_help_configure_value_sp, dbo.sysmail_logmailevent_sp, dbo.sysmail_mailitems, dbo.sysmail_send_retries, Properties.value |
| dbo | [sp_purge_jobhistory](dbo.sp_purge_jobhistory.md) | dbo.sp_verify_job_identifiers, dbo.sysjobhistory |
| dbo | [sp_read_settings](dbo.sp_read_settings.md) |  |
| dbo | [sp_readrequest](dbo.sp_readrequest.md) | dbo.ExternalMailQueue, dbo.sp_MailItemResultSets, dbo.sp_process_DialogTimer, dbo.sysmail_logmailevent_sp, dbo.sysmail_mailitems, Properties.value |
| dbo | [sp_reassign_proxy](dbo.sp_reassign_proxy.md) | dbo.sp_update_jobstep, dbo.sp_verify_proxy_identifiers, dbo.sysjobsteps, dbo.sysproxysubsystem, dbo.syssubsystems |
| dbo | [sp_remove_job_from_targets](dbo.sp_remove_job_from_targets.md) | dbo.sp_apply_job_to_targets |
| dbo | [sp_remove_log_shipping_monitor_account](dbo.sp_remove_log_shipping_monitor_account.md) |  |
| dbo | [sp_resync_targetserver](dbo.sp_resync_targetserver.md) | dbo.sp_post_msx_operation, dbo.sysdownloadlist, dbo.systargetservers |
| dbo | [sp_revoke_login_from_proxy](dbo.sp_revoke_login_from_proxy.md) | dbo.sp_sqlagent_is_srvrolemember, dbo.sp_verify_proxy_identifiers, dbo.sysproxylogin |
| dbo | [sp_revoke_proxy_from_subsystem](dbo.sp_revoke_proxy_from_subsystem.md) | dbo.sp_verify_proxy_identifiers, dbo.sp_verify_subsystem_identifiers, dbo.sysproxysubsystem |
| dbo | [sp_RunMailQuery](dbo.sp_RunMailQuery.md) | dbo.ConvertToInt, dbo.sp_isprohibited, dbo.sysmail_help_configure_value_sp |
| dbo | [sp_sem_add_message](dbo.sp_sem_add_message.md) | dbo.spt_values |
| dbo | [sp_sem_drop_message](dbo.sp_sem_drop_message.md) | dbo.spt_values |
| dbo | [sp_send_dbmail](dbo.sp_send_dbmail.md) | dbo.get_principal_id, dbo.sp_GetAttachmentData, dbo.sp_RunMailQuery, dbo.sp_SendMailQueues, dbo.sp_validate_user, dbo.sysmail_attachments, dbo.sysmail_attachments_transfer, dbo.sysmail_mailitems, dbo.sysmail_principalprofile, dbo.sysmail_query_transfer, dbo.sysmail_verify_addressparams_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sp_SendMailMessage](dbo.sp_SendMailMessage.md) |  |
| dbo | [sp_SendMailQueues](dbo.sp_SendMailQueues.md) | dbo.sp_SendMailMessage |
| dbo | [sp_set_local_time](dbo.sp_set_local_time.md) | dbo.xp_cmdshell, dbo.xp_regread |
| dbo | [sp_set_sqlagent_properties](dbo.sp_set_sqlagent_properties.md) | dbo.sp_sqlagent_notify, dbo.xp_instance_regdeletevalue, dbo.xp_instance_regread, dbo.xp_instance_regwrite, dbo.xp_regwrite |
| dbo | [sp_sqlagent_check_msx_version](dbo.sp_sqlagent_check_msx_version.md) |  |
| dbo | [sp_sqlagent_get_perf_counters](dbo.sp_sqlagent_get_perf_counters.md) | dbo.sysalerts, dbo.sysalerts_performance_counters_view |
| dbo | [sp_sqlagent_get_startup_info](dbo.sp_sqlagent_get_startup_info.md) | dbo.xp_qv |
| dbo | [sp_sqlagent_has_server_access](dbo.sp_sqlagent_has_server_access.md) | dbo.SQLAGENT_SUSER_SNAME, dbo.syscachedcredentials, dbo.sysjobs_view, dbo.xp_logininfo |
| dbo | [sp_sqlagent_is_member](dbo.sp_sqlagent_is_member.md) |  |
| dbo | [sp_sqlagent_is_srvrolemember](dbo.sp_sqlagent_is_srvrolemember.md) |  |
| dbo | [sp_sqlagent_log_jobhistory](dbo.sp_sqlagent_log_jobhistory.md) | dbo.MSdistributiondbs, dbo.sp_jobhistory_row_limiter, dbo.sp_verify_job_date, dbo.sp_verify_job_time, dbo.sp_verify_jobproc_caller, dbo.sysjobactivity, dbo.sysjobhistory, dbo.sysjobs, dbo.sysjobs_view, dbo.sysjobsteps, dbo.sysoperators |
| dbo | [sp_sqlagent_notify](dbo.sp_sqlagent_notify.md) | dbo.sysalerts, dbo.sysjobs_view, dbo.sysjobsteps, dbo.sysschedules, dbo.xp_sqlagent_notify |
| dbo | [sp_sqlagent_probe_msx](dbo.sp_sqlagent_probe_msx.md) | dbo.sysdownloadlist, dbo.systargetservers |
| dbo | [sp_sqlagent_refresh_job](dbo.sp_sqlagent_refresh_job.md) | dbo.SQLAGENT_SUSER_SNAME, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysjobsteps, dbo.systargetservers_view |
| dbo | [sp_sqlagent_update_agent_xps](dbo.sp_sqlagent_update_agent_xps.md) |  |
| dbo | [sp_ssis_addfolder](dbo.sp_ssis_addfolder.md) | dbo.sysssispackagefolders |
| dbo | [sp_ssis_addlogentry](dbo.sp_ssis_addlogentry.md) | dbo.sysssislog |
| dbo | [sp_ssis_checkexists](dbo.sp_ssis_checkexists.md) | dbo.sysssispackages |
| dbo | [sp_ssis_deletefolder](dbo.sp_ssis_deletefolder.md) | dbo.sysssispackagefolders, dbo.sysssispackages |
| dbo | [sp_ssis_deletepackage](dbo.sp_ssis_deletepackage.md) | dbo.sysssispackages |
| dbo | [sp_ssis_getfolder](dbo.sp_ssis_getfolder.md) | dbo.sysssispackagefolders |
| dbo | [sp_ssis_getpackage](dbo.sp_ssis_getpackage.md) | dbo.sysssispackages |
| dbo | [sp_ssis_getpackageroles](dbo.sp_ssis_getpackageroles.md) | dbo.sysssispackages |
| dbo | [sp_ssis_listfolders](dbo.sp_ssis_listfolders.md) | dbo.sysssispackagefolders |
| dbo | [sp_ssis_listpackages](dbo.sp_ssis_listpackages.md) | dbo.sysssispackages |
| dbo | [sp_ssis_putpackage](dbo.sp_ssis_putpackage.md) | dbo.sysssispackages |
| dbo | [sp_ssis_renamefolder](dbo.sp_ssis_renamefolder.md) | dbo.sysssispackagefolders |
| dbo | [sp_ssis_setpackageroles](dbo.sp_ssis_setpackageroles.md) | dbo.sysssispackages |
| dbo | [sp_start_job](dbo.sp_start_job.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sysjobs, dbo.sysjobservers, dbo.sysjobsteps, dbo.systargetservers |
| dbo | [sp_stop_job](dbo.sp_stop_job.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sysjobs_view, dbo.sysjobservers, dbo.systargetservers |
| dbo | [sp_syscollector_cleanup_collector](dbo.sp_syscollector_cleanup_collector.md) | dbo.sp_delete_job, dbo.syscollector_collection_sets, dbo.syscollector_collection_sets_internal, dbo.syscollector_config_store_internal, dbo.syscollector_execution_log_internal, dbo.sysjobs |
| dbo | [sp_syscollector_configure_sql_dumper](dbo.sp_syscollector_configure_sql_dumper.md) | dbo.sp_syscollector_verify_collection_set, dbo.syscollector_collection_sets, dbo.syscollector_collection_sets_internal |
| dbo | [sp_syscollector_create_collection_item](dbo.sp_syscollector_create_collection_item.md) | dbo.sp_syscollector_validate_xml, dbo.syscollector_collection_items_internal, dbo.syscollector_collection_sets, dbo.syscollector_collector_types |
| dbo | [sp_syscollector_create_collection_set](dbo.sp_syscollector_create_collection_set.md) | dbo.sp_verify_proxy_identifiers, dbo.syscollector_collection_sets_internal, dbo.sysproxylogin, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_create_collector_type](dbo.sp_syscollector_create_collector_type.md) | dbo.syscollector_collector_types_internal, dbo.sysssispackages |
| dbo | [sp_syscollector_create_jobs](dbo.sp_syscollector_create_jobs.md) | dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_attach_schedule, dbo.sp_verify_proxy_identifiers |
| dbo | [sp_syscollector_create_tsql_query_collector](dbo.sp_syscollector_create_tsql_query_collector.md) | dbo.sp_ssis_setpackageroles, dbo.syscollector_collection_items, dbo.syscollector_collection_sets, dbo.syscollector_tsql_query_collector, dbo.sysssispackages |
| dbo | [sp_syscollector_delete_collection_item](dbo.sp_syscollector_delete_collection_item.md) | dbo.sp_syscollector_delete_collection_item_internal, dbo.sp_syscollector_stop_collection_set, dbo.sp_syscollector_verify_collection_item, dbo.syscollector_collection_items, dbo.syscollector_collection_sets |
| dbo | [sp_syscollector_delete_collection_item_internal](dbo.sp_syscollector_delete_collection_item_internal.md) | dbo.syscollector_collection_items_internal |
| dbo | [sp_syscollector_delete_collection_set](dbo.sp_syscollector_delete_collection_set.md) | dbo.sp_syscollector_delete_collection_set_internal, dbo.sp_syscollector_stop_collection_set, dbo.sp_syscollector_verify_collection_set, dbo.syscollector_collection_sets |
| dbo | [sp_syscollector_delete_collection_set_internal](dbo.sp_syscollector_delete_collection_set_internal.md) | dbo.sp_syscollector_delete_execution_log_tree, dbo.sp_syscollector_delete_jobs, dbo.syscollector_collection_sets, dbo.syscollector_collection_sets_internal, dbo.syscollector_execution_log, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_delete_collector_type](dbo.sp_syscollector_delete_collector_type.md) | dbo.sp_syscollector_verify_collector_type, dbo.syscollector_collection_items, dbo.syscollector_collector_types_internal |
| dbo | [sp_syscollector_delete_execution_log_tree](dbo.sp_syscollector_delete_execution_log_tree.md) | dbo.fn_syscollector_find_collection_set_root, dbo.syscollector_execution_log, dbo.syscollector_execution_log_internal, dbo.sysssislog |
| dbo | [sp_syscollector_delete_jobs](dbo.sp_syscollector_delete_jobs.md) | dbo.sp_delete_job, dbo.sp_delete_jobserver, dbo.sp_detach_schedule |
| dbo | [sp_syscollector_disable_collector](dbo.sp_syscollector_disable_collector.md) | dbo.sp_stop_job, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_syscollector_stop_collection_set_jobs, dbo.syscollector_collection_sets, dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_enable_collector](dbo.sp_syscollector_enable_collector.md) | dbo.sp_syscollector_start_collection_set_jobs, dbo.syscollector_collection_sets, dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_event_oncollectionbegin](dbo.sp_syscollector_event_oncollectionbegin.md) | dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_oncollectionend](dbo.sp_syscollector_event_oncollectionend.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_oncollectionstart](dbo.sp_syscollector_event_oncollectionstart.md) | dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_oncollectionstop](dbo.sp_syscollector_event_oncollectionstop.md) | dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_onerror](dbo.sp_syscollector_event_onerror.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log, dbo.syscollector_execution_log_internal, dbo.sysssislog |
| dbo | [sp_syscollector_event_onpackagebegin](dbo.sp_syscollector_event_onpackagebegin.md) | dbo.syscollector_execution_log, dbo.syscollector_execution_log_internal, dbo.sysssispackages |
| dbo | [sp_syscollector_event_onpackageend](dbo.sp_syscollector_event_onpackageend.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_onpackageupdate](dbo.sp_syscollector_event_onpackageupdate.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_onstatsupdate](dbo.sp_syscollector_event_onstatsupdate.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_stats_internal |
| dbo | [sp_syscollector_get_collection_set_execution_status](dbo.sp_syscollector_get_collection_set_execution_status.md) | dbo.syscollector_collection_sets, dbo.xp_sqlagent_enum_jobs |
| dbo | [sp_syscollector_get_instmdw](dbo.sp_syscollector_get_instmdw.md) | dbo.sp_syscollector_upload_instmdw, dbo.syscollector_blobs_internal |
| dbo | [sp_syscollector_get_trace_info](dbo.sp_syscollector_get_trace_info.md) |  |
| dbo | [sp_syscollector_get_tsql_query_collector_package_ids](dbo.sp_syscollector_get_tsql_query_collector_package_ids.md) | dbo.syscollector_tsql_query_collector, dbo.sysssispackages |
| dbo | [sp_syscollector_get_warehouse_connection_string](dbo.sp_syscollector_get_warehouse_connection_string.md) | dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_purge_collection_logs](dbo.sp_syscollector_purge_collection_logs.md) | dbo.sp_syscollector_delete_execution_log_tree, dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal, dbo.sysssislog |
| dbo | [sp_syscollector_run_collection_set](dbo.sp_syscollector_run_collection_set.md) | dbo.sp_start_job, dbo.sp_syscollector_create_jobs, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_syscollector_verify_collection_set, dbo.sp_syscollector_verify_collector_state, dbo.sp_verify_proxy_identifiers, dbo.sp_verify_schedule_identifiers, dbo.syscollector_collection_items, dbo.syscollector_collection_sets, dbo.syscollector_collection_sets_internal, dbo.syscollector_config_store_internal, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_set_cache_directory](dbo.sp_syscollector_set_cache_directory.md) | dbo.sp_syscollector_verify_collector_state, dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_set_cache_window](dbo.sp_syscollector_set_cache_window.md) | dbo.sp_syscollector_verify_collector_state, dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_set_warehouse_database_name](dbo.sp_syscollector_set_warehouse_database_name.md) | dbo.sp_syscollector_verify_collector_state, dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_set_warehouse_instance_name](dbo.sp_syscollector_set_warehouse_instance_name.md) | dbo.sp_syscollector_verify_collector_state, dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_sql_text_lookup](dbo.sp_syscollector_sql_text_lookup.md) |  |
| dbo | [sp_syscollector_start_collection_set](dbo.sp_syscollector_start_collection_set.md) | dbo.sp_syscollector_create_jobs, dbo.sp_syscollector_verify_collection_set, dbo.sp_verify_proxy_identifiers, dbo.sp_verify_schedule_identifiers, dbo.syscollector_collection_items, dbo.syscollector_collection_sets, dbo.syscollector_collection_sets_internal, dbo.syscollector_config_store_internal, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_start_collection_set_jobs](dbo.sp_syscollector_start_collection_set_jobs.md) | dbo.sp_start_job, dbo.sp_syscollector_event_oncollectionstart, dbo.sp_update_job, dbo.syscollector_collection_sets |
| dbo | [sp_syscollector_stop_collection_set](dbo.sp_syscollector_stop_collection_set.md) | dbo.sp_stop_job, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_syscollector_verify_collection_set, dbo.syscollector_collection_sets, dbo.syscollector_collection_sets_internal |
| dbo | [sp_syscollector_stop_collection_set_jobs](dbo.sp_syscollector_stop_collection_set_jobs.md) | dbo.sp_attach_schedule, dbo.sp_detach_schedule, dbo.sp_start_job, dbo.sp_syscollector_event_oncollectionstop, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_update_job, dbo.syscollector_collection_sets, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_text_query_plan_lookpup](dbo.sp_syscollector_text_query_plan_lookpup.md) |  |
| dbo | [sp_syscollector_update_collection_item](dbo.sp_syscollector_update_collection_item.md) | dbo.sp_syscollector_start_collection_set, dbo.sp_syscollector_stop_collection_set, dbo.sp_syscollector_update_collection_item_internal, dbo.sp_syscollector_validate_xml, dbo.sp_syscollector_verify_collection_item, dbo.syscollector_collection_items, dbo.syscollector_collection_sets |
| dbo | [sp_syscollector_update_collection_item_internal](dbo.sp_syscollector_update_collection_item_internal.md) | dbo.syscollector_collection_items_internal |
| dbo | [sp_syscollector_update_collection_set](dbo.sp_syscollector_update_collection_set.md) | dbo.sp_syscollector_start_collection_set, dbo.sp_syscollector_stop_collection_set, dbo.sp_syscollector_update_collection_set_internal, dbo.sp_syscollector_verify_collection_set, dbo.sp_verify_proxy_identifiers, dbo.syscollector_collection_sets, dbo.sysproxylogin, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_update_collection_set_internal](dbo.sp_syscollector_update_collection_set_internal.md) | dbo.sp_attach_schedule, dbo.sp_detach_schedule, dbo.sp_syscollector_create_jobs, dbo.sp_syscollector_delete_jobs, dbo.sp_syscollector_update_job_proxy, dbo.syscollector_collection_sets, dbo.syscollector_collection_sets_internal, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_update_collector_type](dbo.sp_syscollector_update_collector_type.md) | dbo.sp_syscollector_verify_collector_type, dbo.syscollector_collector_types, dbo.syscollector_collector_types_internal, dbo.sysssispackages |
| dbo | [sp_syscollector_update_job_proxy](dbo.sp_syscollector_update_job_proxy.md) | dbo.sp_update_jobstep, dbo.sysjobsteps |
| dbo | [sp_syscollector_upload_collection_set](dbo.sp_syscollector_upload_collection_set.md) | dbo.sp_start_job, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_syscollector_verify_collection_set, dbo.sp_syscollector_verify_collector_state, dbo.syscollector_collection_sets |
| dbo | [sp_syscollector_upload_instmdw](dbo.sp_syscollector_upload_instmdw.md) | dbo.syscollector_blobs_internal, dbo.xp_instance_regread |
| dbo | [sp_syscollector_validate_xml](dbo.sp_syscollector_validate_xml.md) | dbo.sp_syscollector_verify_collector_type, dbo.syscollector_collector_types_internal |
| dbo | [sp_syscollector_verify_collection_item](dbo.sp_syscollector_verify_collection_item.md) | dbo.syscollector_collection_items |
| dbo | [sp_syscollector_verify_collection_set](dbo.sp_syscollector_verify_collection_set.md) | dbo.syscollector_collection_sets |
| dbo | [sp_syscollector_verify_collector_state](dbo.sp_syscollector_verify_collector_state.md) | dbo.syscollector_config_store_internal |
| dbo | [sp_syscollector_verify_collector_type](dbo.sp_syscollector_verify_collector_type.md) | dbo.syscollector_collector_types |
| dbo | [sp_syscollector_verify_event_log_id](dbo.sp_syscollector_verify_event_log_id.md) | dbo.syscollector_execution_log |
| dbo | [sp_sysdac_add_history_entry](dbo.sp_sysdac_add_history_entry.md) | dbo.fn_sysdac_is_dac_creator, dbo.sysdac_history_internal, dbo.sysdac_instances |
| dbo | [sp_sysdac_add_instance](dbo.sp_sysdac_add_instance.md) | dbo.fn_sysdac_is_dac_creator, dbo.sysdac_instances_internal |
| dbo | [sp_sysdac_delete_history](dbo.sp_sysdac_delete_history.md) | dbo.sysdac_history_internal, dbo.sysdac_instances, dbo.sysdac_instances_internal |
| dbo | [sp_sysdac_delete_instance](dbo.sp_sysdac_delete_instance.md) | dbo.sysdac_instances, dbo.sysdac_instances_internal |
| dbo | [sp_sysdac_drop_database](dbo.sp_sysdac_drop_database.md) |  |
| dbo | [sp_sysdac_ensure_dac_creator](dbo.sp_sysdac_ensure_dac_creator.md) | dbo.fn_sysdac_is_dac_creator |
| dbo | [sp_sysdac_rename_database](dbo.sp_sysdac_rename_database.md) |  |
| dbo | [sp_sysdac_resolve_pending_entry](dbo.sp_sysdac_resolve_pending_entry.md) | dbo.sysdac_history_internal, dbo.sysdac_instances_internal |
| dbo | [sp_sysdac_rollback_all_pending_objects](dbo.sp_sysdac_rollback_all_pending_objects.md) | dbo.sp_sysdac_rollback_pending_object, dbo.sysdac_history_internal |
| dbo | [sp_sysdac_rollback_committed_step](dbo.sp_sysdac_rollback_committed_step.md) | dbo.sp_sysdac_delete_instance, dbo.sp_sysdac_drop_database, dbo.sp_sysdac_rename_database, dbo.sp_sysdac_setreadonly_database, dbo.sysdac_history_internal, dbo.sysdac_instances_internal |
| dbo | [sp_sysdac_rollback_pending_object](dbo.sp_sysdac_rollback_pending_object.md) | dbo.sp_sysdac_resolve_pending_entry, dbo.sp_sysdac_rollback_committed_step, dbo.sysdac_history_internal |
| dbo | [sp_sysdac_setreadonly_database](dbo.sp_sysdac_setreadonly_database.md) |  |
| dbo | [sp_sysdac_update_history_entry](dbo.sp_sysdac_update_history_entry.md) | dbo.fn_sysdac_get_currentusername, dbo.fn_sysdac_is_currentuser_sa, dbo.sysdac_history_internal |
| dbo | [sp_sysdac_update_instance](dbo.sp_sysdac_update_instance.md) | dbo.sysdac_instances, dbo.sysdac_instances_internal |
| dbo | [sp_sysdac_upgrade_instance](dbo.sp_sysdac_upgrade_instance.md) | dbo.sp_sysdac_delete_instance, dbo.sysdac_instances, dbo.sysdac_instances_internal |
| dbo | [sp_sysmail_activate](dbo.sp_sysmail_activate.md) | dbo.ConvertToInt, dbo.sysmail_help_configure_value_sp, dbo.sysmail_logmailevent_sp |
| dbo | [sp_sysmanagement_add_shared_registered_server](dbo.sp_sysmanagement_add_shared_registered_server.md) | dbo.sp_sysmanagement_verify_shared_server_type, dbo.sysmanagement_shared_registered_servers_internal, dbo.sysmanagement_shared_server_groups_internal |
| dbo | [sp_sysmanagement_add_shared_server_group](dbo.sp_sysmanagement_add_shared_server_group.md) | dbo.sp_sysmanagement_verify_shared_server_type, dbo.sysmanagement_shared_server_groups_internal |
| dbo | [sp_sysmanagement_delete_shared_registered_server](dbo.sp_sysmanagement_delete_shared_registered_server.md) | dbo.sysmanagement_shared_registered_servers_internal |
| dbo | [sp_sysmanagement_delete_shared_server_group](dbo.sp_sysmanagement_delete_shared_server_group.md) | dbo.sysmanagement_shared_server_groups_internal |
| dbo | [sp_sysmanagement_move_shared_registered_server](dbo.sp_sysmanagement_move_shared_registered_server.md) | dbo.sysmanagement_shared_registered_servers_internal, dbo.sysmanagement_shared_server_groups_internal |
| dbo | [sp_sysmanagement_move_shared_server_group](dbo.sp_sysmanagement_move_shared_server_group.md) | dbo.sysmanagement_shared_server_groups_internal |
| dbo | [sp_sysmanagement_rename_shared_registered_server](dbo.sp_sysmanagement_rename_shared_registered_server.md) | dbo.sysmanagement_shared_registered_servers_internal |
| dbo | [sp_sysmanagement_rename_shared_server_group](dbo.sp_sysmanagement_rename_shared_server_group.md) | dbo.sysmanagement_shared_server_groups_internal |
| dbo | [sp_sysmanagement_update_shared_registered_server](dbo.sp_sysmanagement_update_shared_registered_server.md) | dbo.sysmanagement_shared_registered_servers_internal |
| dbo | [sp_sysmanagement_update_shared_server_group](dbo.sp_sysmanagement_update_shared_server_group.md) | dbo.sysmanagement_shared_server_groups_internal |
| dbo | [sp_sysmanagement_verify_shared_server_type](dbo.sp_sysmanagement_verify_shared_server_type.md) |  |
| dbo | [sp_syspolicy_add_condition](dbo.sp_syspolicy_add_condition.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_conditions, dbo.syspolicy_conditions_internal, dbo.syspolicy_management_facets |
| dbo | [sp_syspolicy_add_object_set](dbo.sp_syspolicy_add_object_set.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_management_facets, dbo.syspolicy_object_sets_internal |
| dbo | [sp_syspolicy_add_policy](dbo.sp_syspolicy_add_policy.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.syspolicy_conditions_internal, dbo.syspolicy_object_sets, dbo.syspolicy_policies, dbo.syspolicy_policies_internal, dbo.syspolicy_policy_categories, dbo.sysschedules |
| dbo | [sp_syspolicy_add_policy_category](dbo.sp_syspolicy_add_policy_category.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policy_categories_internal |
| dbo | [sp_syspolicy_add_policy_category_subscription](dbo.sp_syspolicy_add_policy_category_subscription.md) | dbo.syspolicy_policy_categories, dbo.syspolicy_policy_categories_internal, dbo.syspolicy_policy_category_subscriptions_internal |
| dbo | [sp_syspolicy_add_target_set](dbo.sp_syspolicy_add_target_set.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_object_set_identifiers, dbo.syspolicy_target_sets_internal |
| dbo | [sp_syspolicy_add_target_set_level](dbo.sp_syspolicy_add_target_set_level.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.syspolicy_target_set_levels_internal, dbo.syspolicy_target_sets |
| dbo | [sp_syspolicy_check_membership](dbo.sp_syspolicy_check_membership.md) |  |
| dbo | [sp_syspolicy_configure](dbo.sp_syspolicy_configure.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_set_config_enabled, dbo.sp_syspolicy_set_config_history_retention, dbo.sp_syspolicy_set_log_on_success |
| dbo | [sp_syspolicy_create_job](dbo.sp_syspolicy_create_job.md) | dbo.fn_syspolicy_get_ps_command, dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_attach_schedule, dbo.sp_syspolicy_check_membership, dbo.sp_update_jobstep, dbo.sysjobs, dbo.sysschedules |
| dbo | [sp_syspolicy_create_purge_job](dbo.sp_syspolicy_create_purge_job.md) | dbo.sp_add_job, dbo.sp_add_jobschedule, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_syspolicy_check_membership, dbo.sp_update_job, dbo.sysjobs, dbo.syspolicy_configuration, dbo.syspolicy_configuration_internal |
| dbo | [sp_syspolicy_delete_condition](dbo.sp_syspolicy_delete_condition.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.syspolicy_conditions_internal, dbo.syspolicy_policies |
| dbo | [sp_syspolicy_delete_object_set](dbo.sp_syspolicy_delete_object_set.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_object_set_identifiers, dbo.syspolicy_object_sets_internal |
| dbo | [sp_syspolicy_delete_policy](dbo.sp_syspolicy_delete_policy.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_policy_identifiers, dbo.syspolicy_policies_internal |
| dbo | [sp_syspolicy_delete_policy_category](dbo.sp_syspolicy_delete_policy_category.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_policy_category_identifiers, dbo.syspolicy_policies, dbo.syspolicy_policy_categories_internal, dbo.syspolicy_policy_category_subscriptions |
| dbo | [sp_syspolicy_delete_policy_category_subscription](dbo.sp_syspolicy_delete_policy_category_subscription.md) | dbo.syspolicy_policies, dbo.syspolicy_policy_category_subscriptions, dbo.syspolicy_policy_category_subscriptions_internal |
| dbo | [sp_syspolicy_delete_policy_execution_history](dbo.sp_syspolicy_delete_policy_execution_history.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policy_execution_history_internal |
| dbo | [sp_syspolicy_delete_target_set](dbo.sp_syspolicy_delete_target_set.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_target_sets_internal |
| dbo | [sp_syspolicy_dispatch_event](dbo.sp_syspolicy_dispatch_event.md) | c.value, dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_dispatch_event, dbo.spt_values, dbo.syspolicy_conditions_internal, dbo.syspolicy_execution_internal, dbo.syspolicy_facet_events, dbo.syspolicy_policies, dbo.syspolicy_policy_categories, dbo.syspolicy_policy_category_subscriptions, dbo.syspolicy_target_set_levels, dbo.syspolicy_target_sets |
| dbo | [sp_syspolicy_events_reader](dbo.sp_syspolicy_events_reader.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_dispatch_event, dbo.syspolicy_event_queue |
| dbo | [sp_syspolicy_log_policy_execution_detail](dbo.sp_syspolicy_log_policy_execution_detail.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policy_execution_history_details_internal, dbo.syspolicy_policy_execution_history_internal |
| dbo | [sp_syspolicy_log_policy_execution_end](dbo.sp_syspolicy_log_policy_execution_end.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policy_execution_history_internal |
| dbo | [sp_syspolicy_log_policy_execution_start](dbo.sp_syspolicy_log_policy_execution_start.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_policy_identifiers, dbo.syspolicy_policy_execution_history_internal |
| dbo | [sp_syspolicy_mark_system](dbo.sp_syspolicy_mark_system.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.sp_syspolicy_verify_object_set_identifiers, dbo.sp_syspolicy_verify_policy_identifiers, dbo.syspolicy_conditions_internal, dbo.syspolicy_object_sets_internal, dbo.syspolicy_policies_internal |
| dbo | [sp_syspolicy_purge_health_state](dbo.sp_syspolicy_purge_health_state.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_system_health_state_internal |
| dbo | [sp_syspolicy_purge_history](dbo.sp_syspolicy_purge_history.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_configuration, dbo.syspolicy_policies, dbo.syspolicy_policy_category_subscriptions_internal, dbo.syspolicy_policy_execution_history_details_internal, dbo.syspolicy_policy_execution_history_internal |
| dbo | [sp_syspolicy_rename_condition](dbo.sp_syspolicy_rename_condition.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.syspolicy_conditions_internal |
| dbo | [sp_syspolicy_rename_policy](dbo.sp_syspolicy_rename_policy.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_policy_identifiers, dbo.syspolicy_policies_internal |
| dbo | [sp_syspolicy_rename_policy_category](dbo.sp_syspolicy_rename_policy_category.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_policy_category_identifiers, dbo.syspolicy_policy_categories_internal  |
| dbo | [sp_syspolicy_repair_policy_automation](dbo.sp_syspolicy_repair_policy_automation.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policies_internal |
| dbo | [sp_syspolicy_set_config_enabled](dbo.sp_syspolicy_set_config_enabled.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_configuration_internal |
| dbo | [sp_syspolicy_set_config_history_retention](dbo.sp_syspolicy_set_config_history_retention.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_configuration_internal |
| dbo | [sp_syspolicy_set_log_on_success](dbo.sp_syspolicy_set_log_on_success.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_configuration_internal |
| dbo | [sp_syspolicy_update_condition](dbo.sp_syspolicy_update_condition.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.syspolicy_conditions_internal, dbo.syspolicy_management_facets |
| dbo | [sp_syspolicy_update_policy](dbo.sp_syspolicy_update_policy.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.sp_syspolicy_verify_object_set_identifiers, dbo.sp_syspolicy_verify_policy_identifiers, dbo.syspolicy_conditions_internal, dbo.syspolicy_object_sets, dbo.syspolicy_policies, dbo.syspolicy_policies_internal, dbo.syspolicy_policy_categories, dbo.sysschedules |
| dbo | [sp_syspolicy_update_policy_category](dbo.sp_syspolicy_update_policy_category.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_policy_category_identifiers, dbo.syspolicy_policy_categories_internal  |
| dbo | [sp_syspolicy_update_policy_category_subscription](dbo.sp_syspolicy_update_policy_category_subscription.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policies, dbo.syspolicy_policy_categories, dbo.syspolicy_policy_categories_internal, dbo.syspolicy_policy_category_subscriptions, dbo.syspolicy_policy_category_subscriptions_internal |
| dbo | [sp_syspolicy_update_target_set](dbo.sp_syspolicy_update_target_set.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_target_sets_internal |
| dbo | [sp_syspolicy_update_target_set_level](dbo.sp_syspolicy_update_target_set_level.md) | dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_verify_condition_identifiers, dbo.syspolicy_target_set_levels_internal |
| dbo | [sp_syspolicy_verify_condition_identifiers](dbo.sp_syspolicy_verify_condition_identifiers.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_conditions |
| dbo | [sp_syspolicy_verify_object_set_identifiers](dbo.sp_syspolicy_verify_object_set_identifiers.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_object_sets |
| dbo | [sp_syspolicy_verify_object_set_references](dbo.sp_syspolicy_verify_object_set_references.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policies |
| dbo | [sp_syspolicy_verify_policy_category_identifiers](dbo.sp_syspolicy_verify_policy_category_identifiers.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policy_categories |
| dbo | [sp_syspolicy_verify_policy_identifiers](dbo.sp_syspolicy_verify_policy_identifiers.md) | dbo.sp_syspolicy_check_membership, dbo.syspolicy_policies |
| dbo | [sp_sysutility_mi_add_ucp_registration](dbo.sp_sysutility_mi_add_ucp_registration.md) | dbo.sysutility_mi_configuration_internal, dbo.xp_instance_regwrite |
| dbo | [sp_sysutility_mi_collect_dac_execution_statistics_internal](dbo.sp_sysutility_mi_collect_dac_execution_statistics_internal.md) | dbo.sysdac_instances, dbo.sysutility_mi_dac_execution_statistics_internal, dbo.sysutility_mi_session_statistics_internal |
| dbo | [sp_sysutility_mi_configure_proxy_account](dbo.sp_sysutility_mi_configure_proxy_account.md) | dbo.sp_add_proxy, dbo.sp_delete_proxy, dbo.sp_grant_login_to_proxy, dbo.sp_grant_proxy_to_subsystem, dbo.sysproxies |
| dbo | [sp_sysutility_mi_create_cache_directory](dbo.sp_sysutility_mi_create_cache_directory.md) | dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_delete_job, dbo.sysjobs, dbo.xp_instance_regread |
| dbo | [sp_sysutility_mi_create_job_validate_wmi](dbo.sp_sysutility_mi_create_job_validate_wmi.md) | dbo.fn_sysutility_mi_get_validate_wmi_script, dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_delete_job, dbo.sysjobs |
| dbo | [sp_sysutility_mi_disable_collection](dbo.sp_sysutility_mi_disable_collection.md) | dbo.sp_update_job, dbo.syscategories, dbo.sysjobs |
| dbo | [sp_sysutility_mi_enroll](dbo.sp_sysutility_mi_enroll.md) | dbo.sp_sysutility_mi_validate_enrollment_preconditions |
| dbo | [sp_sysutility_mi_get_dac_execution_statistics_internal](dbo.sp_sysutility_mi_get_dac_execution_statistics_internal.md) | dbo.sysutility_batch_time_internal, dbo.sysutility_mi_dac_execution_statistics_internal |
| dbo | [sp_sysutility_mi_initialize_collection](dbo.sp_sysutility_mi_initialize_collection.md) | dbo.fn_sysutility_mi_get_collect_script, dbo.fn_sysutility_ucp_get_instance_is_mi, dbo.sp_add_category, dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_add_schedule, dbo.sp_attach_schedule, dbo.sp_delete_jobstep, dbo.sp_start_job, dbo.sp_sysutility_mi_collect_dac_execution_statistics_internal, dbo.sp_update_job, dbo.syscategories, dbo.sysjobs, dbo.sysschedules_localserver_view |
| dbo | [sp_sysutility_mi_remove](dbo.sp_sysutility_mi_remove.md) | dbo.sp_syscollector_disable_collector, dbo.sp_syscollector_enable_collector, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_syscollector_set_cache_directory, dbo.sp_syscollector_stop_collection_set, dbo.sp_syscollector_update_collection_set, dbo.sp_sysutility_mi_disable_collection, dbo.sp_sysutility_mi_remove_ucp_registration, dbo.syscollector_collection_sets, dbo.syscollector_config_store |
| dbo | [sp_sysutility_mi_remove_ucp_registration](dbo.sp_sysutility_mi_remove_ucp_registration.md) | dbo.fn_sysutility_get_is_instance_ucp, dbo.sysutility_mi_configuration_internal, dbo.xp_instance_regdeletekey, dbo.xp_instance_regdeletevalue, dbo.xp_instance_regread |
| dbo | [sp_sysutility_mi_upload](dbo.sp_sysutility_mi_upload.md) | dbo.fn_sysutility_ucp_get_instance_is_mi, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_syscollector_run_collection_set, dbo.sp_syscollector_verify_collector_state, dbo.syscollector_collection_sets_internal, dbo.syscollector_execution_log_internal |
| dbo | [sp_sysutility_mi_validate_enrollment_preconditions](dbo.sp_sysutility_mi_validate_enrollment_preconditions.md) | dbo.xp_qv |
| dbo | [sp_sysutility_mi_validate_proxy_account](dbo.sp_sysutility_mi_validate_proxy_account.md) | dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_add_proxy, dbo.sp_delete_job, dbo.sp_delete_proxy, dbo.sp_grant_proxy_to_subsystem, dbo.sysjobs, dbo.sysproxies |
| dbo | [sp_sysutility_ucp_add_mi](dbo.sp_sysutility_ucp_add_mi.md) | dbo.sysutility_ucp_managed_instances_internal |
| dbo | [sp_sysutility_ucp_add_policy](dbo.sp_sysutility_ucp_add_policy.md) | dbo.syspolicy_policies, dbo.sysutility_ucp_health_policies_internal |
| dbo | [sp_sysutility_ucp_calculate_aggregated_dac_health](dbo.sp_sysutility_ucp_calculate_aggregated_dac_health.md) | dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_dac_health_internal |
| dbo | [sp_sysutility_ucp_calculate_aggregated_mi_health](dbo.sp_sysutility_ucp_calculate_aggregated_mi_health.md) | dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_mi_health_internal |
| dbo | [sp_sysutility_ucp_calculate_computer_health](dbo.sp_sysutility_ucp_calculate_computer_health.md) | dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_computer_policies, dbo.sysutility_ucp_computers, dbo.sysutility_ucp_instances, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policy_violations, dbo.sysutility_ucp_volumes |
| dbo | [sp_sysutility_ucp_calculate_dac_file_space_health](dbo.sp_sysutility_ucp_calculate_dac_file_space_health.md) | dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_policies, dbo.sysutility_ucp_databases, dbo.sysutility_ucp_deployed_dacs, dbo.sysutility_ucp_filegroups, dbo.sysutility_ucp_filegroups_with_policy_violations_internal |
| dbo | [sp_sysutility_ucp_calculate_dac_health](dbo.sp_sysutility_ucp_calculate_dac_health.md) | dbo.fn_sysutility_ucp_get_aggregated_health, dbo.sp_sysutility_ucp_calculate_dac_file_space_health, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_dac_policies, dbo.sysutility_ucp_dac_policy_type, dbo.sysutility_ucp_datafiles, dbo.sysutility_ucp_deployed_dacs, dbo.sysutility_ucp_logfiles, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policy_violations |
| dbo | [sp_sysutility_ucp_calculate_filegroups_with_policy_violations](dbo.sp_sysutility_ucp_calculate_filegroups_with_policy_violations.md) | dbo.sysutility_ucp_database_files, dbo.sysutility_ucp_filegroups_with_policy_violations_internal, dbo.sysutility_ucp_policy_violations |
| dbo | [sp_sysutility_ucp_calculate_health](dbo.sp_sysutility_ucp_calculate_health.md) | dbo.sp_sysutility_ucp_calculate_aggregated_dac_health, dbo.sp_sysutility_ucp_calculate_aggregated_mi_health, dbo.sp_sysutility_ucp_calculate_computer_health, dbo.sp_sysutility_ucp_calculate_dac_health, dbo.sp_sysutility_ucp_calculate_filegroups_with_policy_violations, dbo.sp_sysutility_ucp_calculate_mi_health, dbo.sp_sysutility_ucp_get_policy_violations, dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_filegroups_with_policy_violations_internal, dbo.sysutility_ucp_mi_database_health_internal, dbo.sysutility_ucp_mi_file_space_health_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_processing_state_internal |
| dbo | [sp_sysutility_ucp_calculate_mi_file_space_health](dbo.sp_sysutility_ucp_calculate_mi_file_space_health.md) | dbo.sysutility_ucp_databases, dbo.sysutility_ucp_filegroups, dbo.sysutility_ucp_filegroups_with_policy_violations_internal, dbo.sysutility_ucp_instance_policies, dbo.sysutility_ucp_instances, dbo.sysutility_ucp_mi_database_health_internal, dbo.sysutility_ucp_mi_file_space_health_internal |
| dbo | [sp_sysutility_ucp_calculate_mi_health](dbo.sp_sysutility_ucp_calculate_mi_health.md) | dbo.fn_sysutility_ucp_get_aggregated_health, dbo.sp_sysutility_ucp_calculate_mi_file_space_health, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_datafiles, dbo.sysutility_ucp_instance_policies, dbo.sysutility_ucp_instance_policy_type, dbo.sysutility_ucp_instances, dbo.sysutility_ucp_logfiles, dbo.sysutility_ucp_managed_instances, dbo.sysutility_ucp_mi_file_space_health_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policy_violations |
| dbo | [sp_sysutility_ucp_configure_policies](dbo.sp_sysutility_ucp_configure_policies.md) | dbo.sp_delete_job, dbo.sp_delete_schedule, dbo.sp_syspolicy_add_condition, dbo.sp_syspolicy_add_object_set, dbo.sp_syspolicy_add_policy, dbo.sp_syspolicy_add_target_set, dbo.sp_syspolicy_add_target_set_level, dbo.sp_syspolicy_delete_condition, dbo.sp_syspolicy_delete_object_set, dbo.sp_syspolicy_delete_policy, dbo.sp_syspolicy_mark_system, dbo.sp_sysutility_ucp_add_policy, dbo.sp_sysutility_ucp_calculate_health, dbo.sysjobs_view, dbo.syspolicy_conditions, dbo.syspolicy_object_sets, dbo.syspolicy_policies, dbo.sysschedules, dbo.sysutility_ucp_health_policies_internal |
| dbo | [sp_sysutility_ucp_create](dbo.sp_sysutility_ucp_create.md) | dbo.sp_sysutility_ucp_validate_prerequisites |
| dbo | [sp_sysutility_ucp_delete_policy](dbo.sp_sysutility_ucp_delete_policy.md) | dbo.sysutility_ucp_health_policies_internal |
| dbo | [sp_sysutility_ucp_delete_policy_history](dbo.sp_sysutility_ucp_delete_policy_history.md) | dbo.sysutility_ucp_configuration_internal, dbo.sysutility_ucp_processing_state_internal |
| dbo | [sp_sysutility_ucp_get_policy_violations](dbo.sp_sysutility_ucp_get_policy_violations.md) | dbo.syspolicy_policy_execution_history_details_internal, dbo.syspolicy_policy_execution_history_internal, dbo.sysutility_ucp_policies, dbo.sysutility_ucp_policy_configuration, dbo.sysutility_ucp_policy_violations_internal, dbo.sysutility_ucp_processing_state_internal |
| dbo | [sp_sysutility_ucp_initialize](dbo.sp_sysutility_ucp_initialize.md) | dbo.sysutility_ucp_configuration_internal, dbo.xp_instance_regwrite |
| dbo | [sp_sysutility_ucp_initialize_mdw](dbo.sp_sysutility_ucp_initialize_mdw.md) | dbo.fn_sysutility_get_is_instance_ucp, dbo.sp_sysutility_ucp_recreate_synonym_internal |
| dbo | [sp_sysutility_ucp_provision_proxy_account](dbo.sp_sysutility_ucp_provision_proxy_account.md) | dbo.sp_sqlagent_has_server_access |
| dbo | [sp_sysutility_ucp_provision_utility_object_internal](dbo.sp_sysutility_ucp_provision_utility_object_internal.md) |  |
| dbo | [sp_sysutility_ucp_recreate_synonym_internal](dbo.sp_sysutility_ucp_recreate_synonym_internal.md) |  |
| dbo | [sp_sysutility_ucp_remove](dbo.sp_sysutility_ucp_remove.md) | core.source_info_internal, dbo.fn_sysutility_get_is_instance_ucp, dbo.sp_delete_job, dbo.sp_syspolicy_delete_condition, dbo.sp_syspolicy_delete_object_set, dbo.sp_syspolicy_delete_policy, dbo.sp_syspolicy_mark_system, dbo.sysjobs_view, dbo.syspolicy_policies, dbo.syspolicy_target_set_levels, dbo.syspolicy_target_sets, dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_configuration_internal, dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_filegroups_with_policy_violations_internal, dbo.sysutility_ucp_health_policies_internal, dbo.sysutility_ucp_managed_instances, dbo.sysutility_ucp_mi_database_health_internal, dbo.sysutility_ucp_mi_file_space_health_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policies, dbo.sysutility_ucp_policy_violations_internal, dbo.sysutility_ucp_processing_state_internal, dbo.sysutility_ucp_snapshot_partitions_internal, dbo.xp_instance_regdeletekey, dbo.xp_instance_regdeletevalue, dbo.xp_instance_regread, sysutility_ucp_misc.utility_objects_internal |
| dbo | [sp_sysutility_ucp_remove_mi](dbo.sp_sysutility_ucp_remove_mi.md) | dbo.sp_sysutility_ucp_calculate_aggregated_dac_health, dbo.sp_sysutility_ucp_calculate_aggregated_mi_health, dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_managed_instances_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_processing_state_internal |
| dbo | [sp_sysutility_ucp_update_policy](dbo.sp_sysutility_ucp_update_policy.md) | dbo.sysutility_ucp_health_policies_internal |
| dbo | [sp_sysutility_ucp_update_utility_configuration](dbo.sp_sysutility_ucp_update_utility_configuration.md) | dbo.sysutility_ucp_configuration_internal |
| dbo | [sp_sysutility_ucp_validate_prerequisites](dbo.sp_sysutility_ucp_validate_prerequisites.md) | dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal |
| dbo | [sp_target_server_summary](dbo.sp_target_server_summary.md) | dbo.sysdownloadlist, dbo.systargetservers |
| dbo | [sp_uniquetaskname](dbo.sp_uniquetaskname.md) | dbo.sysjobs |
| dbo | [sp_update_alert](dbo.sp_update_alert.md) | dbo.sp_is_sqlagent_starting, dbo.sp_sqlagent_notify, dbo.sp_verify_alert, dbo.sysalerts, dbo.syscategories, dbo.sysjobs_view |
| dbo | [sp_update_category](dbo.sp_update_category.md) | dbo.sp_verify_category, dbo.syscategories |
| dbo | [sp_update_job](dbo.sp_update_job.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_has_server_access, dbo.sp_sqlagent_notify, dbo.sp_verify_job, dbo.sp_verify_job_identifiers, dbo.SQLAGENT_SUSER_SNAME, dbo.sysalerts, dbo.syscategories, dbo.sysjobs, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoperators |
| dbo | [sp_update_jobschedule](dbo.sp_update_jobschedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_update_replication_job_parameter, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sp_verify_schedule, dbo.sysjobs, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysoriginatingservers_view, dbo.sysschedules, dbo.sysschedules_localserver_view |
| dbo | [sp_update_jobstep](dbo.sp_update_jobstep.md) | dbo.sp_post_msx_operation, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sp_verify_jobstep, dbo.sp_verify_proxy_identifiers, dbo.sysjobs, dbo.sysjobservers, dbo.sysjobsteps |
| dbo | [sp_update_log_shipping_monitor_info](dbo.sp_update_log_shipping_monitor_info.md) | dbo.log_shipping_primaries, dbo.log_shipping_secondaries |
| dbo | [sp_update_notification](dbo.sp_update_notification.md) | dbo.sp_sqlagent_notify, dbo.sp_verify_notification, dbo.sysalerts, dbo.sysnotifications |
| dbo | [sp_update_operator](dbo.sp_update_operator.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_operator, dbo.syscategories, dbo.sysoperators, dbo.systargetservers, dbo.xp_instance_regread, dbo.xp_instance_regwrite |
| dbo | [sp_update_proxy](dbo.sp_update_proxy.md) | dbo.sp_verify_credential_identifiers, dbo.sp_verify_proxy_identifiers, dbo.sysproxies |
| dbo | [sp_update_replication_job_parameter](dbo.sp_update_replication_job_parameter.md) | dbo.sysjobs, dbo.sysjobsteps |
| dbo | [sp_update_schedule](dbo.sp_update_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_update_replication_job_parameter, dbo.sp_verify_schedule, dbo.sp_verify_schedule_identifiers, dbo.SQLAGENT_SUSER_SID, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysschedules |
| dbo | [sp_update_targetservergroup](dbo.sp_update_targetservergroup.md) | dbo.systargetservergroups |
| dbo | [sp_validate_user](dbo.sp_validate_user.md) | dbo.sysmail_principalprofile, dbo.xp_logininfo |
| dbo | [sp_verify_alert](dbo.sp_verify_alert.md) | dbo.sp_sqlagent_notify, dbo.sp_verify_job_date, dbo.sp_verify_job_identifiers, dbo.sp_verify_job_time, dbo.sp_verify_performance_condition, dbo.sysalerts, dbo.syscategories, dbo.sysjobservers, dbo.xp_instance_regread |
| dbo | [sp_verify_category](dbo.sp_verify_category.md) |  |
| dbo | [sp_verify_category_identifiers](dbo.sp_verify_category_identifiers.md) | dbo.syscategories |
| dbo | [sp_verify_credential_identifiers](dbo.sp_verify_credential_identifiers.md) |  |
| dbo | [sp_verify_job](dbo.sp_verify_job.md) | dbo.syscategories, dbo.sysjobs, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoperators, dbo.sysoriginatingservers_view, dbo.systargetservers |
| dbo | [sp_verify_job_date](dbo.sp_verify_job_date.md) |  |
| dbo | [sp_verify_job_identifiers](dbo.sp_verify_job_identifiers.md) | dbo.sp_is_sqlagent_starting, dbo.sysjobs_view |
| dbo | [sp_verify_job_time](dbo.sp_verify_job_time.md) |  |
| dbo | [sp_verify_jobproc_caller](dbo.sp_verify_jobproc_caller.md) | dbo.sysjobs_view |
| dbo | [sp_verify_jobstep](dbo.sp_verify_jobstep.md) | dbo.sp_verify_proxy_permissions, dbo.sp_verify_subsystem, dbo.sysjobs, dbo.sysjobservers, dbo.sysjobsteps |
| dbo | [sp_verify_login_identifiers](dbo.sp_verify_login_identifiers.md) |  |
| dbo | [sp_verify_notification](dbo.sp_verify_notification.md) | dbo.sysalerts, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_verify_operator](dbo.sp_verify_operator.md) | dbo.sp_verify_job_time, dbo.syscategories, dbo.sysoperators |
| dbo | [sp_verify_operator_identifiers](dbo.sp_verify_operator_identifiers.md) | dbo.sysoperators |
| dbo | [sp_verify_performance_condition](dbo.sp_verify_performance_condition.md) | dbo.sysalerts_performance_counters_view |
| dbo | [sp_verify_proxy](dbo.sp_verify_proxy.md) | dbo.sysproxies |
| dbo | [sp_verify_proxy_identifiers](dbo.sp_verify_proxy_identifiers.md) | dbo.sysproxies |
| dbo | [sp_verify_proxy_permissions](dbo.sp_verify_proxy_permissions.md) | dbo.get_principal_id, dbo.sp_sqlagent_is_member, dbo.sp_sqlagent_is_srvrolemember, dbo.sysproxies, dbo.sysproxyloginsubsystem_view, dbo.sysproxysubsystem, dbo.syssubsystems |
| dbo | [sp_verify_schedule](dbo.sp_verify_schedule.md) | dbo.sp_verify_job_date, dbo.sp_verify_job_time |
| dbo | [sp_verify_schedule_identifiers](dbo.sp_verify_schedule_identifiers.md) | dbo.sysjobschedules, dbo.sysoriginatingservers_view, dbo.sysschedules, dbo.sysschedules_localserver_view |
| dbo | [sp_verify_subsystem](dbo.sp_verify_subsystem.md) | dbo.sp_verify_subsystems, dbo.syssubsystems |
| dbo | [sp_verify_subsystem_identifiers](dbo.sp_verify_subsystem_identifiers.md) | dbo.sp_verify_subsystems, dbo.syssubsystems |
| dbo | [sp_verify_subsystems](dbo.sp_verify_subsystems.md) | dbo.syssubsystems, dbo.xp_instance_regread, dbo.xp_msver, dbo.xp_regread |
| dbo | [sp_write_sysjobstep_log](dbo.sp_write_sysjobstep_log.md) | dbo.sp_delete_jobsteplog, dbo.sysjobsteps, dbo.sysjobstepslogs |
| dbo | [sysmail_add_account_sp](dbo.sysmail_add_account_sp.md) | dbo.sysmail_account, dbo.sysmail_create_user_credential_sp, dbo.sysmail_server, dbo.sysmail_verify_accountparams_sp, dbo.sysmail_verify_addressparams_sp |
| dbo | [sysmail_add_principalprofile_sp](dbo.sysmail_add_principalprofile_sp.md) | dbo.sysmail_principalprofile, dbo.sysmail_verify_principal_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_add_profile_sp](dbo.sysmail_add_profile_sp.md) | dbo.sysmail_profile |
| dbo | [sysmail_add_profileaccount_sp](dbo.sysmail_add_profileaccount_sp.md) | dbo.sysmail_profileaccount, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_alter_user_credential_sp](dbo.sysmail_alter_user_credential_sp.md) |  |
| dbo | [sysmail_configure_sp](dbo.sysmail_configure_sp.md) | dbo.sysmail_configuration |
| dbo | [sysmail_create_user_credential_sp](dbo.sysmail_create_user_credential_sp.md) |  |
| dbo | [sysmail_delete_account_sp](dbo.sysmail_delete_account_sp.md) | dbo.sysmail_account, dbo.sysmail_drop_user_credential_sp, dbo.sysmail_server, dbo.sysmail_verify_account_sp |
| dbo | [sysmail_delete_log_sp](dbo.sysmail_delete_log_sp.md) | dbo.sysmail_log |
| dbo | [sysmail_delete_mailitems_sp](dbo.sysmail_delete_mailitems_sp.md) | dbo.sysmail_allitems, dbo.sysmail_logmailevent_sp |
| dbo | [sysmail_delete_principalprofile_sp](dbo.sysmail_delete_principalprofile_sp.md) | dbo.sysmail_principalprofile, dbo.sysmail_verify_principal_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_delete_profile_sp](dbo.sysmail_delete_profile_sp.md) | dbo.sysmail_mailitems, dbo.sysmail_profile, dbo.sysmail_unsentitems, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_delete_profileaccount_sp](dbo.sysmail_delete_profileaccount_sp.md) | dbo.sysmail_profileaccount, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_drop_user_credential_sp](dbo.sysmail_drop_user_credential_sp.md) |  |
| dbo | [sysmail_help_account_sp](dbo.sysmail_help_account_sp.md) | dbo.sysmail_account, dbo.sysmail_server, dbo.sysmail_verify_account_sp |
| dbo | [sysmail_help_admin_account_sp](dbo.sysmail_help_admin_account_sp.md) | dbo.sysmail_account, dbo.sysmail_server, dbo.sysmail_verify_account_sp |
| dbo | [sysmail_help_configure_sp](dbo.sysmail_help_configure_sp.md) | dbo.sysmail_configuration |
| dbo | [sysmail_help_configure_value_sp](dbo.sysmail_help_configure_value_sp.md) | dbo.sysmail_configuration |
| dbo | [sysmail_help_principalprofile_sp](dbo.sysmail_help_principalprofile_sp.md) | dbo.get_principal_id, dbo.sysmail_principalprofile, dbo.sysmail_profile, dbo.sysmail_verify_principal_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_help_profile_sp](dbo.sysmail_help_profile_sp.md) | dbo.sysmail_profile, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_help_profileaccount_sp](dbo.sysmail_help_profileaccount_sp.md) | dbo.sysmail_account, dbo.sysmail_profile, dbo.sysmail_profileaccount, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_help_queue_sp](dbo.sysmail_help_queue_sp.md) | dbo.ExternalMailQueue, dbo.InternalMailQueue |
| dbo | [sysmail_help_status_sp](dbo.sysmail_help_status_sp.md) |  |
| dbo | [sysmail_logmailevent_sp](dbo.sysmail_logmailevent_sp.md) | dbo.ConvertToInt, dbo.sysmail_help_configure_value_sp, dbo.sysmail_log |
| dbo | [sysmail_start_sp](dbo.sysmail_start_sp.md) | dbo.sysmail_logmailevent_sp |
| dbo | [sysmail_stop_sp](dbo.sysmail_stop_sp.md) | dbo.sysmail_logmailevent_sp |
| dbo | [sysmail_update_account_sp](dbo.sysmail_update_account_sp.md) | dbo.sysmail_account, dbo.sysmail_alter_user_credential_sp, dbo.sysmail_create_user_credential_sp, dbo.sysmail_drop_user_credential_sp, dbo.sysmail_server, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_accountparams_sp, dbo.sysmail_verify_addressparams_sp |
| dbo | [sysmail_update_principalprofile_sp](dbo.sysmail_update_principalprofile_sp.md) | dbo.sysmail_principalprofile, dbo.sysmail_verify_principal_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_update_profile_sp](dbo.sysmail_update_profile_sp.md) | dbo.sysmail_profile, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_update_profileaccount_sp](dbo.sysmail_update_profileaccount_sp.md) | dbo.sysmail_profileaccount, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_verify_account_sp](dbo.sysmail_verify_account_sp.md) | dbo.sysmail_account |
| dbo | [sysmail_verify_accountparams_sp](dbo.sysmail_verify_accountparams_sp.md) |  |
| dbo | [sysmail_verify_addressparams_sp](dbo.sysmail_verify_addressparams_sp.md) |  |
| dbo | [sysmail_verify_principal_sp](dbo.sysmail_verify_principal_sp.md) | dbo.get_principal_sid |
| dbo | [sysmail_verify_profile_sp](dbo.sysmail_verify_profile_sp.md) | dbo.sysmail_profile |
