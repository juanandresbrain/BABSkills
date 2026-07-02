# dbo.sp_GetThemes

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_GetThemes"]
    dbo_Theme(["dbo.Theme"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Theme |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Author, Carl Haufle>
-- Create date: <11/26/19>
-- Description:	<returns all themes from the Theme table>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetThemes]
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
END
```

