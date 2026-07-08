# dbo.Sl_Sv_GetNextID_Ex

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sl_Sv_GetNextID_Ex"]
    Sl_Sv_NextID(["Sl_Sv_NextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sl_Sv_NextID |

## Stored Procedure Code

```sql
create proc dbo.Sl_Sv_GetNextID_Ex @table_id 	int, @number_of_ids 	int
as

/* 
    Proc to reserve a number of sequential unique ids for a table from Sl_Sv_NextID.
    Proc returns the last unique id reserved.

    Modifications:
    --------------
	Ashraf Zaid		    June 10 1997  - Developed.
    Chris C.            April 4, 2000 - Changed to avoid Deadlocks in Exports.
*/

DECLARE	@next_id 	int,
        @max_id		int

    BEGIN TRANSACTION

	UPDATE Sl_Sv_NextID
	   SET next_id = next_id + @number_of_ids
	 WHERE table_id = @table_id

	SELECT @next_id = next_id,
		   @max_id = max_id
  	  FROM Sl_Sv_NextID 
 	 WHERE table_id = @table_id

    COMMIT TRANSACTION

	IF @next_id >= @max_id
		SELECT @next_id = 0

Return @next_id
```

