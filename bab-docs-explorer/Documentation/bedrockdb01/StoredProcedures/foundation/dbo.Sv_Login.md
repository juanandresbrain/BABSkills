# dbo.Sv_Login

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_Login"]
    Sv_UserSession(["Sv_UserSession"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_UserSession |

## Stored Procedure Code

```sql
create proc dbo.Sv_Login (@user_id int, @app_id int)

/*******************************************************/
/*	                                                 */
/*	    Author   Andrea Nagy                         */
/*	    Creation Date  21-JUL-2000                   */
/*	    Comments   Logs the SV user into the SV      */
/*	                                                 */
/*******************************************************/

AS

DECLARE   @current_spid int

begin

SELECT @current_spid = @@spid

DELETE FROM Sv_UserSession
      WHERE session_id = @current_spid
      
INSERT INTO Sv_UserSession (user_id, session_id, serial_no,app_id, db_group_id, target_session_id, target_serial_no)
	VALUES (@user_id, @current_spid, NULL, @app_id, NULL, NULL, NULL)
end
```

