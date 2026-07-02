# Views: msdb

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [sysalerts_performance_counters_view](dbo.sysalerts_performance_counters_view.md) |  |
| dbo | [syscollector_execution_log](dbo.syscollector_execution_log.md) | dbo.fn_syscollector_get_package_path, dbo.syscollector_execution_log_internal |
| dbo | [syscollector_execution_log_full](dbo.syscollector_execution_log_full.md) | dbo.fn_syscollector_get_execution_log_tree, dbo.syscollector_collection_sets, dbo.syscollector_execution_log_internal, dbo.sysssispackages |
| dbo | [syscollector_execution_stats](dbo.syscollector_execution_stats.md) | dbo.syscollector_execution_stats_internal |
| dbo | [sysdtslog90](dbo.sysdtslog90.md) | dbo.sysssislog |
| dbo | [sysmail_allitems](dbo.sysmail_allitems.md) | dbo.sysmail_mailitems |
| dbo | [sysmail_event_log](dbo.sysmail_event_log.md) | dbo.sysmail_allitems, dbo.sysmail_log |
| dbo | [sysmail_faileditems](dbo.sysmail_faileditems.md) | dbo.sysmail_allitems |
| dbo | [sysmail_mailattachments](dbo.sysmail_mailattachments.md) | dbo.sysmail_attachments, dbo.sysmail_mailitems |
| dbo | [sysmail_sentitems](dbo.sysmail_sentitems.md) | dbo.sysmail_allitems |
| dbo | [sysmail_unsentitems](dbo.sysmail_unsentitems.md) | dbo.sysmail_allitems |
| dbo | [syspolicy_policy_execution_history](dbo.syspolicy_policy_execution_history.md) | dbo.syspolicy_policy_execution_history_internal |
| dbo | [syspolicy_policy_execution_history_details](dbo.syspolicy_policy_execution_history_details.md) | dbo.syspolicy_policy_execution_history_details_internal |
| dbo | [syspolicy_system_health_state](dbo.syspolicy_system_health_state.md) | dbo.syspolicy_system_health_state_internal |
| dbo | [sysutility_ucp_computer_cpu_utilizations](dbo.sysutility_ucp_computer_cpu_utilizations.md) | dbo.sysutility_ucp_computers |
| dbo | [sysutility_ucp_dac_cpu_utilizations](dbo.sysutility_ucp_dac_cpu_utilizations.md) | dbo.sysutility_ucp_deployed_dacs |
| dbo | [sysutility_ucp_dac_database_file_space_utilizations](dbo.sysutility_ucp_dac_database_file_space_utilizations.md) | dbo.sysutility_ucp_database_files, dbo.sysutility_ucp_deployed_dacs |
| dbo | [sysutility_ucp_dac_volume_space_utilizations](dbo.sysutility_ucp_dac_volume_space_utilizations.md) | dbo.sysutility_ucp_deployed_dacs, dbo.sysutility_ucp_volumes |
| dbo | [sysutility_ucp_databases](dbo.sysutility_ucp_databases.md) | dbo.syn_sysutility_ucp_databases |
| dbo | [sysutility_ucp_filegroups](dbo.sysutility_ucp_filegroups.md) | dbo.syn_sysutility_ucp_filegroups |
| dbo | [sysutility_ucp_mi_cpu_utilizations](dbo.sysutility_ucp_mi_cpu_utilizations.md) | dbo.sysutility_ucp_instances |
| dbo | [sysutility_ucp_mi_database_file_space_utilizations](dbo.sysutility_ucp_mi_database_file_space_utilizations.md) | dbo.sysutility_ucp_database_files |
| dbo | [sysutility_ucp_mi_volume_space_utilizations](dbo.sysutility_ucp_mi_volume_space_utilizations.md) | dbo.sysutility_ucp_instances, dbo.sysutility_ucp_volumes |
| dbo | [sysutility_ucp_policy_violations](dbo.sysutility_ucp_policy_violations.md) | dbo.sysutility_ucp_policy_violations_internal |
| dbo | [sysutility_ucp_volumes](dbo.sysutility_ucp_volumes.md) | dbo.syn_sysutility_ucp_volumes |
