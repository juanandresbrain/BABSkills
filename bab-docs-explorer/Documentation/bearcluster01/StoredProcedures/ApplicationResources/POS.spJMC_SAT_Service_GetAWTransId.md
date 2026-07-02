# POS.spJMC_SAT_Service_GetAWTransId

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["POS.spJMC_SAT_Service_GetAWTransId"]
    dbo_NSBTransactionNumbers(["dbo.NSBTransactionNumbers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.NSBTransactionNumbers |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Barud, Ben
-- Create date: 7-25-2023
-- Description:	Used to manage the consumption of transaction ids
-- =============================================
CREATE PROCEDURE [POS].[spJMC_SAT_Service_GetAWTransId] 
	-- Add the parameters for the stored procedure here
	@AppName VARCHAR(50),
	@StoreId INT,
	@RegisterNo INT
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
	AND	[iStoreNumber] = @StoreId
	AND [iRegisterNumber] = @RegisterNo;
	
	
	IF @CountOfAWTransId > 0
		UPDATE [NSBTransactionNumbers]
		SET [iNSBTransactionNumber] = [iNSBTransactionNumber] + 1
		WHERE [sAppName] = @AppName
		AND	[iStoreNumber] = @StoreId
		AND [iRegisterNumber] = @RegisterNo
	ELSE
		INSERT INTO NSBTransactionNumbers
			(iStoreNumber,
			 iNSBTransactionNumber,
			 sAppName,
			 iRegisterNumber)
		VALUES(@StoreId, 1, @AppName, @RegisterNo)
	
	
	
	SELECT @AWTransId = [iNSBTransactionNumber]
	FROM [NSBTransactionNumbers]
	WHERE [sAppName] = @AppName
	AND	[iStoreNumber] = @StoreId
	AND [iRegisterNumber] = @RegisterNo;
	
	COMMIT;

	-- Insert statements for procedure here
	SELECT @AWTransId
	
END
```

