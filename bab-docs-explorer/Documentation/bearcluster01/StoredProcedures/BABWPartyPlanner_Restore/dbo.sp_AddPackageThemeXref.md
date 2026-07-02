# dbo.sp_AddPackageThemeXref

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_AddPackageThemeXref"]
    dbo_ThemePackageXref(["dbo.ThemePackageXref"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ThemePackageXref |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Carl Haufle>
-- Create date: <12/5/2019>
-- Description:	<inserts themes for a packageID>
-- =============================================
CREATE PROCEDURE [dbo].[sp_AddPackageThemeXref]
	-- Add the parameters for the stored procedure here
	@packageID int,
	@themeID int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    INSERT INTO [BABWPartyPlanner].[dbo].[ThemePackageXref] (ThemeID, PackageID)
    VALUES (@themeID, @packageID);
END
```

