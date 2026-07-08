# dbo.emp_av_txn_purchasing

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emp_av_txn_purchasing"]
    av_transaction_header(["av_transaction_header"]) --> VIEW
    sv_employee(["sv_employee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| av_transaction_header |
| sv_employee |

## View Code

```sql
create view dbo.emp_av_txn_purchasing as 
select distinct h.employee_no,
    e.employee_first_name, e.employee_last_name, e.home_store_no,
    e.employee_type, e.verified,e.house_account_no,
    e.date_of_hire, e.date_of_termination,
    e.employee_department, e.employee_type_descr,
    e.timestamp
from av_transaction_header h
left outer join sv_employee e
on h.employee_no = e.employee_no
```

