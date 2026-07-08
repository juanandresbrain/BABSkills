# dbo.Target_Login

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Target_Login"]
    Sv_UserSession(["Sv_UserSession"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_UserSession |

## Stored Procedure Code

```sql
create proc dbo.Target_Login (@db_group_id int, @target_session_id int, @target_serial_no int)

/*******************************************************/
/*	                                                 */
/*	    Author   Andrea Nagy                         */
/*	    Creation Date  21-JUL-2000                   */
/*	    Comments   Logs the SV user into the target  */
/*	                    DB                           */
/*******************************************************/

AS

DECLARE   @current_spid int

begin

SELECT @current_spid = @@spid

UPDATE Sv_UserSession
   SET db_group_id = @db_group_id,
       target_session_id = @target_session_id,  
       target_serial_no = @target_serial_no
 WHERE session_id = @current_spid
      

end
```

