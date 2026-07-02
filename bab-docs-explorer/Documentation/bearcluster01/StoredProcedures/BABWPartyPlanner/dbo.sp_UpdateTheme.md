# dbo.sp_UpdateTheme

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_UpdateTheme"]
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
-- Description:	<inserts a new theme into the theme table>
-- =============================================
CREATE PROCEDURE [dbo].[sp_UpdateTheme] 
	-- Add the parameters for the stored procedure here
	@themeID int,
	@themeName varchar(30),
	@themeDescription varchar(250)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE [BABWPartyPlanner].[dbo].[Theme]
SET [ThemeName] = @themeName, [Enabled] = 1, [ThemeDesc] = @themeDescription
WHERE ThemeID = @themeID
END
```

