# dbo.FNDTN_SYNC_MASS_LOCK_$SP

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SYNC_MASS_LOCK_$SP"]
    FNDTN_SYNC_LOCK(["FNDTN_SYNC_LOCK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SYNC_LOCK |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SYNC_MASS_LOCK_$SP 
( @family_id    int,
  @service_name varchar(50),
  @segment_id   numeric(12,0),
  @job_id       int,
  @execution_id int,
  @process_id   int,
  @machine_name varchar(50),
  @sync_lock_id binary(16)   out,
  @error_msg    varchar(255)  out,
  @expiry_date  datetime = null     
)
AS
 
  /* Procedure	: FNDTN_SYNC_MASS_LOCK_$SP	 			*/
  /* Author	: Ian Kendrick						*/
  /* Date	: 12 Jan 2005						*/
  /*									*/
  /* Purpose	: Put multiple locks into the FNDTN_SYNC_LOCK table	*/
  
DECLARE

  @success      int,
  @token        varchar(50),
  @used_service varchar(50)
  
BEGIN

  IF @process_id   = -1 SELECT @process_id   = null
  IF @segment_id   = -1 SELECT @segment_id   = null
  IF @job_id       = -1 SELECT @job_id       = null
  IF @execution_id = -1 SELECT @execution_id = null
  IF @machine_name = '' SELECT @machine_name = null
  IF @service_name = '' SELECT @service_name = null

  SELECT @sync_lock_id = null, @error_msg = null, @success = 0
  
  /* First lock FNDTN_SYNC_LOCK table as cannot be concurrently used */
  
  BEGIN TRAN
  
  SELECT TOP 1 SYNC_LOCK_ID FROM FNDTN_SYNC_LOCK WITH (TABLOCKX)

  /* Remove any expired locks that belong to the requested token */
  
  IF EXISTS (SELECT 1 FROM FNDTN_SYNC_LOCK WHERE TKN = @token AND EXPRY_DATE < getdate() AND EXPRY_DATE IS NOT NULL)
  BEGIN
  
    DELETE FROM FNDTN_SYNC_LOCK
      WHERE TKN        = @token
        AND EXPRY_DATE < getdate()
        AND EXPRY_DATE IS NOT NULL
        
  END
  
  SELECT @sync_lock_id = newid()
              
  /* Pass through all tokens in table and try to lock each one */
  
  DECLARE c_multilock CURSOR
    FOR
    SELECT TKN
      FROM #SYNC_MASS_LOCK

  OPEN c_multilock

  WHILE 1=1
  BEGIN
  
     FETCH c_multilock
      INTO @token
      
     IF @@fetch_status <> 0
       BREAK
    
    IF EXISTS (SELECT 1 FROM FNDTN_SYNC_LOCK WHERE TKN = @token AND FMLY_ID = 0)
      BEGIN
      
        SELECT @used_service=SRVC_NAME
          FROM FNDTN_SYNC_LOCK
         WHERE TKN = @token AND FMLY_ID = 0

        IF @success = 1
         SELECT @success = 2
         
        SELECT @error_msg = 'Token name already uniquely locked by service ' + @used_service

      END
    ELSE
      BEGIN
        
        /* Next see if locked required belongs to same family */
        
        IF EXISTS (SELECT 1 FROM FNDTN_SYNC_LOCK WHERE TKN = @token AND FMLY_ID != @family_id)
          BEGIN
          
            SELECT @used_service=SRVC_NAME
              FROM FNDTN_SYNC_LOCK
             WHERE TKN = @token AND FMLY_ID != @family_id
         
            /* Not cool, already locked by different family */

            IF @success = 1
              SELECT @success = 2
              
            SELECT @error_msg = 'Token name already locked by service ' + @used_service
            
          END  
        ELSE
          BEGIN
          
            /* Cool, we can set a lock for this token family */
            
            INSERT INTO FNDTN_SYNC_LOCK
                 VALUES (@sync_lock_id,
                         @token,
                         @family_id,
                         @service_name,
                         @segment_id,
                         @job_id,
                         @execution_id,
                         @process_id,
                         @machine_name,
                         getdate(),
                         @expiry_date)
                         
            DELETE FROM #SYNC_MASS_LOCK
                  WHERE TKN = @token
                         
            IF @success = 0
              SELECT @success = 1                         
                                    
          END

      END

  END
  
  CLOSE c_multilock

  DEALLOCATE c_multilock
  
  COMMIT
  
  RETURN @success
  
END
```

