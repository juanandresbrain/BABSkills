# dbo.sp_alterdiagram

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_alterdiagram"]
    dbo_sysdiagrams(["dbo.sysdiagrams"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysdiagrams |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_alterdiagram
	(
		@diagramname 	sysname,
		@owner_id	int	= null,
		@version 	int,
		@definition 	varbinary(max)
	)
	WITH EXECUTE AS 'dbo'
	AS
	BEGIN
		set nocount on
	
		declare @theId 			int
		declare @retval 		int
		declare @IsDbo 			int
		
		declare @UIDFound 		int
		declare @DiagId			int
		declare @ShouldChangeUID	int
	
		if(@diagramname is null)
		begin
			RAISERROR ('Invalid ARG', 16, 1)
			return -1
		end
	
		execute as caller;
		select @theId = DATABASE_PRINCIPAL_ID();	 
		select @IsDbo = IS_MEMBER(N'db_owner'); 
		if(@owner_id is null)
			select @owner_id = @theId;
		revert;
	
		select @ShouldChangeUID = 0
		select @DiagId = diagram_id, @UIDFound = principal_id from dbo.sysdiagrams where principal_id = @owner_id and name = @diagramname 
		
		if(@DiagId IS NULL or (@IsDbo = 0 and @theId <> @UIDFound))
		begin
			RAISERROR ('Diagram does not exist or you do not have permission.', 16, 1);
			return -3
		end
	
		if(@IsDbo <> 0)
		begin
			if(@UIDFound is null or USER_NAME(@UIDFound) is null) -- invalid principal_id
			begin
				select @ShouldChangeUID = 1 ;
			end
		end

		-- update dds data			
		update dbo.sysdiagrams set definition = @definition where diagram_id = @DiagId ;

		-- change owner
		if(@ShouldChangeUID = 1)
			update dbo.sysdiagrams set principal_id = @theId where diagram_id = @DiagId ;

		-- update dds version
		if(@version is not null)
			update dbo.sysdiagrams set version = @version where diagram_id = @DiagId ;

		return 0
	END
	
dbo,sp_ArchiveEventData,-- =============================================
-- Author:		Tim Bytnar
-- Create date: 6-23-2017
-- Description:	This will archive all Events older than 2 years and any related comments or parties.
-- =============================================
CREATE PROCEDURE [dbo].[sp_ArchiveEventData] 

AS
BEGIN
	SET NOCOUNT ON;

DECLARE @NextIDs TABLE(EventID int primary key)
DECLARE @TwoYearsAgo datetime
SELECT @TwoYearsAgo = DATEADD(d, -(2 * 365), GetDate())

WHILE EXISTS(SELECT 1 FROM [dbo].[Event] WHERE [Event].[EventStart] < @TwoYearsAgo)
BEGIN 
    BEGIN TRAN 

    INSERT INTO @NextIDs(EventID)
        SELECT TOP 1000 EventID FROM [dbo].[Event] WHERE [Event].[EventStart] < @TwoYearsAgo

    -----ARCHIVE THE EVENT ROWS
    INSERT INTO [dbo].[Event_Archive](EventID,EventStart,EventEnd,EventType,CreatedDate,CreatedBy,LastUpdated,StoreID,Active) 
        SELECT a.EventID,EventStart,EventEnd,EventType,CreatedDate,CreatedBy,LastUpdated,StoreID,Active
        FROM  [dbo].[Event] AS a
        INNER JOIN @NextIDs AS b ON a.EventID = b.EventID

    DELETE [dbo].[Event]
	   FROM  [dbo].[Event] AS a
	   INNER JOIN @NextIDs AS b ON a.EventID = b.EventID

    -----ARCHIVE THE COMMENT ROWS
    INSERT INTO [dbo].[Comment_Archive](CommentID,EventID,CreatedDate,Comment,CreatedBy,LastUpdated)
	   SELECT CommentID,a.EventID,CreatedDate,Comment,CreatedBy,LastUpdated
	   FROM [dbo].[Comment] AS a
	   INNER JOIN @NextIDs AS b ON a.EventID = b.EventID

    DELETE [dbo].[Comment]
	   FROM [dbo].[Comment] AS a 
	   INNER JOIN @NextIDs AS b ON a.EventID = b.EventID

    -----ARCHIVE THE PARTY ROWS
    INSERT INTO [dbo].[Party_Archive](PartyID,OccasionID,TotalGuests,CustomerID,EventID,GOHAge,GOHFirstName,GOHGender,GuestAvgAge,PartyStateID,DepositAmount)
	   SELECT PartyID,OccasionID,TotalGuests,CustomerID,a.EventID,GOHAge,GOHFirstName,GOHGender,GuestAvgAge,PartyStateID,DepositAmount
	   FROM [dbo].[Party] AS a
	   INNER JOIN @NextIDs AS b ON a.EventID = b.EventID

    DELETE [dbo].[Party]
	   FROM [dbo].[Party] AS a 
	   INNER JOIN @NextIDs AS b ON a.EventID = b.EventID

    DELETE FROM @NextIDs

    COMMIT TRAN
END 

END

dbo,sp_ClearCountryOptionXref,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_ClearCountryOptionXref
	@countryid int
AS
BEGIN

	delete from CountryOptionXref where Countryid=@countryid;

END

dbo,sp_ClearGroupBookingHours,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[sp_ClearGroupBookingHours]

	@groupid int

AS
BEGIN

	delete from StoregroupBookingHour where groupid=@groupid;

END

dbo,sp_ClearStoreBookingHours,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_ClearStoreBookingHours

	@storeid int

AS
BEGIN

	delete from StoreBookingHour where StoreID=@storeid;

END

dbo,sp_ClearStoreOptionXrefByOptionID,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[sp_ClearStoreOptionXrefByOptionID]
	@optionid int
AS
BEGIN

delete from [dbo].[OptionStoreXref] where optionid=@optionid;

END

dbo,sp_ClearStorePackageXref,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[sp_ClearStorePackageXref]
	@storeid int
AS
BEGIN

	delete from StorePackageXref where storeid=@storeid;

END

dbo,sp_ClearStorePackageXrefByPackageID,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_ClearStorePackageXrefByPackageID
	@packageid int
AS
BEGIN

delete from [dbo].[StorePackageXref] where packageid=@packageid;

END

dbo,sp_CountryOptions,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_CountryOptions]
	@countryid int
AS
BEGIN


select a.optionid, optionname, isnull(b.optionID,'0') as enabled from [option] a
left join countryoptionxref b

on  
 b.countryid=@countryid
and a.optionid=b.optionid
where a.enabled=1
order by orderby, optionname 

END

dbo,sp_CountryPackges,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_CountryPackges]
	@countryid int
AS
BEGIN


select a.packageid, packagename, isnull(b.PackageID,'0') as enabled from package a
left join countrypackagexref b

on a.enabled=1 
and b.countryid=@countryid
and a.packageid=b.packageid

--order by orderby, packagename 

--select packageid, packagename, isnull(countryID,'0') as enabled from package 
--where
--enabled=1 
----and countryid=@countryid
--order by orderby, packagename 

END
```

