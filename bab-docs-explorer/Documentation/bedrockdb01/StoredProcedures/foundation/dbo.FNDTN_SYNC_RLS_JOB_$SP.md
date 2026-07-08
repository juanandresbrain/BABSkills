# dbo.FNDTN_SYNC_RLS_JOB_$SP

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SYNC_RLS_JOB_$SP"]
    FNDTN_SYNC_LOCK(["FNDTN_SYNC_LOCK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SYNC_LOCK |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SYNC_RLS_JOB_$SP ( @job_id        int,
  @execution_id  int    
)
AS
 
  /* Procedure	: FNDTN_SYNC_RELEASE GUID_$SP	 			*/
  /* Author	: Ian Kendrick						*/
  /* Date	: 13 Jan 2005						*/
  /*									*/
  /* Purpose	: Release a all locks for a job / execution id		*/
  
DECLARE

  @success      int,
  @errno        int
  
BEGIN

  SELECT @success = 1

  DELETE FROM FNDTN_SYNC_LOCK
        WHERE JOB_ID    = @job_id
          AND EXCTN_ID  = @execution_id
        
  SELECT @errno = @@error
  IF @errno <> 0
     SELECT @success = 0
  
  RETURN @success
  
END
```

