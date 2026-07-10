# dbo.sp_InsertPartitionHistory

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_InsertPartitionHistory"]
    ASPartitionHistory(["ASPartitionHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ASPartitionHistory |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_InsertPartitionHistory]
(
    @partID    INT,
    @startTime DATETIME,
    @endTime   DATETIME = NULL
)
AS
	IF @endTime IS NULL
		SET @endTime = getdate()

	DECLARE @secsDiff INT
	SET @secsDiff = datediff(s, @startTime, @endTime)

	INSERT INTO ASPartitionHistory (partID
								  , refreshDateTime
								  , numSeconds)
	VALUES
		(@partID, @endTime, @secsDiff)
```

