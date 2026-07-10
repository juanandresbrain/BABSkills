# dbo.vwDW_ReferenceNo_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_ReferenceNo_Dim"]
    discount_facts(["discount_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| discount_facts |

## View Code

```sql
create view vwDW_ReferenceNo_Dim as
select 'df' as source,
line_object_key, reference_no , sum(units) UnitsRedeemed,
count(distinct transaction_id) NoOfTransWithRefNo
from discount_facts df with (nolock)
where reference_no is not null 
group by line_object_key, reference_no
--order by line_object_key, count(distinct transaction_id) desc
```

