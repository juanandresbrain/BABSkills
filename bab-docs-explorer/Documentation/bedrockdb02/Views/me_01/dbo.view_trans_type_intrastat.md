# dbo.view_trans_type_intrastat

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_trans_type_intrastat"]
    dbo_transaction_type(["dbo.transaction_type"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_type |

## View Code

```sql
CREATE view dbo.view_trans_type_intrastat
as
select transaction_type_id, transaction_type_code, transaction_type_desc,
 10 nature_of_transaction_code
from transaction_type
where transaction_type_code in (200,300,305,400,405,230,1970,1971)
union all
select transaction_type_id, transaction_type_code, transaction_type_desc,
 20 nature_of_transaction_code
from transaction_type
where transaction_type_code = 225
```

