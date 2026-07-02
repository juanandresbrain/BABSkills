# dbo.sp_dropdiagram

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_dropdiagram"]
    dbo_sysdiagrams(["dbo.sysdiagrams"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysdiagrams |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_dropdiagram
	(
		@diagramname 	sysname,
		@owner_id	int	= null
	)
	WITH EXECUTE AS 'dbo'
	AS
	BEGIN
		set nocount on
		declare @theId 			int
		declare @IsDbo 			int
		
		declare @UIDFound 		int
		declare @DiagId			int
	
		if(@diagramname is null)
		begin
			RAISERROR ('Invalid value', 16, 1);
			return -1
		end
	
		EXECUTE AS CALLER;
		select @theId = DATABASE_PRINCIPAL_ID();
		select @IsDbo = IS_MEMBER(N'db_owner'); 
		if(@owner_id is null)
			select @owner_id = @theId;
		REVERT; 
		
		select @DiagId = diagram_id, @UIDFound = principal_id from dbo.sysdiagrams where principal_id = @owner_id and name = @diagramname 
		if(@DiagId IS NULL or (@IsDbo = 0 and @UIDFound <> @theId))
		begin
			RAISERROR ('Diagram does not exist or you do not have permission.', 16, 1)
			return -3
		end
	
		delete from dbo.sysdiagrams where diagram_id = @DiagId;
	
		return 0;
	END
	
dbo,sp_FindExistingCustomerID,-- =============================================
-- Author:		Tim Bytnar
-- Create date: 5/2/2017
-- Description:	This proc will look for a pre-existing customer based first upon their Email address, and then based upon their first and last name.  If a match is found, the customer ID will be returned, if no match is found 0 is returned.
-- =============================================
CREATE PROCEDURE [dbo].[sp_FindExistingCustomerID] 
	@FirstName varchar(64),
     @LastName varchar(64),
     @EmailAddress varchar(128),
	 @CustomerNumber varchar(20) = '',
	@CustomerID int OUTPUT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
    SET NOCOUNT ON;
    DECLARE @Result int;
    
	-- Had to use table variables because CTEs only work for a single execution	
    DECLARE @CustNoMatches TABLE
    (
	   CustomerID int
    )
	INSERT INTO @CustNoMatches
		SELECT CustomerID
		FROM [BABWPartyPlanner].[dbo].[Customer] WITH (NOLOCK)
		WHERE ISNUMERIC(CustomerNumber) = 1
			  AND CustomerNumber = @CustomerNumber

    -- Had to use table variables because CTEs only work for a single execution	
    DECLARE @NameMatches TABLE
    (
	   CustomerID int
    )
    INSERT INTO @NameMatches
	   SELECT CustomerID
		FROM [BABWPartyPlanner].[dbo].[Customer] WITH (NOLOCK)
		WHERE (FirstName = @FirstName AND LastName = @LastName)

    -- Had to use table variables because CTEs only work for a single execution
    DECLARE @EmailMatches TABLE
    (
	   CustomerID int
    )
    INSERT INTO @EmailMatches
	   SELECT CustomerID
		FROM [BABWPartyPlanner].[dbo].[Customer] WITH (NOLOCK)
		WHERE (EmailAddress = @EmailAddress)
    
    -- If there are no customer number or email matches then check for any firstname/lastname matches
	IF((SELECT COUNT(CustomerID) FROM @CustNoMatches) = 0)
		BEGIN
			IF((SELECT COUNT(CustomerID) FROM @EmailMatches) = 0)
			   BEGIN
				  -- If there are no name matches then we have to generate a new cutomer ID so return 0
				  --IF((SELECT COUNT(CustomerID) FROM @NameMatches) = 0)
					 --BEGIN
						--SET @Result = 0;
					 --END
				  --ELSE
					 --BEGIN
						----Get the newest ID if there are duplicates
						--SET @Result = (SELECT MAX(CustomerID) FROM @NameMatches)
					 --END
					 SET @Result = 0
			   END
			ELSE
			   BEGIN
				  --Get the newest ID if there are duplicates
				  SET @Result = (SELECT MAX(CustomerID) FROM @EmailMatches)
			   END
		END
	ELSE
		BEGIN
			SET @Result = (SELECT MAX(CustomerID) FROM @CustNoMatches)
		END

    SET @CustomerID = @Result
END

dbo,sp_GetAllCountries,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetAllCountries]
	@showinactive varchar(max)
AS
BEGIN

	--https://anubhavg.wordpress.com/2009/06/11/how-to-format-datetime-date-in-sql-server-2005

	declare @sql nvarchar(max);
	declare @enable nvarchar(max);
	declare @orderby nvarchar(max);
	declare @sqlcommand nvarchar(max);

	set @sql=' select countryid, countryname, countryabbr, enabled from country ' ;
	
	if (@showinactive != 'on')
		set @enable= ' where enabled=1 ';
	else
		set @enable='';

	set @orderby= ' order by enabled desc, countryname ';

	set @sqlcommand= @sql + @enable + @orderby;
	exec (@sqlcommand);

END

dbo,sp_GetAllCountriesFromStoreMDM,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_GetAllCountriesFromStoreMDM
AS
BEGIN
select distinct CNTRY_ID, country from vwStoreToStoreMDM where country is not null
END

dbo,sp_GetAllGroups,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_GetAllGroups
AS
BEGIN
	
	select storegroupid, storegroupname, storegroupdesc from storegroup

END

dbo,sp_GetAllOptions,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetAllOptions]
@showinactive varchar(max)
AS
BEGIN

	--https://anubhavg.wordpress.com/2009/06/11/how-to-format-datetime-date-in-sql-server-2005

	declare @sql nvarchar(max);
	declare @enable nvarchar(max);
	declare @orderby nvarchar(max);
	declare @sqlcommand nvarchar(max);

	set @sql=' select optionid, optionname, enabled, defaultcost from [option] ' ;
	
	if (@showinactive != 'on')
		set @enable= ' where enabled=1 ';
	else
		set @enable='';

	set @orderby= ' order by enabled desc, orderby, optionname ';

	set @sqlcommand= @sql + @enable + @orderby;
	exec (@sqlcommand);
END

dbo,sp_GetAllPackges,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetAllPackges]
	@showinactive varchar(max)
AS
BEGIN

	--https://anubhavg.wordpress.com/2009/06/11/how-to-format-datetime-date-in-sql-server-2005

	declare @sql nvarchar(max);
	declare @enable nvarchar(max);
	declare @orderby nvarchar(max);
	declare @sqlcommand nvarchar(max);

	set @sql=' select packageid, PackageShortDesc as packagename, enabled from package ' ;
	
	if (@showinactive != 'on')
		set @enable= ' where enabled=1 ';
	else
		set @enable='';

	--set @orderby= ' order by orderby, PackageShortDesc ';
	set @orderby= ' order by PackageShortDesc ';

	set @sqlcommand= @sql + @enable + @orderby;
	exec (@sqlcommand);
END

dbo,sp_GetAllPortalUsers,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetAllPortalUsers]
	
AS
BEGIN

	select userid, password, userdescription, storenum, a.roleid, roledescription 
	from portalusers A inner join portaluserrole b
	on a.roleid=b.roleid
	order by roleid, userid

END

dbo,sp_GetAllStores,-- =============================================countryi
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetAllStores]
AS
BEGIN
   --SELECT [StoreID]
  --    ,[StoreNumber]
   --   ,[StoreGroupID] as StoreGroup
   --FROM [BABWPartyPlanner].[dbo].[Store]
   --ORDER BY StoreNumber ASC



   Select storeid, storenumber, 
   (select storegroupid from store b where a.storenumber=b.storenumber) as storegroupid
    from vwStoreToStoreMDM a order by storenumber
END

dbo,sp_GetAllStoresByCountry,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE procEDURE [dbo].[sp_GetAllStoresByCountry]

	@COUNTRYID	varchar(10)
AS
BEGIN
	select storeid from vwStoreToStoreMDM where countryid=@COUNTRYID

	--select a.StoreID
	--from (vwStoreToStoreMDM a 
	--inner join country b on a.countryid=b.countryid and b.countryid=@countryid)
	--left join [dbo].[StorePackageXref] c on a.storeid=c.storeid order by countryname, storenumber 

END

dbo,sp_GetAllStoresByOptionID,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_GetAllStoresByOptionID
	@optionid int,
		@COUNTRYID	varchar(10)  --not use
AS
BEGIN
select a.StoreID, a.storenumber STR_NUM, a.StoreName nm_full, isnull(c.optionid,0) enabled, a.countryid, countryname
	from (vwStoreToStoreMDM a 
	inner join country b on a.countryid=b.countryid)
	left join optionstorexref c on a.storeid=c.storeid and c.optionid=@optionid order by countryname, storenumber 
END

dbo,sp_GetAllStoresByPackageID,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create procEDURE [dbo].[sp_GetAllStoresByPackageID]

	@COUNTRYID	varchar(10),
	@packageid int
AS
BEGIN

	declare @sql nvarchar(max);
	declare @sql2 nvarchar(max);
	declare @sqlcommand nvarchar(max);



--set @sql='select a.StoreID, b.STR_NUM, b.nm_full, isnull(c.PackageId,0) enabled  from vwStoreToStoreMDM a inner join kodiak.BABWMstrData.dbo.str_dim b on a.storenumber=b.str_num and b.cntry_id in ( ';
--set @sql2=') left join [dbo].[StorePackageXref] c on a.storeid=c.storeid and c.packageid=' + convert(varchar(20),@packageid) + ' order by storenumber ';
	--set @sqlcommand= @sql + @countryid + @sql2;
	--exec (@sqlcommand);

	
	--select a.StoreID, a.storenumber STR_NUM, a.StoreName nm_full, isnull(c.PackageId,0) enabled  from vwStoreToStoreMDM a
	--left join [dbo].[StorePackageXref] c on a.storeid=c.storeid and c.packageid=@packageid where countryid = @countryid order by storenumber 
	
	select a.StoreID, a.storenumber STR_NUM, a.StoreName nm_full, isnull(c.PackageId,0) enabled, a.countryid, countryname
	from (vwStoreToStoreMDM a 
	inner join country b on a.countryid=b.countryid)
	left join [dbo].[StorePackageXref] c on a.storeid=c.storeid and c.packageid=@packageid order by countryname, storenumber 
END

dbo,sp_GetAllStoresWithName,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetAllStoresWithName]

AS
BEGIN

Select distinct storeid,storenumber,  storename, MaxGuests from vwStoreToStoreMDM order by storenumber

END
```

