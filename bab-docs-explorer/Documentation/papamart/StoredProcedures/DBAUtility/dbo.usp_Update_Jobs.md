# dbo.usp_Update_Jobs

**Database:** DBAUtility  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_Update_Jobs"]
    JOBS(["JOBS"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| JOBS |

## Stored Procedure Code

```sql
create procedure usp_Update_Jobs @serverIn varchar(100),@DatabaseIn varchar(100),@JobIn varchar(100)

AS

DECLARE @Test Varchar(10)

SELECT @Test= 
(Select Server from JOBS
WHERE 
server 		=	@ServerIn
AND
Database_Name	=	@DatabaseIN
AND
Job		=	@JobIn
)
IF @Test IS NULL
BEGIN
	INSERT	JOBs
	VALUES	(@ServerIn, @DatabaseIn,@JobIn,GETDATE(),27)
END

UPDATE	JOBS
SET	UPDATED	= Getdate()

WHERE
server 		=	@ServerIn
AND
Database_Name	=	@DatabaseIN
AND
Job		=	@JobIn
```

