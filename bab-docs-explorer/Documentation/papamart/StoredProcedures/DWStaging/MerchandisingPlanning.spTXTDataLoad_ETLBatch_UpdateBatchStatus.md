# MerchandisingPlanning.spTXTDataLoad_ETLBatch_UpdateBatchStatus

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_ETLBatch_UpdateBatchStatus"]
    MerchandisingPlanning_TXTDataLoad_ETLBatch(["MerchandisingPlanning.TXTDataLoad_ETLBatch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| MerchandisingPlanning.TXTDataLoad_ETLBatch |

## Stored Procedure Code

```sql
CREATE PROCEDURE MerchandisingPlanning.spTXTDataLoad_ETLBatch_UpdateBatchStatus(
	@ETLBatchID INT
	, @ETLStatusID INT
) AS 
BEGIN
	SET NOCOUNT ON;

	UPDATE MerchandisingPlanning.TXTDataLoad_ETLBatch WITH(ROWLOCK)
	SET ETLStatusID = @ETLStatusID
		, ETLBatchStartDateTime = CASE WHEN @ETLStatusID = 1
										THEN GETDATE()
									ELSE ETLBatchStartDateTime
									END
		, ETLBatchEndDateTime = CASE WHEN @ETLStatusID IN (2, 3)
										THEN GETDATE()
									ELSE ETLBatchEndDateTime
									END
	WHERE ETLBatchID = @ETLBatchID
END
```

