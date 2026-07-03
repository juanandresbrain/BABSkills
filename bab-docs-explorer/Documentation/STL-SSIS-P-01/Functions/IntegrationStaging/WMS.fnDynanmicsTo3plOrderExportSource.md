# WMS.fnDynanmicsTo3plOrderExportSource

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["WMS.fnDynanmicsTo3plOrderExportSource"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @seed | bigint | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql

CREATE FUNCTION [WMS].[fnDynanmicsTo3plOrderExportSource]
(  
	  @seed bigint
)	


RETURNS TABLE
as 
RETURN 
(

with DocumentNumber as (

select 
sourceid, 
destid, 
rec_type,
--@seed + DENSE_RANK() OVER (ORDER BY destid, rec_type) as document_number
@seed + DENSE_RANK() OVER (ORDER BY sourceid, destid, rec_type) as document_number -- Replaced Above on 2025-03-24
from wms.DynamicsTo3PLOrderExportStage 
group by 
sourceid, 
destid, 
rec_type


)

select 
s.sourceid, 
s.destid, 
s.rec_type, 
s.message, 
s.style_code, 
s.quantity, 
s.release_date, 
s.distribution_number, 
s.ref_field_1, 
s.short_desc, 
s.vendor_style, 
s.color_code, 
dn.document_number, 
s.DynamicsOrderId

from wms.DynamicsTo3PLOrderExportStage S
join DocumentNumber DN on s.sourceid=dn.sourceid
					and s.destid=dn.destid
					and s.rec_type=dn.rec_type


)
```
