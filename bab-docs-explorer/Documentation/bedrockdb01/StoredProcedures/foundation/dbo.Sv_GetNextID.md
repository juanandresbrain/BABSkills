# dbo.Sv_GetNextID

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_GetNextID"]
    Sv_NextID(["Sv_NextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_NextID |

## Stored Procedure Code

```sql
create proc dbo.Sv_GetNextID @table_id 	int
as

/* 
	Proc to get a unique id for a table from Sv_NextID 

    Modifications:
    --------------
	Ashraf Zaid		    June 10 1997  - Developed.
    Chris C.            April 4, 2000 - Changed to avoid Deadlocks in Exports.
*/

DECLARE	@next_id 	int,
	    @max_id		int

    BEGIN TRANSACTION

	UPDATE Sv_NextID
	   SET next_id = next_id + 1
	 WHERE table_id = @table_id

	SELECT @next_id = next_id,
		   @max_id = max_id
  	  FROM Sv_NextID 
 	 WHERE table_id = @table_id

    COMMIT TRANSACTION

	IF @next_id = @max_id
		SELECT @next_id = 0

Return @next_id
```

