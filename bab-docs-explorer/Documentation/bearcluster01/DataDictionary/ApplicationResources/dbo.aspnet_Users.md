# dbo.aspnet_Users

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ApplicationId | uniqueidentifier | 16 | 0 |  | YES |  |
| UserId | uniqueidentifier | 16 | 0 | YES |  |  |
| UserName | nvarchar | 512 | 0 |  |  |  |
| LoweredUserName | nvarchar | 512 | 0 |  |  |  |
| MobileAlias | nvarchar | 32 | 1 |  |  |  |
| IsAnonymous | bit | 1 | 0 |  |  |  |
| LastActivityDate | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.aspnet_Profile_DeleteInactiveProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_DeleteInactiveProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetNumberOfInactiveProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetNumberOfInactiveProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetProperties](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetProperties.md)
- [ApplicationResources: dbo.aspnet_Profile_SetProperties](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_SetProperties.md)
- [ApplicationResources: dbo.aspnet_Users_CreateUser](../../StoredProcedures/ApplicationResources/dbo.aspnet_Users_CreateUser.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_AddUsersToRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_AddUsersToRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_FindUsersInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_FindUsersInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetRolesForUser](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetRolesForUser.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_GetUsersInRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_GetUsersInRoles.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_IsUserInRole](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_IsUserInRole.md)
- [ApplicationResources: dbo.aspnet_UsersInRoles_RemoveUsersFromRoles](../../StoredProcedures/ApplicationResources/dbo.aspnet_UsersInRoles_RemoveUsersFromRoles.md)

