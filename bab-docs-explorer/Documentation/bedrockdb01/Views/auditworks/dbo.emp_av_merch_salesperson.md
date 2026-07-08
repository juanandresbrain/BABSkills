# dbo.emp_av_merch_salesperson

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emp_av_merch_salesperson"]
    sv_av_merchandise_detail(["sv_av_merchandise_detail"]) --> VIEW
    sv_employee(["sv_employee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| sv_av_merchandise_detail |
| sv_employee |

## View Code

```sql
create view dbo.emp_av_merch_salesperson as 
select distinct m.salesperson as employee_no,
    e.employee_first_name, e.employee_last_name, e.home_store_no,
    e.employee_type, e.verified,e.house_account_no,
    e.date_of_hire, e.date_of_termination,
    e.employee_department, e.employee_type_descr,
    e.timestamp
from sv_av_merchandise_detail m    
left outer join sv_employee e
on m.salesperson = e.employee_no
```

