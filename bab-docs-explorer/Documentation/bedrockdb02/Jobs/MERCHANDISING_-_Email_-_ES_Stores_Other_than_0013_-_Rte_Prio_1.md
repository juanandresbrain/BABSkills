# Job: MERCHANDISING - Email - ES Stores Other than 0013 - Rte Prio 1

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Email - ES Stores Other than 0013 - Rte Prio 1"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
set nocount on 

IF (Object_ID('tempdb..#es_rp') IS NOT null) DROP TABLE #es_rp
select location_code, location_name, routing_priority
into #es_rp
from location
where routing_priority = 1


if (select count (*) from #es_rp where location_code <> '0013') > 1 

begin 

	IF (Object_ID('tempdb..##es_rp2') IS NOT null) DROP TABLE ##es_rp2
	select l.location_code, l.location_name, l.routing_priority
	into ##es_rp2
	from location l
	Where l.routing_priority = '1'


	EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
		@recipients = 'merchadmin@buildabear.com;3144526954@text.att.net;3142396350@text.att.net',
		@subject = 'A location other than 0013 is Configured for ES!',
		@body = 'A location other than 0013 is configured as routing_priority 1 in Merchandising. Please investigate ASAP.
		
		',
		@profile_name = 'MerchAdmin',
		@query = 'set nocount on select * from ##es_rp2',
		@attach_query_result_as_file = '1' , 
		@query_result_separator = ',',
		@query_result_no_padding = '1'
	
	

end




MERCHANDISING - Email - FAO Schwarz	Yes	Everynight it sends an email with a table of all unreceived shipments for store 0311 located inside FAO Schwarz. The purpose is that they will pick which shipments they will receive, based on their need.
Updated on 11/14/2014 to add steps to also send emails to stores 0630, 0631, 0632, 0633, 0634	1	uno	TSQL	exec me_01.dbo.spMerchandisingEmailFAOShipments
MERCHANDISING - Email - FAO Schwarz	Yes	Everynight it sends an email with a table of all unreceived shipments for store 0311 located inside FAO Schwarz. The purpose is that they will pick which shipments they will receive, based on their need.
Updated on 11/14/2014 to add steps to also send emails to stores 0630, 0631, 0632, 0633, 0634	2	630	TSQL	exec me_01.dbo.spMerchandisingEmailMacysShipments0630
MERCHANDISING - Email - FAO Schwarz	Yes	Everynight it sends an email with a table of all unreceived shipments for store 0311 located inside FAO Schwarz. The purpose is that they will pick which shipments they will receive, based on their need.
Updated on 11/14/2014 to add steps to also send emails to stores 0630, 0631, 0632, 0633, 0634	3	631	TSQL	exec me_01.dbo.spMerchandisingEmailMacysShipments0631
MERCHANDISING - Email - FAO Schwarz	Yes	Everynight it sends an email with a table of all unreceived shipments for store 0311 located inside FAO Schwarz. The purpose is that they will pick which shipments they will receive, based on their need.
Updated on 11/14/2014 to add steps to also send emails to stores 0630, 0631, 0632, 0633, 0634	4	632	TSQL	exec me_01.dbo.spMerchandisingEmailMacysShipments0632
MERCHANDISING - Email - FAO Schwarz	Yes	Everynight it sends an email with a table of all unreceived shipments for store 0311 located inside FAO Schwarz. The purpose is that they will pick which shipments they will receive, based on their need.
Updated on 11/14/2014 to add steps to also send emails to stores 0630, 0631, 0632, 0633, 0634	5	633	TSQL	exec me_01.dbo.spMerchandisingEmailMacysShipments0633
MERCHANDISING - Email - FAO Schwarz	Yes	Everynight it sends an email with a table of all unreceived shipments for store 0311 located inside FAO Schwarz. The purpose is that they will pick which shipments they will receive, based on their need.
Updated on 11/14/2014 to add steps to also send emails to stores 0630, 0631, 0632, 0633, 0634	6	634	TSQL	exec me_01.dbo.spMerchandisingEmailMacysShipments0634
```


