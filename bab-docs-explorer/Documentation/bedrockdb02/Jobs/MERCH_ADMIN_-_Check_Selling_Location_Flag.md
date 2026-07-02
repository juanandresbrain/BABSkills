# Job: MERCH ADMIN - Check Selling Location Flag

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Checks to see if Selling Location flag is in sync between IB and MA because if flag is not enabled in MA, seasonal indices will not be generated for that location If not in sync, e-mail is sent to MerchAdmin

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCH ADMIN - Check Selling Location Flag"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
-- IB Lookup
select location_code, selling_location
into #i
from location l
where active_flag = 1 -- Active Location 
and location_type = 2 -- Store Type Location
and selling_location = 1 -- Selling Location Flag

--MA Lookup
select location_code as ma_locn_code, selling_location as ma_selling_location
into #m
from ma_01.dbo.location l
where active_flag = 1  -- Active Location 
and location_type = 2 -- Store Type Location
and selling_location = 1 -- Selling Location Flag


-- Comparison join

select i.location_code, m.ma_locn_code
into #Compare
from #i i 
left join #m m on i.location_code=m.ma_locn_code
where m.ma_locn_code is null


-- If out of sync send email 

if (select count(*) from #Compare) > 1 

Begin 



	EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
	@recipients = 'MerchAdmin@buildabear.com',
	@subject = 'Selling Location Flag Out of Sync Between IB and MA',
	@body = 'There are locations in IB that have the selling location flag checked but the MA location does not have the flag checked.
Please investigate as this will prevent seasonal indices to be generated for these locations. 
See Bedrockdb02 SQL Agent Job MERCH ADMIN - Check Selling Location Flag for details.',
	@profile_name = 'MerchAdmin'

	
End
```


