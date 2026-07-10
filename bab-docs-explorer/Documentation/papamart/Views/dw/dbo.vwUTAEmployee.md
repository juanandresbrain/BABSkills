# dbo.vwUTAEmployee

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwUTAEmployee"]
    uhcmemp(["uhcmemp"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| uhcmemp |

## View Code

```sql
CREATE view [dbo].[vwUTAEmployee]

as

-- Replaced on 10/24/2023
-- Need to Use Preferred Name if Available 
/*
select 
e.eepEEID as Emp_Name, 
concat(e.EepNameLast,', ',e.EepNameFirst) as Emp_Fullname, 
e.EecLocation 

from uhcmemp e
where 1=1
--and ISNUMERIC(e.EecLocation) = 1
--and e.EepEEID = '0055533'
group by
e.eepEEID, 
concat(e.EepNameLast,', ',e.EepNameFirst), 
e.EecLocation 

*/


with RawData as 
(
select 
e.eepEEID as Emp_Name, 
e.EepNameLast, 
e.EepNameFirst, 
e.EepNamePreferred, 
e.EecLocation
from uhcmemp e
where 1=1
--and ISNUMERIC(e.EecLocation) = 1
--and e.EepNameFirst <> e.EepNamePreferred
--and e.EepEEID in ('0065246','2017339','0001812','0042207')
--order by e.EepNamePreferred

), 

Summary1 as 

(

select 
r.Emp_Name,
r.EepNameLast, 
case when r.EepNamePreferred <> r.EepNameFirst and r.EepNamePreferred <> ''
		then r.EepNamePreferred
	when r.EepNamePreferred is null 
		then r.EepNameFirst
	when r.EepNamePreferred = ''
		then r.EepNameFirst
	else r.EepNameFirst
	end as FirstName, 
	
	r.EecLocation
from RawData r

) 

Select 
s.Emp_Name, 
concat(s.EepNameLast,', ',s.FirstName) as Emp_Fullname, 
s.EecLocation 
From Summary1 s
group by 
s.Emp_Name, 
concat(s.EepNameLast,', ',s.FirstName), 
s.EecLocation
```

