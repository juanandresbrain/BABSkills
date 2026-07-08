# dbo.MNTRNG_P_ID_MNGR

**Database:** foundation_event  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.MNTRNG_P_ID_MNGR"]
    ID_MNGR(["ID_MNGR"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ID_MNGR |

## Stored Procedure Code

```sql
/**************************************************************** 
 Name           : MNTRNG_P_ID_MNGR 
 Purpose        : Returns the next ID for a table
 Parameters     : @TBL_ID: ID of a table
 Returns        : -1 in case of error, Next ID in case of success
 Created by     : Philippe Lanthier 
 Creation Date  : Jan-18-2005
****************************************************************/ 
CREATE PROCEDURE [dbo].[MNTRNG_P_ID_MNGR] 

@TBL_ID as int			

AS

DECLARE @NEXT_ID   int,
        @MAX_ID    int

SET @NEXT_ID = -1

BEGIN TRANSACTION

SELECT @NEXT_ID = LAST_ID + 1,
       @MAX_ID = MAX_ID
  FROM ID_MNGR
 WHERE TBL_ID = @TBL_ID

IF @@ERROR <> 0
BEGIN
   ROLLBACK TRANSACTION
   RETURN -1
END

--Loop to first value if max is reached
IF @NEXT_ID >= @MAX_ID
   SELECT @NEXT_ID = 0

--Update the new value
UPDATE ID_MNGR
   SET LAST_ID = @NEXT_ID
 WHERE TBL_ID = @TBL_ID

IF @@ERROR <> 0
BEGIN
   ROLLBACK TRANSACTION
   RETURN -1
END

COMMIT TRANSACTION

RETURN @NEXT_ID
```

