# dbo.vwdw_merchandise_plan_facts

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_merchandise_plan_facts"]
    dbo_merchandise_plan_facts(["dbo.merchandise_plan_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.merchandise_plan_facts |

## View Code

```sql
create view dbo.vwdw_merchandise_plan_facts
AS
select * from LH_Mart.dbo.merchandise_plan_facts
```

