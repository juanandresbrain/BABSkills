# dbo.spAWImport_110_Assign_BatchNumbers

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spAWImport_110_Assign_BatchNumbers"]
    aw_Transaction_Header(["aw_Transaction_Header"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| aw_Transaction_Header |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spAWImport_110_Assign_BatchNumbers]
-- =============================================================================================================
-- Name: spAWImport_110_Assign_BatchNumbers
--
-- Description:	
--	Assign the Batch numbers for this import run
--
--
-- Input:		
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Murrish	4/17/2013		Created

-- =============================================================================================================
AS

	SET NOCOUNT ON
	DECLARE	@batchNumber int,
			@recCount int
	SET @batchNumber = 1
	SET @recCount = 1



	WHILE @recCount > 0
	BEGIN
		WITH q
		AS (SELECT TOP 200000
			ath.batchNumber
		FROM aw_Transaction_Header ath WITH (NOLOCK)
		WHERE ath.batchNumber = 0)
		UPDATE q
		SET batchNumber = @batchNumber

		SET @batchNumber = @batchNumber + 1
		SET @recCount =
		ISNULL((SELECT
			COUNT(*)
		FROM aw_Transaction_Header ath
		WHERE ath.batchNumber = 0)
		, 0)
	END
```

