# dbo.spDeleteJumpmindJsonRecords

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDeleteJumpmindJsonRecords"]
    POS_JumpMindAPI_Logging(["POS.JumpMindAPI_Logging"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| POS.JumpMindAPI_Logging |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDeleteJumpmindJsonRecords]

-- =============================================================================================================
-- Name: spDeleteJumpmindJsonRecords 
--
-- Description:	Get's Missing JumpMind transactions for alerts and reprocessing
--	
-- Output: 
--	
-- Available actions:
--	
-- Dependencies: 
--		
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		09/03/2024		Creation
--		Ben Barud		09/15/2024		Changed from rolling 90 days to 35 days
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    IF (Object_ID('tempdb..#tmp') IS NOT NULL) DROP TABLE #tmp

    SELECT id
    INTO #tmp
    FROM [ApplicationResources].[POS].[JumpMindAPI_Logging]
    WHERE apiDateTime < DATEADD(DAY, -35, getdate())

    DECLARE @currentId AS INT

    WHILE (SELECT COUNT(*) FROM #tmp) > 0
    BEGIN

	  SELECT TOP 1 @currentId = id FROM #tmp ORDER BY id
	
	  DELETE FROM [ApplicationResources].[POS].[JumpMindAPI_Logging]
      WHERE id = @currentId
  
	  DELETE FROM #tmp
      WHERE id = @currentId

    END
END

dbo,spPostProductionService_GetTransactionNumber,-- =============================================
-- Author:		Barud, Ben
-- Create date: 8-4-2017
-- Description:	Used to manage the consumption of transaction numbers
-- =============================================
CREATE PROCEDURE [dbo].[spPostProductionService_GetTransactionNumber] 
	-- Add the parameters for the stored procedure here
	@ServiceID INT,
	@StoreNumber INT
AS
BEGIN

	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	BEGIN TRAN;
		
	DECLARE @TransNum INT;
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

