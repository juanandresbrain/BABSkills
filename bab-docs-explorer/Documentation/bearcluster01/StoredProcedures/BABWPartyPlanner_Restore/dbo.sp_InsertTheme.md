# dbo.sp_InsertTheme

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_InsertTheme"]
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
CREATE PROCEDURE [dbo].[sp_InsertTheme] 
	-- Add the parameters for the stored procedure here
	@themeName varchar(30),
	@themeDescription varchar(250)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO [BABWPartyPlanner].[dbo].[Theme] ([ThemeName]
      ,[Enabled]
      ,[ThemeDesc])
	VALUES (@themeName, 1, @themeDescription)
END

dbo,sp_NewStoreSaveStep1,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_NewStoreSaveStep1]
	@bsrmsg varchar(max),
	@webmsg varchar(max),
	@groupid int,
	@storeid int,
	@maxguests int,
	@minguests int,
	@canbookonline bit,
	@bookingparties bit
AS
BEGIN
	update store 
	set BSRMessage=@bsrmsg, 
	WebMessage=@webmsg, 
	StoreGroupID=@groupid ,
	MaxGuests=@maxguests,
	MinGuests=@minguests,
	CanBookOnline=@canbookonline,
	BookingParties=@bookingparties
	where storeid=@storeid;
END
dbo,sp_NewStoreSetUpGroup,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_NewStoreSetUpGroup]
	@storeid int
AS
BEGIN
	
select a.storegroupid, storegroupname, isnull(b.StoreGroupID,-1) as assignedgroup
from storegroup a left join Store B
on b.StoreGroupID = a.StoreGroupID
and b.StoreID=@storeid

END

dbo,sp_RemoveUser,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE procedure sp_RemoveUser
	@aduser nvarchar(max)
AS
BEGIN
	delete from users where ADUser=@aduser;
END
```

