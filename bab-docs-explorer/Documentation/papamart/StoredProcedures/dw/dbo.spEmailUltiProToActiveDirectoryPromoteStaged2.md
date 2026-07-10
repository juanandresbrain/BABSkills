# dbo.spEmailUltiProToActiveDirectoryPromoteStaged2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmailUltiProToActiveDirectoryPromoteStaged2"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmailUltiProToActiveDirectoryPromoteStaged2] 
	@EmployeeID nvarchar(7),
	@EecLocation nvarchar(50),
	@EepNameFirst nvarchar(50),
	@EepNameLast nvarchar(50),
	@JbcJobCode nvarchar(50),
	@EecOrgLvl1Code nvarchar(50),
	@samaccountname nvarchar(50),
	@managerEmail nvarchar(100)

--========================================================================================================================
--	2020-05-06	Ian Wallace - Created proc 
--========================================================================================================================

as

set nocount on

declare 
	@provisionText varchar(20),
	@subj varchar(100),
	@recip varchar(1000),
	@copy_recip varchar(1000),
	@cc varchar(100),
	@body nvarchar(max)


select @Subj = 'UltiPro to Active Directory Employee account name update'
	--select @recip = 'ianw@buildabear.com'
	SET @recip = 'IT-ServiceDesk@buildabear.com;SarahMe@buildabear.com;ianw@buildabear.com'
	--SET @recip = 'ianw@buildabear.com'
	set @copy_recip = @managerEmail
	select @ProvisionText = 'C'


select @body = 
'<font face =arial size = 2><B>UltiPro to Active Directory store employee account name update staged</B><br>' +
'The following employee record account name or email is new or has changed. <br> ' +
'The employee may need to be notified of this samaccountname as their new login username. <br> ' +
'</font>' +
	'<table border="1">' +
		'<tr><th><font face =arial size = 2>ProvisioningEvent</font></th>' +
			'<th><font face =arial size = 2>EmployeeID</font></th>' +
			'<th><font face =arial size = 2>Location</font></th>' +
			'<th><font face =arial size = 2>First Name</font></th>' +
			'<th><font face =arial size = 2>Last Name</font></th>' +
			'<th><font face =arial size = 2>Job Code</font></th>' +
			'<th><font face =arial size = 2>samaccountname</font></th>' +
'<font face =arial size = 2>' +
    CAST ( ( SELECT td = @provisionText,'',
                    td = @EmployeeID, '',
					td = @EecLocation, '',
					td=  @EepNameFirst, '',
					td=  @EepNameLast, '',
					td=  @JbcJobCode,'',
                    td = @samaccountname, ''	
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
			--@copy_recipients = @managerEmail,
			@body = @body,
			@subject = @subj,
			@body_format = 'HTML'
```

