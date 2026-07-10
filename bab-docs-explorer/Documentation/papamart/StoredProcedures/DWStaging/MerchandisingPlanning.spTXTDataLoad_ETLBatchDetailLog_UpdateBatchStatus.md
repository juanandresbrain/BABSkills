# MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus"]
    MerchandisingPlanning_TXTDataLoad_ETLBatchDetailLog(["MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog |

## Stored Procedure Code

```sql
CREATE PROCEDURE MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus(
	@ETLBatchDetailLogID INT
	, @ETLStatusID INT
) AS 
BEGIN
	SET NOCOUNT ON;

	UPDATE MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog WITH(ROWLOCK)
	SET ETLStatusID = @ETLStatusID
		, ETLBatchDetailItemStartDateTime = CASE WHEN @ETLStatusID = 1
												THEN GETDATE()
											ELSE ETLBatchDetailItemStartDateTime
											END
		, ETLBatchDetailItemEndDateTime = CASE WHEN @ETLStatusID IN (2, 3)
												THEN GETDATE()
											ELSE ETLBatchDetailItemEndDateTime
											END
	WHERE ETLBatchDetailLogID = @ETLBatchDetailLogID
END
```

