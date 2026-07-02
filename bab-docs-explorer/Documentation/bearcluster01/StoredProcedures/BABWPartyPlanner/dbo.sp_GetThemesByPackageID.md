# dbo.sp_GetThemesByPackageID

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_GetThemesByPackageID"]
    dbo_vwThemesPackages(["dbo.vwThemesPackages"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwThemesPackages |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetThemesByPackageID]
	-- Add the parameters for the stored procedure here
	@packageID int = NULL
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	
	--SELECT * FROM [BABWPartyPlanner].[dbo].[vwThemesPackages] 	where PackageID = @packageID 


	IF (@packageID is null)
		BEGIN
			SELECT * FROM [BABWPartyPlanner].[dbo].[vwThemesPackages] 	
			WHERE PackageName is null
		END
	Else
		BEGIN
			SELECT * FROM [BABWPartyPlanner].[dbo].[vwThemesPackages] 
			WHERE PackageID = @packageID
		END

	--CASE 
	--	WHEN @packageID is null THEN SELECT * FROM [BABWPartyPlanner].[dbo].[vwThemesPackages] where PackageID is null
	--	ELSE SELECT * FROM [BABWPartyPlanner].[dbo].[vwThemesPackages] 	where PackageID = @packageID 
	--END


END
```

