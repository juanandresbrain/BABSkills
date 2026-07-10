# dbo.spMetricFacts_DupeCheck_NEW

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMetricFacts_DupeCheck_NEW"]
    metric_facts(["metric_facts"]) --> SP
    mf(["mf"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| metric_facts |
| mf |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
--EXEC spMetricFacts_DupeCheck


CREATE      procedure [dbo].[spMetricFacts_DupeCheck_NEW]
AS

DECLARE @dupecnt int


select metric_dim_key,store_key,date_key,min(metric_facts_key) as metric_facts_key
into ##metric_facts_dupes
from dw..metric_facts (nolock)
group by metric_dim_key,store_key,date_key
having count(*) >1

SET @dupecnt = (select count(*) from ##metric_facts_dupes)

IF @dupecnt > 0
BEGIN
--NOTIFY OF ANY DUPES THAT WOULDN'T BE DELETED, BECAUSE THEY DIDN'T HAVE AMOUNT =0
	exec msdb.dbo.sp_send_dbmail @recipients='trista.parmentier@daugherty.com', @subject ='Metric_Facts Dupes PRE-FIX ', @query = 'select count(*) from ##metric_facts_dupes d join dw..metric_facts mf on mf.metric_facts_key = d.metric_facts_key and mf.store_key = d.store_key and mf.metric_dim_key = d.metric_dim_key and mf.date_key = d.date_key'

--REMOVE DUPES--
	delete mf
	from ##metric_facts_dupes d
		join metric_facts mf on mf.metric_facts_key = d.metric_facts_key 
			and mf.store_key = d.store_key 
			and mf.metric_dim_key = d.metric_dim_key
			and mf.date_key = d.date_key
	--where mf.amount = 0

--POST CHECK---
	exec msdb.dbo.sp_send_dbmail @recipients='trista.parmentier@daugherty.com', @subject ='Metric_Facts Dupes POST-FIX CHECK (expect 0)', @query = 'select count(*) from dw..metric_facts (nolock) group by metric_dim_key,store_key,date_key having count(*) >1'
	END
ELSE
	BEGIN
	exec msdb.dbo.sp_send_dbmail @recipients='trista.parmentier@daugherty.com', @subject ='Metric_Facts NO Dupes'
	END
```

