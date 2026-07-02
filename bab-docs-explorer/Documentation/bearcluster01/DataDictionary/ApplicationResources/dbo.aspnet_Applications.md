# dbo.aspnet_Applications

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ApplicationName | nvarchar | 512 | 0 |  |  |  |
| LoweredApplicationName | nvarchar | 512 | 0 |  |  |  |
| ApplicationId | uniqueidentifier | 16 | 0 | YES |  |  |
| Description | nvarchar | 512 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.aspnet_Applications_CreateApplication](../../StoredProcedures/ApplicationResources/dbo.aspnet_Applications_CreateApplication.md)
- [ApplicationResources: dbo.aspnet_Profile_DeleteInactiveProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_DeleteInactiveProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetNumberOfInactiveProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetNumberOfInactiveProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetProperties](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetProperties.md)
- [ApplicationResources: dbo.aspnet_Roles_DeleteRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_Roles_DeleteRole.md)
- [ApplicationResources: dbo.aspnet_Roles_GetAllRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Roles_GetAllRoles.md)
- [ApplicationResources: dbo.aspnet_Roles_RoleExists](../../StoredProcedures/ApplicationResources/dbo.aspnet_Roles_RoleExists.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_AddUsersToRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_AddUsersToRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_FindUsersInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_FindUsersInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetRolesForUser](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetRolesForUser.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetUsersInRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetUsersInRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_IsUserInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_IsUserInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_RemoveUsersFromRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_RemoveUsersFromRoles.md)

