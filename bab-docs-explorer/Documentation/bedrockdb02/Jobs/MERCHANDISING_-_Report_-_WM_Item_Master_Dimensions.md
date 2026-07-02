# Job: MERCHANDISING - Report - WM Item Master Dimensions

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Queries WM for current Item Master Dimensions, outputs CSV and emails to logistics team.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - WM Item Master Dimensions"]
    JOB --> Generate_Report_Table_1["Step 1: Generate Report Table [TSQL]"]`n    JOB --> Send_E_mail_2["Step 2: Send E-mail [TSQL]"]`n```

## Steps

### Step 1: Generate Report Table
**Subsystem:** TSQL  

```sql
exec wmdb01.wmprod.dbo.spCreateItemMasterDimsReportTable
```

### Step 2: Send E-mail
**Subsystem:** TSQL  

```sql
Begin

		DECLARE @1query VARCHAR(1000)
		,@1file_name VARCHAR(100)
		,@1file_location VARCHAR(100)
		,@1server VARCHAR(20)
		,@1database VARCHAR(20)
		,@1sqlcmd VARCHAR(1000)
		,@1query_text VARCHAR(1000)
		,@1file VARCHAR(1000)
		,@1body VARCHAR(1000)
		,@1subj VARCHAR(1000)

	SELECT @1query_text = 'set nocount on select * from WMDB01.WMPROD.DBO.ItemMasterDimsReportTable order by style'

	SET @1query = @1query_text
	SET @1file_location = '\\kermode\FileRepository\MERCHANDISING\WM\ITEM_MASTER_DIMS\'
	SET @1file_name = 'WM_Item_Master_Dims.csv'
	SET @1server = 'bedrockdb02'
	SET @1database = 'me_01'
	SET @1sqlcmd = 'sqlcmd -S' + @1server + ' -d' + @1database + ' -Q' + '"' + @1query + '"' + ' -o' + '"' + @1file_location + @1file_name + '"' + ' -s"," -w1000 -W'

	EXEC master..xp_cmdshell @1sqlcmd

	EXEC msdb.dbo.sp_send_dbmail 
		@profile_name = 'MerchAdmin',
		@recipients= 'SantiagoB@buildabear.com;KristyK@buildabear.com',
		--@copy_recipients = 'MerchAdmin@buildabear.com' ,		
		@subject = 'WM Item Master Dimensions Report',
		@body = 'Please review attached report.',
		@file_attachments ='\\kermode\FileRepository\MERCHANDISING\WM\ITEM_MASTER_DIMS\WM_Item_Master_Dims.csv'

End
```


