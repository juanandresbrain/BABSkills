# dbo.dw_input_payroll_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_payroll_detail"]
    dbo_input_payroll_detail(["dbo.input_payroll_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_payroll_detail |

## View Code

```sql
CREATE VIEW dbo.dw_input_payroll_detail AS
SELECT input_id,
       store_no,
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
       lookup_pos_code,
       pos_description FROM dbo.input_payroll_detail
```

