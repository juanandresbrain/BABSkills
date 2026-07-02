# dbo.aspnet_Profile

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UserId | uniqueidentifier | 16 | 0 | YES | YES |  |
| PropertyNames | ntext | 6000 | 0 |  |  |  |
| PropertyValuesString | ntext | 6000 | 0 |  |  |  |
| PropertyValuesBinary | image | 6000 | 0 |  |  |  |
| LastUpdatedDate | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.aspnet_Profile_DeleteInactiveProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_DeleteInactiveProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetNumberOfInactiveProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetNumberOfInactiveProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetProfiles](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetProfiles.md)
- [ApplicationResources: dbo.aspnet_Profile_GetProperties](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_GetProperties.md)
- [ApplicationResources: dbo.aspnet_Profile_SetProperties](../../StoredProcedures/ApplicationResources/dbo.aspnet_Profile_SetProperties.md)

