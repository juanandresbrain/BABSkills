# Stored Procedures: msdb

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [autoadmin_fetch_system_flags](dbo.autoadmin_fetch_system_flags.md) | dbo.autoadmin_system_flags, managed_backup.fn_backup_db_config, managed_backup.fn_backup_instance_config, smart_admin.fn_backup_db_config, smart_admin.fn_backup_instance_config |
| dbo | [autoadmin_metadata_delete_task_agent_data_for_database](dbo.autoadmin_metadata_delete_task_agent_data_for_database.md) | dbo.autoadmin_managed_databases, dbo.autoadmin_task_agent_metadata |
| dbo | [autoadmin_metadata_delete_task_agent_global_data](dbo.autoadmin_metadata_delete_task_agent_global_data.md) | dbo.autoadmin_task_agent_metadata |
| dbo | [autoadmin_metadata_insert_task_agent_global_data](dbo.autoadmin_metadata_insert_task_agent_global_data.md) | dbo.autoadmin_task_agent_metadata |
| dbo | [autoadmin_metadata_query_dbs](dbo.autoadmin_metadata_query_dbs.md) | dbo.autoadmin_managed_databases, dbo.autoadmin_task_agent_metadata |
| dbo | [autoadmin_metadata_query_task_agent_global_data](dbo.autoadmin_metadata_query_task_agent_global_data.md) | dbo.autoadmin_task_agent_metadata, dbo.fn_autoadmin_schema_version |
| dbo | [autoadmin_metadata_update_task_agent_data_for_database](dbo.autoadmin_metadata_update_task_agent_data_for_database.md) | dbo.autoadmin_managed_databases, dbo.autoadmin_task_agent_metadata |
| dbo | [autoadmin_metadata_update_task_agent_global_data](dbo.autoadmin_metadata_update_task_agent_global_data.md) | dbo.autoadmin_task_agent_metadata |
| dbo | [autoadmin_restore_headeronly](dbo.autoadmin_restore_headeronly.md) |  |
| dbo | [autoadmin_set_master_switch](dbo.autoadmin_set_master_switch.md) | dbo.autoadmin_master_switch |
| dbo | [autoadmin_set_system_flag](dbo.autoadmin_set_system_flag.md) | dbo.autoadmin_system_flags, dbo.sp_autoadmin_configure_notification |
| dbo | [sp_add_jobserver](dbo.sp_add_jobserver.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_has_server_access, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.SQLAGENT_SUSER_SNAME, dbo.syscategories, dbo.sysjobs, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_add_proxy](dbo.sp_add_proxy.md) | dbo.sp_verify_credential_identifiers, dbo.sp_verify_proxy, dbo.sysproxies |
| dbo | [sp_add_schedule](dbo.sp_add_schedule.md) | dbo.sp_verify_schedule, dbo.SQLAGENT_SUSER_SID, dbo.sysoriginatingservers_view, dbo.sysschedules |
| dbo | [sp_agent_add_job](dbo.sp_agent_add_job.md) |  |
| dbo | [sp_agent_add_jobstep](dbo.sp_agent_add_jobstep.md) |  |
| dbo | [sp_agent_delete_job](dbo.sp_agent_delete_job.md) | dbo.sp_delete_job |
| dbo | [sp_agent_get_jobstep](dbo.sp_agent_get_jobstep.md) | dbo.sp_help_jobstep |
| dbo | [sp_agent_start_job](dbo.sp_agent_start_job.md) |  |
| dbo | [sp_agent_write_sysjobstep_log](dbo.sp_agent_write_sysjobstep_log.md) | dbo.sp_write_sysjobstep_log |
| dbo | [sp_attach_schedule](dbo.sp_attach_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysmaintplan_subplans |
| dbo | [sp_autoadmin_configure_notification](dbo.sp_autoadmin_configure_notification.md) | dbo.sp_autoadmin_create_notification_job, dbo.xp_instance_regread |
| dbo | [sp_autoadmin_create_notification_job](dbo.sp_autoadmin_create_notification_job.md) | dbo.sp_add_job, dbo.sp_add_jobschedule, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_attach_schedule, dbo.sp_delete_job, dbo.sp_update_job, dbo.sysjobs, dbo.sysschedules |
| dbo | [sp_autoadmin_notification_job_send_email](dbo.sp_autoadmin_notification_job_send_email.md) | dbo.autoadmin_system_flags, dbo.sp_send_dbmail, dbo.vw_autoadmin_health_status |
| dbo | [sp_check_smartadmin_notification_enabled](dbo.sp_check_smartadmin_notification_enabled.md) | dbo.autoadmin_system_flags, smart_admin.fn_is_master_switch_on |
| dbo | [sp_cycle_agent_errorlog](dbo.sp_cycle_agent_errorlog.md) | dbo.sp_sqlagent_notify |
| dbo | [sp_delete_proxy](dbo.sp_delete_proxy.md) | dbo.sp_verify_proxy_identifiers, dbo.sysjobsteps, dbo.sysproxies, dbo.sysproxylogin, dbo.sysproxysubsystem |
| dbo | [sp_delete_schedule](dbo.sp_delete_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysschedules |
| dbo | [sp_detach_schedule](dbo.sp_detach_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_verify_job_identifiers, dbo.sp_verify_jobproc_caller, dbo.sp_verify_schedule_identifiers, dbo.sysjobs, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysmaintplan_subplans, dbo.sysschedules |
| dbo | [sp_droptask](dbo.sp_droptask.md) | dbo.sp_delete_job, dbo.sp_manage_jobs_by_login, dbo.sysjobs_view, dbo.systaskids |
| dbo | [sp_DTA_delete_session](dbo.sp_DTA_delete_session.md) | dbo.DTA_input, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_get_tuninglog](dbo.sp_DTA_get_tuninglog.md) | dbo.DTA_input, dbo.DTA_tuninglog, dbo.sp_DTA_check_permission |
| dbo | [sp_DTA_help_session](dbo.sp_DTA_help_session.md) | dbo.DTA_input, dbo.DTA_output, dbo.DTA_progress, dbo.DTA_reports_database, dbo.sp_DTA_check_permission |
| dbo | [sp_enlist_tsx](dbo.sp_enlist_tsx.md) | dbo.sp_delete_targetserver, dbo.sysdownloadlist, dbo.sysoperators, dbo.systargetservers, dbo.xp_instance_regread |
| dbo | [sp_enum_login_for_proxy](dbo.sp_enum_login_for_proxy.md) | dbo.get_principal_id, dbo.sp_verify_proxy_identifiers, dbo.sysproxies, dbo.sysproxylogin |
| dbo | [sp_enum_proxy_for_subsystem](dbo.sp_enum_proxy_for_subsystem.md) | dbo.sp_verify_proxy_identifiers, dbo.sp_verify_subsystem_identifiers, dbo.sysproxies, dbo.sysproxysubsystem, dbo.syssubsystems |
| dbo | [sp_get_traceflag_status_internal](dbo.sp_get_traceflag_status_internal.md) |  |
| dbo | [sp_GetAttachmentData](dbo.sp_GetAttachmentData.md) | dbo.ConvertToInt, dbo.sp_isprohibited, dbo.sysmail_help_configure_value_sp |
| dbo | [sp_help_jobcount](dbo.sp_help_jobcount.md) | dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules |
| dbo | [sp_help_jobhistory_sem](dbo.sp_help_jobhistory_sem.md) | dbo.sysjobhistory, dbo.sysjobs_view, dbo.sysjobservers, dbo.sysoperators, dbo.systargetservers |
| dbo | [sp_help_jobs_in_schedule](dbo.sp_help_jobs_in_schedule.md) | dbo.sp_get_composite_job_info, dbo.sp_verify_schedule_identifiers |
| dbo | [sp_help_jobschedule](dbo.sp_help_jobschedule.md) | dbo.sp_get_schedule_description, dbo.sp_verify_job_identifiers, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysschedules |
| dbo | [sp_help_proxy](dbo.sp_help_proxy.md) | dbo.sp_verify_proxy_identifiers, dbo.sp_verify_proxy_permissions, dbo.sp_verify_subsystem_identifiers, dbo.sp_verify_subsystems, dbo.sysproxies, dbo.syssubsystems |
| dbo | [sp_help_schedule](dbo.sp_help_schedule.md) | dbo.sp_get_schedule_description, dbo.sp_verify_schedule_identifiers, dbo.sysjobschedules, dbo.sysschedules_localserver_view |
| dbo | [sp_log_shipping_monitor_backup](dbo.sp_log_shipping_monitor_backup.md) | dbo.log_shipping_primaries, dbo.sp_log_shipping_in_sync |
| dbo | [sp_read_settings](dbo.sp_read_settings.md) |  |
| dbo | [sp_readrequest](dbo.sp_readrequest.md) | dbo.ExternalMailQueue, dbo.sp_MailItemResultSets, dbo.sp_process_DialogTimer, dbo.sysmail_logmailevent_sp, dbo.sysmail_mailitems, Properties.value |
| dbo | [sp_remove_log_shipping_monitor_account](dbo.sp_remove_log_shipping_monitor_account.md) |  |
| dbo | [sp_revoke_login_from_proxy](dbo.sp_revoke_login_from_proxy.md) | dbo.sp_sqlagent_is_srvrolemember, dbo.sp_verify_proxy_identifiers, dbo.sysproxylogin |
| dbo | [sp_revoke_proxy_from_subsystem](dbo.sp_revoke_proxy_from_subsystem.md) | dbo.sp_verify_proxy_identifiers, dbo.sp_verify_subsystem_identifiers, dbo.sysproxysubsystem |
| dbo | [sp_RunMailQuery](dbo.sp_RunMailQuery.md) | dbo.ConvertToInt, dbo.sp_isprohibited, dbo.sysmail_help_configure_value_sp |
| dbo | [sp_set_sqlagent_properties](dbo.sp_set_sqlagent_properties.md) | dbo.sp_sqlagent_notify, dbo.xp_instance_regdeletevalue, dbo.xp_instance_regread, dbo.xp_instance_regwrite, dbo.xp_regwrite |
| dbo | [sp_sqlagent_is_member](dbo.sp_sqlagent_is_member.md) |  |
| dbo | [sp_sqlagent_is_srvrolemember](dbo.sp_sqlagent_is_srvrolemember.md) |  |
| dbo | [sp_syscollector_event_oncollectionbegin](dbo.sp_syscollector_event_oncollectionbegin.md) | dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_oncollectionend](dbo.sp_syscollector_event_oncollectionend.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_oncollectionstart](dbo.sp_syscollector_event_oncollectionstart.md) | dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_oncollectionstop](dbo.sp_syscollector_event_oncollectionstop.md) | dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_onerror](dbo.sp_syscollector_event_onerror.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log, dbo.syscollector_execution_log_internal, dbo.sysssislog |
| dbo | [sp_syscollector_event_onpackagebegin](dbo.sp_syscollector_event_onpackagebegin.md) | dbo.syscollector_execution_log, dbo.syscollector_execution_log_internal, dbo.sysssispackages |
| dbo | [sp_syscollector_event_onpackageend](dbo.sp_syscollector_event_onpackageend.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_onpackageupdate](dbo.sp_syscollector_event_onpackageupdate.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_log_internal |
| dbo | [sp_syscollector_event_onstatsupdate](dbo.sp_syscollector_event_onstatsupdate.md) | dbo.sp_syscollector_verify_event_log_id, dbo.syscollector_execution_stats_internal |
| dbo | [sp_syscollector_get_query_activity_collection_item_params](dbo.sp_syscollector_get_query_activity_collection_item_params.md) | dbo.sp_syscollector_verify_collection_item, dbo.syscollector_collection_items, Properties.value |
| dbo | [sp_syscollector_snapshot_dm_exec_query_stats](dbo.sp_syscollector_snapshot_dm_exec_query_stats.md) | dbo.sp_syscollector_get_query_activity_collection_item_params, dbo.sp_syscollector_snapshot_dm_exec_query_stats_internal |
| dbo | [sp_syscollector_snapshot_dm_exec_query_stats_internal](dbo.sp_syscollector_snapshot_dm_exec_query_stats_internal.md) |  |
| dbo | [sp_syscollector_snapshot_dm_exec_requests](dbo.sp_syscollector_snapshot_dm_exec_requests.md) | dbo.sp_syscollector_get_query_activity_collection_item_params, dbo.sp_syscollector_snapshot_dm_exec_requests_internal |
| dbo | [sp_syscollector_snapshot_dm_exec_requests_internal](dbo.sp_syscollector_snapshot_dm_exec_requests_internal.md) |  |
| dbo | [sp_syscollector_start_collection_set_jobs](dbo.sp_syscollector_start_collection_set_jobs.md) | dbo.sp_start_job, dbo.sp_syscollector_event_oncollectionstart, dbo.sp_update_job, dbo.syscollector_collection_sets |
| dbo | [sp_syscollector_stop_collection_set_jobs](dbo.sp_syscollector_stop_collection_set_jobs.md) | dbo.sp_attach_schedule, dbo.sp_detach_schedule, dbo.sp_start_job, dbo.sp_syscollector_event_oncollectionstop, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_update_job, dbo.syscollector_collection_sets, dbo.sysschedules_localserver_view |
| dbo | [sp_syscollector_verify_event_log_id](dbo.sp_syscollector_verify_event_log_id.md) | dbo.syscollector_execution_log |
| dbo | [sp_sysdac_delete_history](dbo.sp_sysdac_delete_history.md) | dbo.sysdac_history_internal, dbo.sysdac_instances, dbo.sysdac_instances_internal |
| dbo | [sp_syspolicy_check_membership](dbo.sp_syspolicy_check_membership.md) |  |
| dbo | [sp_syspolicy_dispatch_event](dbo.sp_syspolicy_dispatch_event.md) | c.value, dbo.sp_syspolicy_check_membership, dbo.sp_syspolicy_dispatch_event, dbo.spt_values, dbo.syspolicy_conditions_internal, dbo.syspolicy_execution_internal, dbo.syspolicy_facet_events, dbo.syspolicy_policies, dbo.syspolicy_policy_categories, dbo.syspolicy_policy_category_subscriptions, dbo.syspolicy_target_set_levels, dbo.syspolicy_target_sets |
| dbo | [sp_sysutility_mi_configure_proxy_account](dbo.sp_sysutility_mi_configure_proxy_account.md) | dbo.sp_add_proxy, dbo.sp_delete_proxy, dbo.sp_grant_login_to_proxy, dbo.sp_grant_proxy_to_subsystem, dbo.sysproxies |
| dbo | [sp_sysutility_mi_create_cache_directory](dbo.sp_sysutility_mi_create_cache_directory.md) | dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_delete_job, dbo.sysjobs, dbo.xp_instance_regread |
| dbo | [sp_sysutility_mi_create_job_validate_wmi](dbo.sp_sysutility_mi_create_job_validate_wmi.md) | dbo.fn_sysutility_mi_get_validate_wmi_script, dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_delete_job, dbo.sysjobs |
| dbo | [sp_sysutility_mi_enroll](dbo.sp_sysutility_mi_enroll.md) | dbo.sp_sysutility_mi_validate_enrollment_preconditions |
| dbo | [sp_sysutility_mi_get_dac_execution_statistics_internal](dbo.sp_sysutility_mi_get_dac_execution_statistics_internal.md) | dbo.sysutility_batch_time_internal, dbo.sysutility_mi_dac_execution_statistics_internal |
| dbo | [sp_sysutility_mi_remove](dbo.sp_sysutility_mi_remove.md) | dbo.sp_syscollector_disable_collector, dbo.sp_syscollector_enable_collector, dbo.sp_syscollector_get_collection_set_execution_status, dbo.sp_syscollector_set_cache_directory, dbo.sp_syscollector_stop_collection_set, dbo.sp_syscollector_update_collection_set, dbo.sp_sysutility_mi_disable_collection, dbo.sp_sysutility_mi_remove_ucp_registration, dbo.syscollector_collection_sets, dbo.syscollector_config_store |
| dbo | [sp_sysutility_mi_validate_enrollment_preconditions](dbo.sp_sysutility_mi_validate_enrollment_preconditions.md) | dbo.xp_qv |
| dbo | [sp_sysutility_mi_validate_proxy_account](dbo.sp_sysutility_mi_validate_proxy_account.md) | dbo.sp_add_job, dbo.sp_add_jobserver, dbo.sp_add_jobstep, dbo.sp_add_proxy, dbo.sp_delete_job, dbo.sp_delete_proxy, dbo.sp_grant_proxy_to_subsystem, dbo.sysjobs, dbo.sysproxies |
| dbo | [sp_sysutility_ucp_add_mi](dbo.sp_sysutility_ucp_add_mi.md) | dbo.sysutility_ucp_managed_instances_internal |
| dbo | [sp_sysutility_ucp_calculate_aggregated_dac_health](dbo.sp_sysutility_ucp_calculate_aggregated_dac_health.md) | dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_dac_health_internal |
| dbo | [sp_sysutility_ucp_calculate_aggregated_mi_health](dbo.sp_sysutility_ucp_calculate_aggregated_mi_health.md) | dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_mi_health_internal |
| dbo | [sp_sysutility_ucp_calculate_computer_health](dbo.sp_sysutility_ucp_calculate_computer_health.md) | dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_computer_policies, dbo.sysutility_ucp_computers, dbo.sysutility_ucp_instances, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policy_violations, dbo.sysutility_ucp_volumes |
| dbo | [sp_sysutility_ucp_calculate_dac_file_space_health](dbo.sp_sysutility_ucp_calculate_dac_file_space_health.md) | dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_policies, dbo.sysutility_ucp_databases, dbo.sysutility_ucp_deployed_dacs, dbo.sysutility_ucp_filegroups, dbo.sysutility_ucp_filegroups_with_policy_violations_internal |
| dbo | [sp_sysutility_ucp_calculate_dac_health](dbo.sp_sysutility_ucp_calculate_dac_health.md) | dbo.fn_sysutility_ucp_get_aggregated_health, dbo.sp_sysutility_ucp_calculate_dac_file_space_health, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_dac_policies, dbo.sysutility_ucp_dac_policy_type, dbo.sysutility_ucp_datafiles, dbo.sysutility_ucp_deployed_dacs, dbo.sysutility_ucp_logfiles, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policy_violations |
| dbo | [sp_sysutility_ucp_calculate_health](dbo.sp_sysutility_ucp_calculate_health.md) | dbo.sp_sysutility_ucp_calculate_aggregated_dac_health, dbo.sp_sysutility_ucp_calculate_aggregated_mi_health, dbo.sp_sysutility_ucp_calculate_computer_health, dbo.sp_sysutility_ucp_calculate_dac_health, dbo.sp_sysutility_ucp_calculate_filegroups_with_policy_violations, dbo.sp_sysutility_ucp_calculate_mi_health, dbo.sp_sysutility_ucp_get_policy_violations, dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_filegroups_with_policy_violations_internal, dbo.sysutility_ucp_mi_database_health_internal, dbo.sysutility_ucp_mi_file_space_health_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_processing_state_internal |
| dbo | [sp_sysutility_ucp_calculate_mi_file_space_health](dbo.sp_sysutility_ucp_calculate_mi_file_space_health.md) | dbo.sysutility_ucp_databases, dbo.sysutility_ucp_filegroups, dbo.sysutility_ucp_filegroups_with_policy_violations_internal, dbo.sysutility_ucp_instance_policies, dbo.sysutility_ucp_instances, dbo.sysutility_ucp_mi_database_health_internal, dbo.sysutility_ucp_mi_file_space_health_internal |
| dbo | [sp_sysutility_ucp_calculate_mi_health](dbo.sp_sysutility_ucp_calculate_mi_health.md) | dbo.fn_sysutility_ucp_get_aggregated_health, dbo.sp_sysutility_ucp_calculate_mi_file_space_health, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_datafiles, dbo.sysutility_ucp_instance_policies, dbo.sysutility_ucp_instance_policy_type, dbo.sysutility_ucp_instances, dbo.sysutility_ucp_logfiles, dbo.sysutility_ucp_managed_instances, dbo.sysutility_ucp_mi_file_space_health_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policy_violations |
| dbo | [sp_sysutility_ucp_create](dbo.sp_sysutility_ucp_create.md) | dbo.sp_sysutility_ucp_validate_prerequisites |
| dbo | [sp_sysutility_ucp_delete_policy_history](dbo.sp_sysutility_ucp_delete_policy_history.md) | dbo.sysutility_ucp_configuration_internal, dbo.sysutility_ucp_processing_state_internal |
| dbo | [sp_sysutility_ucp_initialize](dbo.sp_sysutility_ucp_initialize.md) | dbo.sysutility_ucp_configuration_internal, dbo.xp_instance_regwrite |
| dbo | [sp_sysutility_ucp_initialize_mdw](dbo.sp_sysutility_ucp_initialize_mdw.md) | dbo.fn_sysutility_get_is_instance_ucp, dbo.sp_sysutility_ucp_recreate_synonym_internal |
| dbo | [sp_sysutility_ucp_provision_proxy_account](dbo.sp_sysutility_ucp_provision_proxy_account.md) | dbo.sp_sqlagent_has_server_access |
| dbo | [sp_sysutility_ucp_provision_utility_object_internal](dbo.sp_sysutility_ucp_provision_utility_object_internal.md) |  |
| dbo | [sp_sysutility_ucp_recreate_synonym_internal](dbo.sp_sysutility_ucp_recreate_synonym_internal.md) |  |
| dbo | [sp_sysutility_ucp_remove](dbo.sp_sysutility_ucp_remove.md) | core.source_info_internal, dbo.fn_sysutility_get_is_instance_ucp, dbo.sp_delete_job, dbo.sp_syspolicy_delete_condition, dbo.sp_syspolicy_delete_object_set, dbo.sp_syspolicy_delete_policy, dbo.sp_syspolicy_mark_system, dbo.sysjobs_view, dbo.syspolicy_policies, dbo.syspolicy_target_set_levels, dbo.syspolicy_target_sets, dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_computer_cpu_health_internal, dbo.sysutility_ucp_configuration_internal, dbo.sysutility_ucp_dac_file_space_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_filegroups_with_policy_violations_internal, dbo.sysutility_ucp_health_policies_internal, dbo.sysutility_ucp_managed_instances, dbo.sysutility_ucp_mi_database_health_internal, dbo.sysutility_ucp_mi_file_space_health_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_mi_volume_space_health_internal, dbo.sysutility_ucp_policies, dbo.sysutility_ucp_policy_violations_internal, dbo.sysutility_ucp_processing_state_internal, dbo.sysutility_ucp_snapshot_partitions_internal, dbo.xp_instance_regdeletekey, dbo.xp_instance_regdeletevalue, dbo.xp_instance_regread, sysutility_ucp_misc.utility_objects_internal |
| dbo | [sp_sysutility_ucp_remove_mi](dbo.sp_sysutility_ucp_remove_mi.md) | dbo.sp_sysutility_ucp_calculate_aggregated_dac_health, dbo.sp_sysutility_ucp_calculate_aggregated_mi_health, dbo.sysutility_ucp_aggregated_dac_health_internal, dbo.sysutility_ucp_aggregated_mi_health_internal, dbo.sysutility_ucp_dac_health_internal, dbo.sysutility_ucp_managed_instances_internal, dbo.sysutility_ucp_mi_health_internal, dbo.sysutility_ucp_processing_state_internal |
| dbo | [sp_sysutility_ucp_validate_prerequisites](dbo.sp_sysutility_ucp_validate_prerequisites.md) | dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal |
| dbo | [sp_update_proxy](dbo.sp_update_proxy.md) | dbo.sp_verify_credential_identifiers, dbo.sp_verify_proxy_identifiers, dbo.sysproxies |
| dbo | [sp_update_schedule](dbo.sp_update_schedule.md) | dbo.sp_post_msx_operation, dbo.sp_sqlagent_notify, dbo.sp_update_replication_job_parameter, dbo.sp_verify_schedule, dbo.sp_verify_schedule_identifiers, dbo.SQLAGENT_SUSER_SID, dbo.sysjobschedules, dbo.sysjobservers, dbo.sysschedules |
| dbo | [sp_verify_category_identifiers](dbo.sp_verify_category_identifiers.md) | dbo.syscategories |
| dbo | [sp_verify_credential_identifiers](dbo.sp_verify_credential_identifiers.md) |  |
| dbo | [sp_verify_job](dbo.sp_verify_job.md) | dbo.syscategories, dbo.sysjobs, dbo.sysjobservers, dbo.sysjobsteps, dbo.sysoperators, dbo.sysoriginatingservers_view, dbo.systargetservers |
| dbo | [sp_verify_job_time](dbo.sp_verify_job_time.md) |  |
| dbo | [sp_verify_login_identifiers](dbo.sp_verify_login_identifiers.md) |  |
| dbo | [sp_verify_operator_identifiers](dbo.sp_verify_operator_identifiers.md) | dbo.sysoperators |
| dbo | [sp_verify_proxy](dbo.sp_verify_proxy.md) | dbo.sysproxies |
| dbo | [sp_verify_proxy_identifiers](dbo.sp_verify_proxy_identifiers.md) | dbo.sysproxies |
| dbo | [sp_verify_subsystem_identifiers](dbo.sp_verify_subsystem_identifiers.md) | dbo.sp_verify_subsystems, dbo.syssubsystems |
| dbo | [sp_verify_subsystems](dbo.sp_verify_subsystems.md) | dbo.syssubsystems, dbo.xp_regread |
| dbo | [sysmail_add_account_sp](dbo.sysmail_add_account_sp.md) | dbo.sysmail_account, dbo.sysmail_create_user_credential_sp, dbo.sysmail_server, dbo.sysmail_verify_accountparams_sp, dbo.sysmail_verify_addressparams_sp |
| dbo | [sysmail_add_principalprofile_sp](dbo.sysmail_add_principalprofile_sp.md) | dbo.sysmail_principalprofile, dbo.sysmail_verify_principal_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_add_profile_sp](dbo.sysmail_add_profile_sp.md) | dbo.sysmail_profile |
| dbo | [sysmail_add_profileaccount_sp](dbo.sysmail_add_profileaccount_sp.md) | dbo.sysmail_profileaccount, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_alter_user_credential_sp](dbo.sysmail_alter_user_credential_sp.md) |  |
| dbo | [sysmail_configure_sp](dbo.sysmail_configure_sp.md) | dbo.sysmail_configuration |
| dbo | [sysmail_create_user_credential_sp](dbo.sysmail_create_user_credential_sp.md) |  |
| dbo | [sysmail_delete_account_sp](dbo.sysmail_delete_account_sp.md) | dbo.sysmail_account, dbo.sysmail_drop_user_credential_sp, dbo.sysmail_server, dbo.sysmail_verify_account_sp |
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
| dbo | [sysmail_update_account_sp](dbo.sysmail_update_account_sp.md) | dbo.sysmail_account, dbo.sysmail_alter_user_credential_sp, dbo.sysmail_create_user_credential_sp, dbo.sysmail_drop_user_credential_sp, dbo.sysmail_server, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_accountparams_sp, dbo.sysmail_verify_addressparams_sp |
| dbo | [sysmail_update_principalprofile_sp](dbo.sysmail_update_principalprofile_sp.md) | dbo.sysmail_principalprofile, dbo.sysmail_verify_principal_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_update_profile_sp](dbo.sysmail_update_profile_sp.md) | dbo.sysmail_profile, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_update_profileaccount_sp](dbo.sysmail_update_profileaccount_sp.md) | dbo.sysmail_profileaccount, dbo.sysmail_verify_account_sp, dbo.sysmail_verify_profile_sp |
| dbo | [sysmail_verify_account_sp](dbo.sysmail_verify_account_sp.md) | dbo.sysmail_account |
| dbo | [sysmail_verify_accountparams_sp](dbo.sysmail_verify_accountparams_sp.md) |  |
| dbo | [sysmail_verify_addressparams_sp](dbo.sysmail_verify_addressparams_sp.md) |  |
| dbo | [sysmail_verify_principal_sp](dbo.sysmail_verify_principal_sp.md) | dbo.get_principal_sid |
| dbo | [sysmail_verify_profile_sp](dbo.sysmail_verify_profile_sp.md) | dbo.sysmail_profile |
| managed_backup | [sp_add_task_command](managed_backup.sp_add_task_command.md) | dbo.sp_agent_delete_job, dbo.sp_agent_start_job, managed_backup.sp_create_job |
| managed_backup | [sp_backup_config_basic](managed_backup.sp_backup_config_basic.md) | managed_backup.sp_add_task_command |
| managed_backup | [sp_backup_master_switch](managed_backup.sp_backup_master_switch.md) | managed_backup.sp_add_task_command |
| managed_backup | [sp_do_backup](managed_backup.sp_do_backup.md) | managed_backup.sp_get_encryption_option, managed_backup.sp_get_striping_option |
| managed_backup | [sp_get_backup_diagnostics](managed_backup.sp_get_backup_diagnostics.md) |  |
| managed_backup | [sp_get_encryption_option](managed_backup.sp_get_encryption_option.md) |  |
| managed_backup | [sp_get_striping_option](managed_backup.sp_get_striping_option.md) |  |
| smart_admin | [sp_add_task_command](smart_admin.sp_add_task_command.md) | managed_backup.sp_add_task_command |
| smart_admin | [sp_backup_master_switch](smart_admin.sp_backup_master_switch.md) | managed_backup.sp_backup_master_switch |
| smart_admin | [sp_backup_on_demand](smart_admin.sp_backup_on_demand.md) | managed_backup.sp_backup_on_demand |
| smart_admin | [sp_create_job](smart_admin.sp_create_job.md) | managed_backup.sp_create_job |
| smart_admin | [sp_do_backup](smart_admin.sp_do_backup.md) | managed_backup.sp_do_backup |
| smart_admin | [sp_get_backup_diagnostics](smart_admin.sp_get_backup_diagnostics.md) | managed_backup.sp_get_backup_diagnostics |
| smart_admin | [sp_get_encryption_option](smart_admin.sp_get_encryption_option.md) | managed_backup.sp_get_encryption_option |
| smart_admin | [sp_set_db_backup](smart_admin.sp_set_db_backup.md) | smart_admin.sp_add_task_command |
| smart_admin | [sp_set_instance_backup](smart_admin.sp_set_instance_backup.md) | smart_admin.sp_add_task_command |
| smart_admin | [sp_set_parameter](smart_admin.sp_set_parameter.md) | managed_backup.sp_set_parameter |
