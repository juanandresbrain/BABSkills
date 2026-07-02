# Job: MERCH ADMIN - ASNs missing in WM from TPM

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Checks for ASNs from TPM in shipped status but do not exist in WM. This job ws created on DB02 rather than wmdb01 because wmdb01 does not have the same sp send dbmail capabilities as DB02

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCH ADMIN - ASNs missing in WM from TPM"]
    JOB --> Select_Missing_ASNs_1["Step 1: Select Missing ASNs [TSQL]"]`n    JOB --> E_mail_Missing_ASNs_2["Step 2: E-mail Missing ASNs [TSQL]"]`n```

## Steps

### Step 1: Select Missing ASNs
**Subsystem:** TSQL  

```sql
exec wmdb01.wmprod.dbo.sp_Select_Missing_ASNs_from_TPM
```

### Step 2: E-mail Missing ASNs
**Subsystem:** TSQL  

```sql
if (select count(*) from wmdb01.wmprod.dbo.MissingASNinWM) > 0


Begin

Declare @BODY3 nvarchar(4000);

	set @BODY3 = '<font face = arial size = 2>' + 
			'The shipments below are marked as shipped in TPM but an ASN does not exist in WM.'+
			'<br>'+
			'You may find these rejected in the WM import tables. Without these ASNs the Bearhouse will not be able to receive or will be forced to perform a blind receipt.'+
			'<br>'+
			'<br>'+
			'<br>'+		
			'<br>'+
			'<br>'+
				'<table border="1">' +
				'<tr><th>Vendor_Code</th><th>TPM_ASN_NBR</th><th>TPM_Status_Date_Time</th><th>WM_ASN_NBR</th><th>WM_Inpt_Table</th><th>WM_Inpt_Mod_Time</th><th>Est_Deliv_Date</th></tr>' +
				CAST ( ( select td = m.Vendor_Code, '',
						td = m.TPM_ASN_NBR, '',
						td = m.TPM_Status_Date_Time, '',
						td = isnull(m.WM_ASN_NBR,''), '',
						td = isnull(m.WM_Inpt_Table,''), '',
						td = isnull(m.WM_Inpt_Mod_Time,''), '',
						td = isnull(m.Est_Deliv_Date,''), ''
						  from wmdb01.wmprod.dbo.MissingASNinWM m
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(4000) ) +
				'</font></table></font></p></p>
				<br>
				<br>
				<br>
			<font face =arial size = 1><i>The information in this message may be privileged, “confidential” and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an empl
	oyee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please
	 notify us immediately by replying to the message and deleting it from your computer.</i></font>'
	

		EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
			@recipients = 'MerchAdmin@buildabear.com',
			@subject = 'Shipments Marked as Shipped in TPM but ASN not in WM',
			@body = @BODY3,
			@profile_name = 'MerchAdmin',
			@body_format= HTML

End



```


