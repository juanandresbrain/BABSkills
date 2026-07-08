# dbo.emp_merch_salesperson2

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emp_merch_salesperson2"]
    sv_employee(["sv_employee"]) --> VIEW
    sv_merchandise_detail(["sv_merchandise_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| sv_employee |
| sv_merchandise_detail |

## View Code

```sql
create view dbo.emp_merch_salesperson2 as 
select distinct m.salesperson2 as employee_no,
    e.employee_first_name, e.employee_last_name, e.home_store_no,
    e.employee_type, e.verified,e.house_account_no,
    e.date_of_hire, e.date_of_termination,
    e.employee_department, e.employee_type_descr,
    e.timestamp
from sv_merchandise_detail m    
left outer join sv_employee e
on m.salesperson2 = e.employee_no
```

