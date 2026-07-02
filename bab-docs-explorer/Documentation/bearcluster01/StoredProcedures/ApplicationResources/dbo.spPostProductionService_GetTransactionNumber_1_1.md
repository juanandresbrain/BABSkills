# dbo.spPostProductionService_GetTransactionNumber_1_1

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spPostProductionService_GetTransactionNumber_1_1"]
    dbo_ServiceTransactionNumbers(["dbo.ServiceTransactionNumbers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ServiceTransactionNumbers |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Barud, Ben
-- Create date: 8-4-2017
-- Description:	Used to manage the consumption of transaction numbers
-- =============================================
CREATE PROCEDURE [dbo].[spPostProductionService_GetTransactionNumber_1_1] 
	-- Add the parameters for the stored procedure here
	@ServiceID INT,
	@StoreNumber INT
AS
BEGIN

	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	BEGIN TRAN;
		
	DECLARE @TransNum BIGINT;
	DECLARE @CountOfTransNum INT;
	
	SELECT @CountOfTransNum = Count([TransactionNumber])
	FROM [ServiceTransactionNumbers]
	WHERE [ServiceID] = @ServiceID
	AND	[StoreNumber] = @StoreNumber;
	
	
	IF @CountOfTransNum > 0
		UPDATE [ServiceTransactionNumbers]
		SET [TransactionNumber] = [TransactionNumber] + 1
		WHERE [ServiceID] = @ServiceID
		AND	[StoreNumber] = @StoreNumber;
	ELSE
		INSERT INTO ServiceTransactionNumbers
			(StoreNumber,
			 TransactionNumber,
			 ServiceID)
		VALUES(@StoreNumber, 1, @ServiceID)
	
	
	
	SELECT @TransNum = [TransactionNumber]
	FROM [ServiceTransactionNumbers]
	WHERE [ServiceID] = @ServiceID
	AND	[StoreNumber] = @StoreNumber;
	
	COMMIT;

	-- Insert statements for procedure here
	SELECT @TransNum
	
END
```

