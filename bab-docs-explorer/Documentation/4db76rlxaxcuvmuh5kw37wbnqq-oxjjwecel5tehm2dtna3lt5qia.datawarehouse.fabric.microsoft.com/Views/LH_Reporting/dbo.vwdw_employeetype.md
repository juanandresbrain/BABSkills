# dbo.vwdw_employeetype

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_employeetype"]
    dbo_employee_type_dim(["dbo.employee_type_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.employee_type_dim |

## View Code

```sql
CREATE VIEW vwdw_employeetype
AS
SELECT * FROM LH_Mart.dbo.employee_type_dim
```

