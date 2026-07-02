# dbo.spPostProductionService_GetAWTransId_V2

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spPostProductionService_GetAWTransId_V2"]
    dbo_NSBTransactionNumbers(["dbo.NSBTransactionNumbers"]) --> SP
    dbo_NSBTranslate_Debug(["dbo.NSBTranslate_Debug"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.NSBTransactionNumbers |
| dbo.NSBTranslate_Debug |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Schlobohm, Ken
-- Create date: 6-27-2011
-- Description:	Used to manage the consumption of transaction ids
-- =============================================
CREATE PROCEDURE [dbo].[spPostProductionService_GetAWTransId_V2] 
	-- Add the parameters for the stored procedure here
	@AppName VARCHAR(50),
	@StoreId INT,
	@OrderNumber VARCHAR(10) = NULL
AS
BEGIN

	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	BEGIN TRAN;
		
	DECLARE @AWTransId INT;
	DECLARE @CountOfAWTransId INT;
	
	IF @OrderNumber IS NOT NULL
	BEGIN
		SELECT DISTINCT @AWTransId = [sNSBTransID] FROM [dbo].[NSBTranslate_Debug]
		WHERE sOrderNumber = @OrderNumber
	END

	IF @AWTransId IS NOT NULL
		BEGIN
		SELECT @CountOfAWTransId = Count([iNSBTransactionNumber])
		FROM [NSBTransactionNumbers]
		WHERE [sAppName] = @AppName
		and	[iStoreNumber] = @StoreId;
	
	
		--IF @CountOfAWTransId > 0
		--	UPDATE [NSBTransactionNumbers]
		--	SET [iNSBTransactionNumber] = [iNSBTransactionNumber] + 1
		--	WHERE [sAppName] = @AppName
		--	AND	[iStoreNumber] = @StoreId;
		--ELSE
		--	INSERT INTO NSBTransactionNumbers
		--		(iStoreNumber,
		--		 iNSBTransactionNumber,
		--		 sAppName)
		--	VALUES(@StoreId, 1, @AppName)
	
	
	
		SELECT @AWTransId = [iNSBTransactionNumber]
		FROM [NSBTransactionNumbers]
		WHERE [sAppName] = @AppName
		AND	[iStoreNumber] = @StoreId;
	
		COMMIT;
	END

	-- Insert statements for procedure here
	SELECT @AWTransId
	
END
```

