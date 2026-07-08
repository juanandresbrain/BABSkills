# dbo.Tr_ShouldWaitOnTPDirs

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_ShouldWaitOnTPDirs"]
    Tr_Directory(["Tr_Directory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Tr_Directory |

## Stored Procedure Code

```sql
create proc Tr_ShouldWaitOnTPDirs @CompanyID int, @Path varchar(255)
/******************************************************************

	Author		MICHAELO
	Creation Date	28/08/2001
	Comments	Checks if there are any other dirs
			processing that have either TPDONE files, 
			or have not yet received their done file.

******************************************************************/
AS 
DECLARE @ShouldWait int

	SELECT @ShouldWait = 0

	SELECT @ShouldWait = COUNT(*) 
	FROM Tr_Directory
	WHERE company_id = @CompanyID
	AND done_file_type != 1
	AND dir_close_date_time IS NULL
	AND path != @Path


RETURN @ShouldWait
```

