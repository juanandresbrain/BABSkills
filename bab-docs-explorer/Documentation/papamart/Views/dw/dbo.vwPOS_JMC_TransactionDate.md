# dbo.vwPOS_JMC_TransactionDate

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOS_JMC_TransactionDate"]
    JMC_sls_retail_line_item(["JMC_sls_retail_line_item"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| JMC_sls_retail_line_item |

## View Code

```sql
create view [dbo].[vwPOS_JMC_TransactionDate]

as

select 
device_id, 
sequence_number as Trans_Nbr, 
max (cast (last_update_time as date) )  as TransactionDateDerived
from JMC_sls_retail_line_item r
where 1=1
--and r.device_id = '1090-002'
--and r.sequence_number = '65'
group by 
device_id, 
sequence_number
--order by 3, 1
```

