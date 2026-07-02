# Job: MERCHANDISING - Email - Shipment\Transfer Received as Zero Units

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Tami B in Distro put in a request for a report that would display shipments and locations that appeared to receive units as zero by just clicking Save\Receive and not specifying units or using the Receive as Sent button

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Email - Shipment\Transfer Received as Zero Units"]
    JOB --> Step_One_1["Step 1: Step One [TSQL]"]`n```

## Steps

### Step 1: Step One
**Subsystem:** TSQL  

```sql

-- Build Table of Store Shipments and Transfers Received Today 
select distinct a.application_identifier, a.application_type
into #today
from ib_audit_trail a
where field_affected = 'receive_date'
and application_type in ('StoreShipment','Transfer')
and convert(nvarchar,a.entry_date,101) = convert(nvarchar, GETDATE (), 101)

-- Build Table of SS and Xfer Detail Entries in Audit Trail table for shipments\transfers received today 
select *
into #details 
from ib_audit_trail
where application_level in ('StoreShipmentDETAILS','TransferDETAILS')
and application_identifier in (select application_identifier from #today)


-- Find Store Shipments that do not have receiving details in the audit trail
-- This appears to be indicative of when a user clicks save\receive without clicking receive\sent 
select t.application_identifier as document_number
into #no_details_store_shipment
from #today t
left join #details d on d.application_identifier=t.application_identifier
where d.ib_audit_trail_id is null
and t.application_type = 'StoreShipment'

-- Find Store Transfers that do not have receiving details in the audit trail
-- This appears to be indicative of when a user clicks save\receive without clicking receive\sent 
select t.application_identifier as document_number
into #no_details_transfer
from #today t
left join #details d on d.application_identifier=t.application_identifier
where d.ib_audit_trail_id is null
and t.application_type = 'Transfer'


-- Join to locational data for Store Shipments
select ndss.document_number, ss.document_no, l.location_code
into #Summary_SS
from #no_details_store_shipment ndss
join store_shipment ss on ss.document_no=ndss.document_number
join location l on l.location_id=ss.location_id

-- Join to locational data for Transfers 
select ndt.document_number, t.document_no, l.location_code
into #Summary_Xfer
from #no_details_transfer ndt
join transfer t on t.document_no=ndt.document_number
join location l on l.location_id=t.to_location_id

-- Create report table and send e-mail 
IF (Object_ID('me_01..Summary_All') IS NOT NULL) DROP TABLE Summary_All

create table Summary_All 
(
document_number nvarchar(20),
location_code varchar(4),
)

insert into Summary_All
select document_number, location_code
from #Summary_Xfer
union
select document_number, location_code
from #Summary_SS

if (select count (*) from Summary_all) > 0

Begin 

Declare @BODY3 nvarchar(max);		

set @BODY3 = '<font face =arial size = 2>' + 
			'<table border="1">' +
			'<tr><th>Document Number</th><th>Location Code </th></tr>' +
			CAST ( ( SELECT	td = sa.document_number, '',
							td = sa.location_code, ''
					  from me_01.dbo.Summary_all sa
					  FOR XML PATH('tr'), TYPE 
			) AS NVARCHAR(MAX) ) +
			'</font></table></font></p></p>
			<br>
			<br>
			<br>
'





EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
	@recipients = 'DistroBears@buildabear.com',
	--@copy_recipients = 'merchadmin@buildabear.com',
	@subject = 'Store Shipments\Transfers Received as Zero - Receive As Sent Button Not Used',
	@body = @BODY3,
	@body_format = 'html',
	@profile_name = 'MerchAdmin'

End
```


