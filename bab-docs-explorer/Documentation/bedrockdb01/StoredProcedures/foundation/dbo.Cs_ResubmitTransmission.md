# dbo.Cs_ResubmitTransmission

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Cs_ResubmitTransmission"]
    Cs_ReTransmission(["Cs_ReTransmission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Cs_ReTransmission |

## Stored Procedure Code

```sql
create proc dbo.Cs_ResubmitTransmission  @orig_transmission_id int, @user_id int 

/*  
	                                                  
   Author: Chris Carveth                         
   Creation Date: May-29-2001 
 
 
Modified by		Date		Defect		Reason 
----------------------------------------------------------------------------------------------------------------------
Adam W			11/12/2001	57		added a check to see if the transmission was already submitted
Adam W			09/26/2001			added status_id to the insert since its a required field
*/ 

AS 

DECLARE @result int,
        @row_exists int

	 
	select @result = -1 

    /* make sure a request hasn't been submitted already */
	select @row_exists = count(*) 
   	  from Cs_ReTransmission
 	 where transmission_id = @orig_transmission_id
             
    if @row_exists > 0 
    begin
      select @result = -2  
      goto EndOfProc
    end 
 
    insert into Cs_ReTransmission (transmission_id, user_id, request_datetime, status_id) 
     values (@orig_transmission_id, @user_id, getdate(), 0)
  
	select @result = 0

EndOfProc:
	 
RETURN @result
```

