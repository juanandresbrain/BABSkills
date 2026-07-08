# dbo.Ex_GetNextFileNum

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_GetNextFileNum"]
    Ex_OutputNumber(["Ex_OutputNumber"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_OutputNumber |

## Stored Procedure Code

```sql
create proc dbo.Ex_GetNextFileNum   @db_group_id int, @object_id int
 
/*
                                             		 
 Author: Andrea Nagy                         	 
 Creation Date: 03-October-2000             	 
 Comments:                                    	 
                                                       
 Modified by		Date		Reason
 ------------------------------------------------------------------------
 Chris			24-Sep-02	Mods related to CS file numbering and new reset type.
                                                      
*/

AS
DECLARE @file_num numeric,
        @reset_type int,
        @last_updated datetime

SELECT @file_num = file_number,
       @reset_type = isnull(reset_flag, 0),
       @last_updated = isnull(last_updated, '01/01/90')
  FROM Ex_OutputNumber 
 WHERE db_group_id = @db_group_id
   AND object_id = @object_id

IF @file_num IS NULL 
BEGIN
    INSERT INTO Ex_OutputNumber(file_number, object_id, db_group_id, last_updated, reset_flag)
     VALUES(1, @object_id, @db_group_id, getdate(), 0)

    SELECT @file_num = 1  
END
ELSE
BEGIN
    IF @reset_type = 0 
       SELECT @file_num = @file_num + 1
    ELSE
    BEGIN
	-- If the last_updated date is the same as the current date then the file_num needs to be 
	-- bumped up by 1. 
	IF convert(varchar(12), @last_updated, 101) = convert(varchar(12), getdate(), 101)
           SELECT @file_num = @file_num + 1
	ELSE
           SELECT @file_num = 1
    END
 
    UPDATE Ex_OutputNumber
       SET file_number = @file_num,
           last_updated = getdate()
     WHERE db_group_id = @db_group_id
       AND object_id = @object_id

END

     
RETURN @file_num
```

