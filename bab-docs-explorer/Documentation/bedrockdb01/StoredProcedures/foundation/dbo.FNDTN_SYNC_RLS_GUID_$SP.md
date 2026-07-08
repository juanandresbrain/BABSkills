# dbo.FNDTN_SYNC_RLS_GUID_$SP

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SYNC_RLS_GUID_$SP"]
    FNDTN_SYNC_LOCK(["FNDTN_SYNC_LOCK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SYNC_LOCK |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SYNC_RLS_GUID_$SP ( @sync_lock_id binary(16)       
)
AS
 
  /* Procedure	: FNDTN_SYNC_RELEASE GUID_$SP	 			*/
  /* Author	: Ian Kendrick						*/
  /* Date	: 12 Jan 2005						*/
  /*									*/
  /* Purpose	: Release a single lock in FNDTN_SYNC_LOCK by ID	*/
  
DECLARE

  @success      int,
  @errno        int
  
BEGIN

  SELECT @success = 1

  DELETE FROM FNDTN_SYNC_LOCK
        WHERE SYNC_LOCK_ID = @sync_lock_id
        
  SELECT @errno = @@error
  IF @errno <> 0
     SELECT @success = 0
     
  RETURN @success
  
END
```

