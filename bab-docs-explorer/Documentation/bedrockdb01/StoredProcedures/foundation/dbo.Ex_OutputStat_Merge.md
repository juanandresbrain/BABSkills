# dbo.Ex_OutputStat_Merge

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_OutputStat_Merge"]
    Ex_OutputStat(["Ex_OutputStat"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_OutputStat |

## Stored Procedure Code

```sql
create proc dbo.Ex_OutputStat_Merge 

@ExecutionID int, @SequenceNo int, @ReturnCode int, 
 @FileSize int, @FileName varchar(255), @MergeDateTime varchar(30)

/*
Author: Chris Carveth
Creation Date: 28-Jan-2000                       
Comments: 

Modified by		Date		Reason
------------------------------------------------------------------------

*/

AS 

DECLARE @errno int,
	@errmsg char(100),
	@returnerrmsg char(120)

	UPDATE Ex_OutputStat 
	   SET merge_file_name = @FileName, 
	       merge_file_size = @FileSize, 
	       merge_return_code = @ReturnCode, 
	       merge_date_time = @MergeDateTime
	 WHERE execution_id = @ExecutionID
	   AND sequence_no = @SequenceNo

	SELECT @errno = @@error
      	 IF @errno != 0
      	   BEGIN
        	   SELECT @errmsg = 'Failed to UPDATE Ex_OutputStat'
        	   GOTO error           
      	   END
      	   
RETURN 1


error: 

IF @@trancount != 0
  ROLLBACK TRANSACTION
  
SELECT @errmsg = 'Ex_OutputStat_Merge ' + @errmsg 
if @errno < 100000 
     select @errno = @errno + 100000 

SET @returnerrmsg = @errno + ', ' + @errmsg

Raiserror(@returnerrmsg, 16, 1)

RETURN @errno
```

