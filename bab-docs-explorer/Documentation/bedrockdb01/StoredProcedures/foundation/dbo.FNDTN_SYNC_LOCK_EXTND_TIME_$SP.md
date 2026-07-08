# dbo.FNDTN_SYNC_LOCK_EXTND_TIME_$SP

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SYNC_LOCK_EXTND_TIME_$SP"]
    FNDTN_SYNC_LOCK(["FNDTN_SYNC_LOCK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SYNC_LOCK |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SYNC_LOCK_EXTND_TIME_$SP 
(
  @sync_lock_id    binary(16),
  @new_expiry_date datetime
)
AS
 
  /* Procedure	: FNDTN_SYNC_LOCK_EXTND_TIME_$SP		*/
  /* Author	: Ian Kendrick					*/
  /* Date	: 22 Feb 2005					*/
  /*								*/
  /* Purpose	: Extend existing locks expiry date		*/
  
DECLARE

  @success int,
  @errno   int
  
BEGIN
  
  /* First lock FNDTN_SYNC_LOCK table as cannot be concurrently used */
    
  SELECT @success = 1
  
  BEGIN TRAN
  
  SELECT TOP 1 SYNC_LOCK_ID FROM FNDTN_SYNC_LOCK WITH (TABLOCKX)
  
  UPDATE FNDTN_SYNC_LOCK
     SET EXPRY_DATE   = @new_expiry_date
   WHERE SYNC_LOCK_ID = @sync_lock_id

  SELECT @errno = @@error
  IF @errno <> 0
     SELECT @success = 0
        
  COMMIT
  
  RETURN @success
  
END
```

