# dbo.vw_test1

**Database:** WH_Integration  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_test1"]
    test1(["test1"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| test1 |

## View Code

```sql
CREATE   view vw_test1 as
(select * from test1)
```

