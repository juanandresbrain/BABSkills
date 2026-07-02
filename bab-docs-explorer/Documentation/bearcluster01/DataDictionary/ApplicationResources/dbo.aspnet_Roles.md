# dbo.aspnet_Roles

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ApplicationId | uniqueidentifier | 16 | 0 |  | YES |  |
| RoleId | uniqueidentifier | 16 | 0 | YES |  |  |
| RoleName | nvarchar | 512 | 0 |  |  |  |
| LoweredRoleName | nvarchar | 512 | 0 |  |  |  |
| Description | nvarchar | 512 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.aspnet_Roles_DeleteRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_Roles_DeleteRole.md)
- [ApplicationResources: dbo.aspnet_Roles_GetAllRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Roles_GetAllRoles.md)
- [ApplicationResources: dbo.aspnet_Roles_RoleExists](../../StoredProcedures/ApplicationResources/dbo.aspnet_Roles_RoleExists.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_AddUsersToRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_AddUsersToRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_FindUsersInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_FindUsersInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetRolesForUser](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetRolesForUser.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetUsersInRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetUsersInRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_IsUserInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_IsUserInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_RemoveUsersFromRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_RemoveUsersFromRoles.md)

