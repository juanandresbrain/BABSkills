# dbo.emp_payroll

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emp_payroll"]
    payroll_detail(["payroll_detail"]) --> VIEW
    sv_employee(["sv_employee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| payroll_detail |
| sv_employee |

## View Code

```sql
create view dbo.emp_payroll as 
select distinct p.employee_no,
    e.employee_first_name, e.employee_last_name, e.home_store_no,
    e.employee_type, e.verified,e.house_account_no,
    e.date_of_hire, e.date_of_termination,
    e.employee_department, e.employee_type_descr,
    e.timestamp
from payroll_detail p    
left outer join sv_employee e
on p.employee_no = e.employee_no
```

