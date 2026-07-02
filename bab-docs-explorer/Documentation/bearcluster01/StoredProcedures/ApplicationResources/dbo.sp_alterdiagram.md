# dbo.sp_alterdiagram

**Database:** ApplicationResources  
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
	
dbo,sp_ArchiveLoggingData,-- =============================================
-- Author:		Tim Bytnar
-- Create date: 4/30/2018
-- Description:	This will archive all logging records older than 30 days
-- =============================================
CREATE PROCEDURE [dbo].[sp_ArchiveLoggingData] 

AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @NextIDs TABLE(LogID int primary key)
	DECLARE @ThirtyDaysAgo datetime
	SELECT @ThirtyDaysAgo = DATEADD(d, -30, GetDate())

	WHILE EXISTS(SELECT 1 [LogID] FROM [dbo].[ServiceLoggingGeneralUsage] WHERE [LogCreatedDate] < @ThirtyDaysAgo)
	BEGIN 
		BEGIN TRAN 

		INSERT INTO @NextIDs(LogID)
			SELECT TOP 1000 [LogID] FROM [dbo].[ServiceLoggingGeneralUsage] WHERE [LogCreatedDate] < @ThirtyDaysAgo

		-----ARCHIVE THE LOGGING ROWS
		INSERT INTO [dbo].[ServiceLoggingGeneralUsage_Archive](LogID,LogCreatedDate,Message,IsAnException,ExceptionMessage,ExceptionStacktrace,ServiceID,FunctionName) 
			SELECT a.LogID,LogCreatedDate,Message,IsAnException,ExceptionMessage,ExceptionStacktrace,ServiceID,FunctionName
			FROM  [dbo].[ServiceLoggingGeneralUsage] AS a
			INNER JOIN @NextIDs AS b ON a.[LogID] = b.[LogID]

		DELETE [dbo].[ServiceLoggingGeneralUsage]
		   FROM  [dbo].[ServiceLoggingGeneralUsage] AS a
		   INNER JOIN @NextIDs AS b ON a.[LogID] = b.[LogID]

		DELETE FROM @NextIDs

		COMMIT TRAN
	END 

END
```

