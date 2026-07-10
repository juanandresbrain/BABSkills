# dbo.spUpdateBatchNumbers

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spUpdateBatchNumbers"]
    dbo_BusinessConductResults(["dbo.BusinessConductResults"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.BusinessConductResults |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Brian E. Byas>
-- Create date: <12-15-2015>
-- Description:	<Gets Max batch number to identify if the job needs to stop assigning new batch #'s>
-- =============================================
CREATE PROCEDURE [dbo].[spUpdateBatchNumbers] @batchNum int OUTPUT

AS


DECLARE @maxBatch AS int
SET @maxBatch = (SELECT
		MAX(BatchNumber)
	FROM
		[Dwstaging].[dbo].BusinessConductResults WITH (NOLOCK)
	WHERE
		documentcode = 'BCP'+CONVERT(VARCHAR,YEAR(getdate()))) + 1
SELECT
	@maxBatch

UPDATE this
	SET BatchNumber = @maxBatch
FROM
	(SELECT TOP 100
			bcr.recID,
			bcr.BatchNumber
		FROM
			[Dwstaging].[dbo].BusinessConductResults bcr WITH (NOLOCK)
		WHERE
			documentcode = 'BCP'+CONVERT(VARCHAR,YEAR(getdate()))
			AND bcr.BatchNumber = 0
		ORDER BY	bcr.EmpLastName,
					bcr.EmpFirstName)
	this

SET @batchNum = (SELECT
	COUNT(*)
FROM
	[Dwstaging].[dbo].BusinessConductResults bcr WITH (NOLOCK)
WHERE
	documentcode = 'BCP'+CONVERT(VARCHAR,YEAR(getdate()))
	AND bcr.BatchNumber = @maxBatch)
```

