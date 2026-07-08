# dbo.Tr_CloseDir

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_CloseDir"]
    Tr_Directory(["Tr_Directory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Tr_Directory |

## Stored Procedure Code

```sql
create proc dbo.Tr_CloseDir @CompanyID int, @OldDirectory varchar(255), @NewDirectory varchar(255)
/********************************************************************************

    Author	Michael Orsoni
    Creation Date: 08-March-2000
    Comments:	Update Translate history table

*********************************************************************************/
AS
	UPDATE Tr_Directory
	   SET dir_close_date_time = getdate(), path = @NewDirectory
	 WHERE path = @OldDirectory
	   AND company_id = @CompanyID
	   AND dir_close_date_time IS NULL 

RETURN 0
```

