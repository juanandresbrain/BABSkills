# dbo.sp_creatediagram

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_creatediagram"]
    dbo_sysdiagrams(["dbo.sysdiagrams"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysdiagrams |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_creatediagram
	(
		@diagramname 	sysname,
		@owner_id		int	= null, 	
		@version 		int,
		@definition 	varbinary(max)
	)
	WITH EXECUTE AS 'dbo'
	AS
	BEGIN
		set nocount on
	
		declare @theId int
		declare @retval int
		declare @IsDbo	int
		declare @userName sysname
		if(@version is null or @diagramname is null)
		begin
			RAISERROR (N'E_INVALIDARG', 16, 1);
			return -1
		end
	
		execute as caller;
		select @theId = DATABASE_PRINCIPAL_ID(); 
		select @IsDbo = IS_MEMBER(N'db_owner');
		revert; 
		
		if @owner_id is null
		begin
			select @owner_id = @theId;
		end
		else
		begin
			if @theId <> @owner_id
			begin
				if @IsDbo = 0
				begin
					RAISERROR (N'E_INVALIDARG', 16, 1);
					return -1
				end
				select @theId = @owner_id
			end
		end
		-- next 2 line only for test, will be removed after define name unique
		if EXISTS(select diagram_id from dbo.sysdiagrams where principal_id = @theId and name = @diagramname)
		begin
			RAISERROR ('The name is already used.', 16, 1);
			return -2
		end
	
		insert into dbo.sysdiagrams(name, principal_id , version, definition)
				VALUES(@diagramname, @theId, @version, @definition) ;
		
		select @retval = @@IDENTITY 
		return @retval
	END
	
dbo,sp_CreateMissingStores,-- =============================================
-- Author:		Tim Bytnar
-- Create date: 10/26/2017
-- Description:	Because the Beartracks Application is unable to be developed to create stores, this procedure will detect missing stores found in StoreMDM and insert them into the store table.
-- =============================================
CREATE PROCEDURE [dbo].[sp_CreateMissingStores] 
	
AS
BEGIN
	
	BEGIN TRY
	   BEGIN TRAN
		   set identity_insert Store ON
		   INSERT INTO Store (StoreID, StoreNumber, CountryID)
		   SELECT StoreNumber, StoreNumber, CNTRY_ID
		   FROM vwMissingStoreFromStoreMDM WITH (NOLOCK)
		   WHERE StoreID IS NULL
		   SET IDENTITY_INSERT Store Off
		   COMMIT
    END TRY
    BEGIN CATCH
	   IF(@@TRANCOUNT > 0)
		  ROLLBACK TRAN
    END CATCH
END

dbo,sp_DeleteEvent,-- =============================================
-- Author:		Tim Bytnar
-- Create date: 6/12/2017
-- Description:	This stored procedure will delete the specified Event and any related rows from the database.
-- =============================================
CREATE PROCEDURE sp_DeleteEvent 
	-- Add the parameters for the stored procedure here
	@EventID int
AS
BEGIN
	BEGIN TRAN
		BEGIN TRY
			BEGIN
				UPDATE [dbo].[Event]
				SET Active = 0,
					LastUpdated = GetDate()
				WHERE EventID = @EventID
				COMMIT
			END
		END TRY
		BEGIN CATCH
			IF @@TRANCOUNT > 0
				ROLLBACK TRAN
		END CATCH
END

dbo,sp_DeletePackage,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_DeletePackage
	@id int
AS
BEGIN

	update package set Enabled=0, orderby=99999 where PackageID=@id;

END
```

