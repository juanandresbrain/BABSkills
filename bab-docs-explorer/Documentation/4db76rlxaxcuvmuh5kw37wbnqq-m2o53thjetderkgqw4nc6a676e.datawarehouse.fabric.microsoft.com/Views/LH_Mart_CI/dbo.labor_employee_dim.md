# dbo.labor_employee_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.labor_employee_dim"]
    dbo_labor_employee_dim(["dbo.labor_employee_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.labor_employee_dim |

## View Code

```sql
CREATE   VIEW [dbo].[labor_employee_dim] AS SELECT emp_key, store_key, emp_id, INS_DT, UPD_DT, ETL_LOG_ID, ETL_EVNT_ID FROM LH_Mart.dbo.labor_employee_dim;
```

