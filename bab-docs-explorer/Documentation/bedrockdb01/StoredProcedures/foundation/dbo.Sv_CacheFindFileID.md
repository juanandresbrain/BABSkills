# dbo.Sv_CacheFindFileID

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_CacheFindFileID"]
    Sv_OutputCache(["Sv_OutputCache"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_OutputCache |

## Stored Procedure Code

```sql
create proc dbo.Sv_CacheFindFileID 

@viewid int, @queryid int,
	@periodid int, @dbgroupid int, @securityqueryid int,
	@dynamicquery varchar(255), @qparametersbag varchar(255)

/*
Author: Tim Nishikawa
Creation Date: 28-Feb-2000
Comments: Returns cache_file_id of record in Sv_OutputCache which will
be used to store info on cache file for parameter info.

Modified by		Date		Reason
------------------------------------------------------------------------

*/
AS
DECLARE @found_file_id	      	int,
	@found_file_valid_date	datetime,
	@found_file_locked	int


BEGIN TRANSACTION
 
/* try to find file record matching parameter criteria */
SELECT @found_file_id = cache_file_id,
	@found_file_valid_date = valid_until,
	@found_file_locked = locked
	FROM Sv_OutputCache WITH(HOLDLOCK)
	WHERE view_id = @viewid
	AND query_id = @queryid
	AND period_id = @periodid
	AND db_group_id = @dbgroupid
	AND security_query_id = @securityqueryid
	AND dynamic_query = @dynamicquery
	AND qparameters_bag = @qparametersbag

IF ISNULL(@found_file_id, 0) > 0	/* IF file was found then... */
BEGIN

	/* check if found file is still valid */
	IF @found_file_valid_date < getdate()	/* no longer valid */
	BEGIN
		/*check if already locked */
		IF @found_file_locked = 1
			SELECT @found_file_id = 0
		ELSE
		BEGIN
			UPDATE Sv_OutputCache
			SET locked = 1
			WHERE cache_file_id = @found_file_id
		
			SELECT @found_file_id = @found_file_id * (-1)
		END
	END

	GOTO endofproc
END		

	/* IF file not found try to find blank record */
	SELECT @found_file_id = MIN(cache_file_id)
	FROM Sv_OutputCache WITH(HOLDLOCK)
	WHERE view_id = 0 AND query_id = 0 
	AND period_id = 0 AND db_group_id = 0 AND locked = 0

	/* IF file was found then save info & lock record */
	IF ISNULL(@found_file_id, 0) > 0
		GOTO saveandlock

	/* IF no more blank records, find oldest record */
	BEGIN
		SELECT @found_file_id = MIN(cache_file_id)
		FROM Sv_OutputCache WITH(HOLDLOCK)
		WHERE locked = 0 AND valid_until =
			(SELECT MIN(valid_until) FROM Sv_OutputCache
			 WHERE locked = 0)
	END
	
	/* IF file was found then save info & lock record */
	IF ISNULL(@found_file_id, 0) > 0
		GOTO saveandlock


	SELECT @found_file_id = 0
	ROLLBACK TRANSACTION
	GOTO endofproc
	
saveandlock: /* save new info and lock record */
	UPDATE Sv_OutputCache
	SET view_id = @viewid, query_id = @queryid,
	period_id = @periodid, db_group_id = @dbgroupid,
	security_query_id = @securityqueryid,
	dynamic_query = @dynamicquery,
	qparameters_bag = @qparametersbag,
	locked = 1
	WHERE cache_file_id = @found_file_id


	SELECT @found_file_id = @found_file_id * (-1)

	
endofproc:	/* end of procedure */
COMMIT TRANSACTION
RETURN @found_file_id
```

