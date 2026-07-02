# dbo.aspnet_UsersInRoles

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UserId | uniqueidentifier | 16 | 0 | YES | YES |  |
| RoleId | uniqueidentifier | 16 | 0 | YES | YES |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.aspnet_Roles_DeleteRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_Roles_DeleteRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_AddUsersToRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_AddUsersToRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_FindUsersInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_FindUsersInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetRolesForUser](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetRolesForUser.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetUsersInRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetUsersInRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_IsUserInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_IsUserInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_RemoveUsersFromRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_RemoveUsersFromRoles.md)

