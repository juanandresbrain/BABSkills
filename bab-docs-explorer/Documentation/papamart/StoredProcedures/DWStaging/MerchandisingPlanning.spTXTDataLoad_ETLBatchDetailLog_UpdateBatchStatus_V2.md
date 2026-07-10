# MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2"]
    MerchandisingPlanning_TXTDataLoad_ETLBatchDetailLog_2(["MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog_2"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog_2 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [MerchandisingPlanning].[spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2](
	@ETLBatchDetailLogID INT
	, @ETLStatusID INT
) AS 
BEGIN
	SET NOCOUNT ON;

	UPDATE MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog_2 WITH(ROWLOCK)
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

