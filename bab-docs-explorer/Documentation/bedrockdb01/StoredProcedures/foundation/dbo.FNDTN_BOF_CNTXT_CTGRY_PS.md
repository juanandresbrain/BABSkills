# dbo.FNDTN_BOF_CNTXT_CTGRY_PS

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_BOF_CNTXT_CTGRY_PS"]
    FNDTN_BOF_NEXT_ID(["FNDTN_BOF_NEXT_ID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_BOF_NEXT_ID |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_BOF_CNTXT_CTGRY_PS
@i_table_id 	int
as
/* 
   Proc to get a unique id for a table from FNDTN_BOF_NEXT_ID  

    Modifications:
    --------------
    Ashraf Zaid		May 26 2003  - Developed.
    Tim Nishikawa	June 02 2003 - Corrected table name to Bof_NextId
    Tim Nishikawa	Feb 17 2004  - Renamed parameter to match the Oracle version of proc.
	Jacek Furmankiewicz	May 2004 - Ported old Bof_GetNextID to new naming standard
*/

DECLARE	@next_id 	int,
    @max_id		int

    BEGIN TRANSACTION

	UPDATE FNDTN_BOF_NEXT_ID 
	   SET NEXT_ID  = NEXT_ID + 1
	 WHERE TBL_ID  = @i_table_id

	SELECT @next_id = NEXT_ID,
		@max_id = MAX_ID
  	  FROM FNDTN_BOF_NEXT_ID
 	 WHERE TBL_ID = @i_table_id

    COMMIT TRANSACTION

	IF @next_id >= @max_id
		SELECT @next_id = 0

Return @next_id
```

