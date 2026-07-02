# Stored Procedures: ApplicationResources

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [aspnet_Applications_CreateApplication](dbo.aspnet_Applications_CreateApplication.md) | dbo.aspnet_Applications |
| dbo | [aspnet_CheckSchemaVersion](dbo.aspnet_CheckSchemaVersion.md) | dbo.aspnet_SchemaVersions |
| dbo | [aspnet_Profile_DeleteInactiveProfiles](dbo.aspnet_Profile_DeleteInactiveProfiles.md) | dbo.aspnet_Applications, dbo.aspnet_Profile, dbo.aspnet_Users |
| dbo | [aspnet_Profile_DeleteProfiles](dbo.aspnet_Profile_DeleteProfiles.md) | dbo.aspnet_Users_DeleteUser |
| dbo | [aspnet_Profile_GetNumberOfInactiveProfiles](dbo.aspnet_Profile_GetNumberOfInactiveProfiles.md) | dbo.aspnet_Applications, dbo.aspnet_Profile, dbo.aspnet_Users |
| dbo | [aspnet_Profile_GetProfiles](dbo.aspnet_Profile_GetProfiles.md) | dbo.aspnet_Applications, dbo.aspnet_Profile, dbo.aspnet_Users |
| dbo | [aspnet_Profile_GetProperties](dbo.aspnet_Profile_GetProperties.md) | dbo.aspnet_Applications, dbo.aspnet_Profile, dbo.aspnet_Users |
| dbo | [aspnet_Profile_SetProperties](dbo.aspnet_Profile_SetProperties.md) | dbo.aspnet_Applications_CreateApplication, dbo.aspnet_Profile, dbo.aspnet_Users, dbo.aspnet_Users_CreateUser |
| dbo | [aspnet_RegisterSchemaVersion](dbo.aspnet_RegisterSchemaVersion.md) | dbo.aspnet_SchemaVersions |
| dbo | [aspnet_Roles_DeleteRole](dbo.aspnet_Roles_DeleteRole.md) | dbo.aspnet_Applications, dbo.aspnet_Roles, dbo.aspnet_UsersInRoles |
| dbo | [aspnet_Roles_GetAllRoles](dbo.aspnet_Roles_GetAllRoles.md) | dbo.aspnet_Applications, dbo.aspnet_Roles |
| dbo | [aspnet_Roles_RoleExists](dbo.aspnet_Roles_RoleExists.md) | dbo.aspnet_Applications, dbo.aspnet_Roles |
| dbo | [aspnet_Setup_RemoveAllRoleMembers](dbo.aspnet_Setup_RemoveAllRoleMembers.md) |  |
| dbo | [aspnet_Setup_RestorePermissions](dbo.aspnet_Setup_RestorePermissions.md) |  |
| dbo | [aspnet_UnRegisterSchemaVersion](dbo.aspnet_UnRegisterSchemaVersion.md) | dbo.aspnet_SchemaVersions |
| dbo | [aspnet_Users_CreateUser](dbo.aspnet_Users_CreateUser.md) | dbo.aspnet_Users |
| dbo | [aspnet_UsersInRoles_AddUsersToRoles](dbo.aspnet_UsersInRoles_AddUsersToRoles.md) | dbo.aspnet_Applications, dbo.aspnet_Roles, dbo.aspnet_Users, dbo.aspnet_UsersInRoles |
| dbo | [aspnet_UsersInRoles_FindUsersInRole](dbo.aspnet_UsersInRoles_FindUsersInRole.md) | dbo.aspnet_Applications, dbo.aspnet_Roles, dbo.aspnet_Users, dbo.aspnet_UsersInRoles |
| dbo | [aspnet_UsersInRoles_GetRolesForUser](dbo.aspnet_UsersInRoles_GetRolesForUser.md) | dbo.aspnet_Applications, dbo.aspnet_Roles, dbo.aspnet_Users, dbo.aspnet_UsersInRoles |
| dbo | [aspnet_UsersInRoles_GetUsersInRoles](dbo.aspnet_UsersInRoles_GetUsersInRoles.md) | dbo.aspnet_Applications, dbo.aspnet_Roles, dbo.aspnet_Users, dbo.aspnet_UsersInRoles |
| dbo | [aspnet_UsersInRoles_IsUserInRole](dbo.aspnet_UsersInRoles_IsUserInRole.md) | dbo.aspnet_Applications, dbo.aspnet_Roles, dbo.aspnet_Users, dbo.aspnet_UsersInRoles |
| dbo | [aspnet_UsersInRoles_RemoveUsersFromRoles](dbo.aspnet_UsersInRoles_RemoveUsersFromRoles.md) | dbo.aspnet_Applications, dbo.aspnet_Roles, dbo.aspnet_Users, dbo.aspnet_UsersInRoles |
| dbo | [sp_alterdiagram](dbo.sp_alterdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_creatediagram](dbo.sp_creatediagram.md) | dbo.sysdiagrams |
| dbo | [sp_dropdiagram](dbo.sp_dropdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_GetJumpMindStateExists](dbo.sp_GetJumpMindStateExists.md) | dbo.tax_authority |
| dbo | [sp_GetJumpMindTaxState](dbo.sp_GetJumpMindTaxState.md) | dbo.state_province, dbo.tax_authority |
| dbo | [sp_helpdiagramdefinition](dbo.sp_helpdiagramdefinition.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagrams](dbo.sp_helpdiagrams.md) | dbo.sysdiagrams |
| dbo | [sp_renamediagram](dbo.sp_renamediagram.md) | dbo.sysdiagrams |
| dbo | [sp_upgraddiagrams](dbo.sp_upgraddiagrams.md) | dbo.dtproperties, dbo.sysdiagrams |
| dbo | [spDeleteJumpmindJsonRecords](dbo.spDeleteJumpmindJsonRecords.md) | POS.JumpMindAPI_Logging |
| dbo | [spPostProductionService_GetTransactionNumber_1_1](dbo.spPostProductionService_GetTransactionNumber_1_1.md) | dbo.ServiceTransactionNumbers |
| POS | [JumpMindAPI_SearchLogs](POS.JumpMindAPI_SearchLogs.md) |  |
| POS | [spJMC_SAT_Service_GetAWTransId](POS.spJMC_SAT_Service_GetAWTransId.md) | dbo.NSBTransactionNumbers |
