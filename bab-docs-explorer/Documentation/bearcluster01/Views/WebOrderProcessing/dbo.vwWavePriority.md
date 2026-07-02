# dbo.vwWavePriority

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwWavePriority"]
    WM_Orders(["WM.Orders"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.Orders |

## View Code

```sql
CREATE view [dbo].[vwWavePriority] 

as 
with MaxOrderNum as 
(
select 
o.OrderNumber
,max (o.OrderNum) as MaxOrderNum
from [WebOrderProcessing].[WM].[Orders] o
where 1=1
and DATEDIFF(dd,OrderDate, getdate()) <= 30
group by o.OrderNumber
) 

select 
case when o.SourceSite = 'BABW-US'
              then 'BAB'
       when o.SourceSite = 'BABW-UK'
              then 'BABUK'
              end as Sitecode
,o.OrderNumber
,o.OrderType as WavePriority
from [WebOrderProcessing].[WM].[Orders] o
join MaxOrderNum mon on mon.OrderNumber = o.OrderNumber
       and mon.MaxOrderNum = o.OrderNum
where 1=1
group by 
case when o.SourceSite = 'BABW-US'
              then 'BAB'
       when o.SourceSite = 'BABW-UK'
              then 'BABUK'
              end
,o.OrderNumber
,o.OrderType
```

