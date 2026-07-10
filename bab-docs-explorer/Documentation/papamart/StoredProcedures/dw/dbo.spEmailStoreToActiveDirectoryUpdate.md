# dbo.spEmailStoreToActiveDirectoryUpdate

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmailStoreToActiveDirectoryUpdate"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmailStoreToActiveDirectoryUpdate] 
	@storeID varchar(30),
	@location varchar(10),
	@storeName varchar(288),
	@district varchar(100),
	@newADlogin varchar(8000),
	@initialPassword varchar(14)

--========================================================================================================================
--	2021-07-15	Ian Wallace	- Created proc 					
--========================================================================================================================

as

set nocount on

declare 
	@provisionText varchar(20),
	@subj varchar(152),
	@recip varchar(1000),
	@copy_recip varchar(1000),
	@cc varchar(100),
	@body nvarchar(max)


select @Subj = 'StoreMDM to Active Directory new store update'
	select @recip = 'zackd@buildabear.com;JenM@buildabear.com'
	--select @recip = 'ianw@buildabear.com'
	set @copy_recip = 'ianw@buildabear.com'
	select @ProvisionText = 'store update'


select @body = 
'<font face =arial size = 2><B>StoreMDM to Active Directory new store update</B><br>' +
'The following store account was added. <br> ' +
'</font>' +
	'<table border="1">' +
		'<tr><th><font face =arial size = 2>Store ID</font></th>' +
			'<th><font face =arial size = 2>Location</font></th>' +
			'<th><font face =arial size = 2>Store name</font></th>' +
			'<th><font face =arial size = 2>District</font></th>' +
			'<th><font face =arial size = 2>AD account</font></th>' +
			'<th><font face =arial size = 2>Initial password</font></th>' +
'<font face =arial size = 2>' +
    CAST ( ( SELECT td = @storeID,'',
                    td =@location, '',
					td = @storeName, '',
					td=  @district, '',
					td= @newADlogin, '',
					td=  @initialPassword,''
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
			@copy_recipients = @copy_recip,
			@blind_copy_recipients ='ianw@buildabear.com',
			@body = @body,
			@subject = @subj,
			@body_format = 'HTML'
```

