# dbo.FNDTN_SL_OBJECT_PU

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SL_OBJECT_PU"]
    FNDTN_SL_OBJCT(["FNDTN_SL_OBJCT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SL_OBJCT |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SL_OBJECT_PU
@objectId int, 
@userId int
as
/* 
   Proc to update the last usage of the object
   created id 

    Modifications:
    --------------
    Ashraf Zaid		May 26 2003  - Developed.
	Jacek Furmankiewicz 	May 2004 - Ported Sl_Object_UpdateLastUsage to new naming scheme
*/

	UPDATE FNDTN_SL_OBJCT
	set LAST_USED_DATE = GetDate(),
	LAST_USED_ID = @userId
	WHERE OBJCT_ID = @objectId
```

