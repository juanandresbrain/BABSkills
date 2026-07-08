# dbo.flash_parameters

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.flash_parameters"]
    dbo_parameter_general(["dbo.parameter_general"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.parameter_general |

## View Code

```sql
create view dbo.flash_parameters as
select max_date = null,
       flash_date = null,
       flash_budget_detail = 'D',
       flash_budget_split  = 'E',
       percentage1         = 0,
       percentage2         = 0,
       percentage3         = 0,
       percentage4         = 0,
       percentage5         = 0,
       percentage6         = 0,
       percentage7         = 0,
       multi_currency      = 0,
       common_currency     = 0,
       history_days        = 0,
       purge_date          = null
  from dbo.parameter_general
```

