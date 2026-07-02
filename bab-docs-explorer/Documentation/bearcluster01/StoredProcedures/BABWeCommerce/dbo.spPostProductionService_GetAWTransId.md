# dbo.spPostProductionService_GetAWTransId

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spPostProductionService_GetAWTransId"]
    dbo_NSBTransactionNumbers(["dbo.NSBTransactionNumbers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.NSBTransactionNumbers |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Schlobohm, Ken
-- Create date: 6-27-2011
-- Description:	Used to manage the consumption of transaction ids
-- =============================================
CREATE PROCEDURE [dbo].[spPostProductionService_GetAWTransId] 
	-- Add the parameters for the stored procedure here
	@AppName VARCHAR(50),
	@StoreId INT
AS
BEGIN

	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	BEGIN TRAN;
		
	DECLARE @AWTransId INT;
	DECLARE @CountOfAWTransId INT;
	
	SELECT @CountOfAWTransId = Count([iNSBTransactionNumber])
	FROM [NSBTransactionNumbers]
	WHERE [sAppName] = @AppName
	and	[iStoreNumber] = @StoreId;
	
	
	IF @CountOfAWTransId > 0
		UPDATE [NSBTransactionNumbers]
		SET [iNSBTransactionNumber] = [iNSBTransactionNumber] + 1
		WHERE [sAppName] = @AppName
		AND	[iStoreNumber] = @StoreId;
	ELSE
		INSERT INTO NSBTransactionNumbers
			(iStoreNumber,
			 iNSBTransactionNumber,
			 sAppName)
		VALUES(@StoreId, 1, @AppName)
	
	
	
	SELECT @AWTransId = [iNSBTransactionNumber]
	FROM [NSBTransactionNumbers]
	WHERE [sAppName] = @AppName
	AND	[iStoreNumber] = @StoreId;
	
	COMMIT;

	-- Insert statements for procedure here
	SELECT @AWTransId
	
END
```

