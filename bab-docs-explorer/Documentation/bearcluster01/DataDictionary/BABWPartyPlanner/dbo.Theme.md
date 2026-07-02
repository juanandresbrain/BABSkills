# dbo.Theme

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ThemeID | int | 4 | 0 | YES |  |  |
| ThemeName | varchar | -1 | 1 |  |  |  |
| Enabled | bit | 1 | 1 |  |  |  |
| ThemeDesc | varchar | 255 | 1 |  |  |  |
| CountryID | int | 4 | 1 |  | YES |  |
| OrderBy | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_DisableTheme](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_DisableTheme.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetTheme](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetTheme.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetThemes](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetThemes.md)
- [BABWPartyPlanner_Restore: dbo.sp_InsertTheme](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_InsertTheme.md)
- [BABWPartyPlanner_Restore: dbo.sp_UpdateTheme](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_UpdateTheme.md)
- [BABWPartyPlanner: dbo.sp_DisableTheme](../../StoredProcedures/BABWPartyPlanner/dbo.sp_DisableTheme.md)
- [BABWPartyPlanner: dbo.sp_GetTheme](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetTheme.md)
- [BABWPartyPlanner: dbo.sp_GetThemes](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetThemes.md)
- [BABWPartyPlanner: dbo.sp_InsertTheme](../../StoredProcedures/BABWPartyPlanner/dbo.sp_InsertTheme.md)
- [BABWPartyPlanner: dbo.sp_UpdateTheme](../../StoredProcedures/BABWPartyPlanner/dbo.sp_UpdateTheme.md)

