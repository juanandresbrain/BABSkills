# dbo.spEmailUltiProToActiveDirectoryDisplayNameUpdate

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmailUltiProToActiveDirectoryDisplayNameUpdate"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmailUltiProToActiveDirectoryDisplayNameUpdate] 
	@EmployeeID nvarchar(7),
	@EecLocation nvarchar(50),
	@EepNameFirst nvarchar(50),
	@EepNameLast nvarchar(50),
	@JbcJobCode nvarchar(50),
	@EecOrgLvl1Code nvarchar(50),
	@samaccountname nvarchar(50),
	@displayName nvarchar(50)

--========================================================================================================================
--	2019-05-17	Ian Wallace	- Created proc 
--========================================================================================================================

as

set nocount on

declare 
	@provisionText varchar(20),
	@subj varchar(152),
	@recip varchar(1000),
	@cc varchar(100),
	@body nvarchar(max)


select @Subj = 'UltiPro to Active Directory store manager display name update'
	select @recip = 'ianw@buildabear.com'
	select @ProvisionText = 'display name update'


select @body = 
'<font face =arial size = 2><B>UltiPro to Active Directory Employee Display Name update</B><br>' +
'The following employee display name was updated. <br> ' +
'</font>' +
	'<table border="1">' +
		'<tr><th><font face =arial size = 2>ProvisioningEvent</font></th>' +
			'<th><font face =arial size = 2>EmployeeID</font></th>' +
			'<th><font face =arial size = 2>Location</font></th>' +
			'<th><font face =arial size = 2>First Name</font></th>' +
			'<th><font face =arial size = 2>Last Name</font></th>' +
			'<th><font face =arial size = 2>Job Code</font></th>' +
			'<th><font face =arial size = 2>Display Name</font></th>' +
'<font face =arial size = 2>' +
    CAST ( ( SELECT td = @provisionText,'',
                    td = @EmployeeID, '',
					td = @EecLocation, '',
					td=  @EepNameFirst, '',
					td=  @EepNameLast, '',
					td=  @JbcJobCode,'',
					td = @displayName, ''
              FOR XML PATH('tr'), TYPE 
    ) AS NVARCHAR(MAX) ) +
    '</font></table></font></p></p>
    <br><br>' +
    '<br>
    <font face =arial size = 1><B>This report was run from SSIS as part of the UltiPro to Active Directory ETL. </B></font>
    <br>
    <br>
<font face =arial size = 1><i>The information in this message may be privileged, “confidential” and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'



		exec msdb.dbo.sp_send_dbmail
			@profile_name = 'BIAdmin',
			@recipients = @recip,
			@body = @body,
			@subject = @subj,
			@body_format = 'HTML'
```

