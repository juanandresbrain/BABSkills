# dbo.transl_payroll_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transl_payroll_detail"]
    dbo_awl_payroll_detail(["dbo.awl_payroll_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.awl_payroll_detail |

## View Code

```sql
CREATE VIEW dbo.transl_payroll_detail AS
   SELECT store_no,
          register_no,
          entry_date_time,
          transaction_series,
          transaction_no,
          line_id,
          employee_no,
          payroll_date,
          employee_payroll_id,
          employee_type,
          payroll_entry_type,
          row_sequence_no,
          transaction_id,
          lookup_pos_code,
          pos_description 
     FROM auditworks_work.dbo.awl_payroll_detail
```

