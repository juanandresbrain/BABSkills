# dbo.FNDTN_SYNC_RLS_SRV_$SP

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SYNC_RLS_SRV_$SP"]
    FNDTN_SYNC_LOCK(["FNDTN_SYNC_LOCK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SYNC_LOCK |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SYNC_RLS_SRV_$SP ( @service_name varchar(50),
  @machine_name varchar(50),
  @start_date   datetime    
)
AS
 
  /* Procedure	: FNDTN_SYNC_RLS_SRV_$SP	 			*/
  /* Author	: Ian Kendrick						*/
  /* Date	: 13 Jan 2005						*/
  /*									*/
  /* Purpose	: Release a all locks for a service / machine /date	*/
  
DECLARE

  @success      int,
  @errno        int
  
BEGIN

  SELECT @success = 1

  DELETE FROM FNDTN_SYNC_LOCK
        WHERE SRVC_NAME  = @service_name
          AND MCHN_NAME  = @machine_name
          AND STRT_DATE < @start_date
        
  SELECT @errno = @@error
  IF @errno <> 0
     SELECT @success = 0
  
  RETURN @success
  
END
```

