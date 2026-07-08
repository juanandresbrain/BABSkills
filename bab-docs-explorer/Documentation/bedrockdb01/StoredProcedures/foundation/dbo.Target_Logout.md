# dbo.Target_Logout

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Target_Logout"]
    Sv_UserSession(["Sv_UserSession"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_UserSession |

## Stored Procedure Code

```sql
create proc dbo.Target_Logout 

/*******************************************************/
/*	                                                 */
/*	    Author   Andrea Nagy                         */
/*	    Creation Date  21-JUL-2000                   */
/*	    Comments   Logs the SV user out of the       */
/*	                target DB                        */
/*******************************************************/

AS

DECLARE   @current_spid int

begin

SELECT @current_spid = @@spid

UPDATE Sv_UserSession
   SET db_group_id = NULL,
       target_session_id = NULL,
       target_serial_no = NULL
 WHERE session_id = @current_spid
      

end
```

