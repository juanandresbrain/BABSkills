# MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation"]
    MerchandisingPlanning_TXTDataLoad_ValidationEmailDetailLog(["MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [MerchandisingPlanning].[spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_Validation](
	@ID INT
) AS 
BEGIN
	SET NOCOUNT ON;

	UPDATE MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog WITH(ROWLOCK)
	SET ETLValidationStatusID = 1	
	WHERE ID = @ID
END
```

