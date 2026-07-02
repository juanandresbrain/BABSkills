# dbo.sp_GetTheme

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_GetTheme"]
    dbo_Theme(["dbo.Theme"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Theme |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Carl Haufle>
-- Create date: <11/27/2019>
-- Description:	<returns data for a specific ThemeID>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetTheme] 
	-- Add the parameters for the stored procedure here
	@themeID int
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT [ThemeID]
      ,[ThemeName]
      ,[Enabled]
      ,[ThemeDesc]
  FROM [BABWPartyPlanner].[dbo].[Theme]
  where ThemeID = @themeID
END
```

