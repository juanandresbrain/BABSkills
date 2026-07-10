# dbo.vwBO_Tender_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBO_Tender_Dim"]
    tender_dim(["tender_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| tender_dim |

## View Code

```sql
create view [dbo].[vwBO_Tender_Dim] as
select *,
case when tender_code in (621,633,640,690) then 'Total Redemptions'
when tender_code between 3001 and 6999 then 'Party Deposit'
when tender_code in (-1,600,601,603,604,605,606,608,609,611,630,642,699) then Tender_desc
when tender_code in (0,9007) then 'N/A'
else 'Other Tender' end as tender_summary
from tender_dim
```

