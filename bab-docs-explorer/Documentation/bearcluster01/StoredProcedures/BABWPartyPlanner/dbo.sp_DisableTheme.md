# dbo.sp_DisableTheme

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DisableTheme"]
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
-- Description:	<disables a theme>
-- =============================================
CREATE PROCEDURE [dbo].[sp_DisableTheme] 
	-- Add the parameters for the stored procedure here
	@themeID int
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE [BABWPartyPlanner].[dbo].[Theme]
	SET  [Enabled] = 0
	WHERE ThemeID = @themeID
END
```

