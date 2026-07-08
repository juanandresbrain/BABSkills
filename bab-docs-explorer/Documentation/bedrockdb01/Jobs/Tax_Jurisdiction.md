# Job: Tax Jurisdiction

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Emails Jack and Retail Systems daily to inform if there are Tax Jurisdictions in AW with the Effective From date other than 1970-01-01.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Tax Jurisdiction"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
IF (Object_ID('tempdb..##taxj') IS NOT NULL) DROP TABLE ##taxj
select s.tax_jurisdiction
into ##taxj
from (select distinct tax_jurisdiction, tax_level from tax_rate) s
	left join tax_rate tr
	on tr.tax_jurisdiction = s.tax_jurisdiction
	and tr.tax_level = s.tax_level
	and effective_from_date = '1970-01-01 00:00:00'
where tr.effective_from_date is null
order by s.tax_jurisdiction

set nocount on 
declare @recipients varchar(8000)
declare @subject varchar(500)
declare @msg varchar(1000)
declare @copy_recipients varchar(8000)

set @recipients = 'jackm@buildabear.com'
set @copy_recipients = 'posadmin@buildabear.com'

set @subject = 'ALERT - Tax Jurisdictions in SA with Effective From Date other than 1970-01-01'
set @msg = 'Listed below are all Tax Jurisdictions in Sales Audit with Effective From Date other than 1970-01-01.' + (char(13)) + 'These need to be corrected in order for tax updates to flow through to the stores.' + (char(13)) + + (char(13)) 

if (select count(*) from ##taxj) > 0  
begin
	exec msdb.dbo.sp_send_dbmail
		@recipients = @recipients,
		@copy_recipients = @copy_recipients,
		@subject=@subject, 
		@query_result_width = 250,
		@body = @msg,
		@query= 'select * from ##taxj'

end

GO
```

