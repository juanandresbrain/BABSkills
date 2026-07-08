# dbo.emp_txn_purchasing

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emp_txn_purchasing"]
    sv_employee(["sv_employee"]) --> VIEW
    transaction_header(["transaction_header"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| sv_employee |
| transaction_header |

## View Code

```sql
create view dbo.emp_txn_purchasing as 
select distinct h.employee_no,
    e.employee_first_name, e.employee_last_name, e.home_store_no,
    e.employee_type, e.verified,e.house_account_no,
    e.date_of_hire, e.date_of_termination,
    e.employee_department, e.employee_type_descr,
    e.timestamp
from transaction_header h
left outer join sv_employee e
on h.employee_no = e.employee_no
```

