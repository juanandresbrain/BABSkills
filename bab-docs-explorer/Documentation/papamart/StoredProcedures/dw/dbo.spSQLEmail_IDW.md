# dbo.spSQLEmail_IDW

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSQLEmail_IDW"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spSQLEmail_IDW]

as


set nocount on


--=====================================================================================================================================
--=====================================================================================================================================

BEGIN
	
			Declare @Recip varchar(100),
					@text nvarchar(max),
					@Subj varchar(100)
	
				select 
					@subj = 'email test',
					@Recip = 'ianw@buildabear.com'
		
	
			exec msdb.dbo.sp_send_dbmail
				@profile_name = 'biadmin',
				@recipients = @Recip, 
				@body = @text,
				@subject = @subj,
				@body_format = 'HTML'
	
END
```

