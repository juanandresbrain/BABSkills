# Views: SSISDB

| Schema | View | Table Dependencies |
|---|---|---|
| catalog | [alwayson_replicas](catalog.alwayson_replicas.md) | internal.alwayson_support_state |
| catalog | [catalog_properties](catalog.catalog_properties.md) | internal.catalog_properties |
| catalog | [customized_logging_levels](catalog.customized_logging_levels.md) | internal.customized_logging_levels |
| catalog | [effective_object_permissions](catalog.effective_object_permissions.md) | internal.current_user_object_permissions, internal.object_folders, internal.object_permissions |
| catalog | [environment_references](catalog.environment_references.md) | internal.current_user_readable_projects, internal.environment_references |
| catalog | [environment_variables](catalog.environment_variables.md) | internal.current_user_readable_environments, internal.environment_variables |
| catalog | [environments](catalog.environments.md) | internal.current_user_readable_environments, internal.environments |
| catalog | [event_message_context](catalog.event_message_context.md) | internal.current_user_readable_operations, internal.event_message_context |
| catalog | [event_messages](catalog.event_messages.md) | internal.current_user_readable_operations, internal.event_messages, internal.operation_messages |
| catalog | [executable_statistics](catalog.executable_statistics.md) | internal.current_user_readable_operations, internal.executable_statistics |
| catalog | [executables](catalog.executables.md) | internal.current_user_readable_operations, internal.executable_statistics, internal.executables, internal.executions |
| catalog | [execution_component_phases](catalog.execution_component_phases.md) | internal.current_user_readable_operations, internal.execution_component_phases |
| catalog | [execution_data_statistics](catalog.execution_data_statistics.md) | internal.current_user_readable_operations, internal.execution_data_statistics |
| catalog | [execution_data_taps](catalog.execution_data_taps.md) | internal.current_user_readable_operations, internal.execution_data_taps |
| catalog | [execution_parameter_values](catalog.execution_parameter_values.md) | internal.current_user_readable_operations, internal.execution_parameter_values |
| catalog | [execution_property_override_values](catalog.execution_property_override_values.md) | internal.current_user_readable_operations, internal.execution_property_override_values |
| catalog | [executions](catalog.executions.md) | internal.current_user_readable_operations, internal.executions, internal.operation_os_sys_info, internal.operations |
| catalog | [explicit_object_permissions](catalog.explicit_object_permissions.md) | catalog.effective_object_permissions, internal.get_principal_id_by_sid, internal.object_permissions |
| catalog | [extended_operation_info](catalog.extended_operation_info.md) | internal.current_user_readable_operations, internal.extended_operation_info |
| catalog | [folders](catalog.folders.md) | internal.current_user_readable_folders, internal.folders |
| catalog | [object_parameters](catalog.object_parameters.md) | internal.current_user_readable_projects, internal.object_parameters, internal.object_versions, internal.projects |
| catalog | [object_versions](catalog.object_versions.md) | internal.current_user_readable_projects, internal.object_versions, internal.projects |
| catalog | [operation_messages](catalog.operation_messages.md) | internal.current_user_readable_operations, internal.operation_messages |
| catalog | [operations](catalog.operations.md) | internal.current_user_readable_operations, internal.operations |
| catalog | [packages](catalog.packages.md) | internal.current_user_readable_projects, internal.object_versions, internal.packages, internal.projects |
| catalog | [projects](catalog.projects.md) | internal.current_user_readable_projects, internal.folders, internal.object_versions, internal.projects |
| catalog | [validations](catalog.validations.md) | internal.current_user_readable_operations, internal.operations, internal.validations |
| internal | [current_user_object_permissions](internal.current_user_object_permissions.md) | internal.object_permissions |
| internal | [current_user_readable_environments](internal.current_user_readable_environments.md) | catalog.effective_object_permissions |
| internal | [current_user_readable_folders](internal.current_user_readable_folders.md) | catalog.effective_object_permissions |
| internal | [current_user_readable_operations](internal.current_user_readable_operations.md) | catalog.effective_object_permissions |
| internal | [current_user_readable_projects](internal.current_user_readable_projects.md) | catalog.effective_object_permissions |
| internal | [execution_info](internal.execution_info.md) | internal.current_user_readable_operations, internal.executions, internal.operations |
| internal | [object_folders](internal.object_folders.md) | internal.environments, internal.folders, internal.projects |
| internal | [object_permissions](internal.object_permissions.md) | internal.environment_permissions, internal.folder_permissions, internal.operation_permissions, internal.project_permissions |
