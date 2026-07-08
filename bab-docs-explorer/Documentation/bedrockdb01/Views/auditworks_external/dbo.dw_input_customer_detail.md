# dbo.dw_input_customer_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_customer_detail"]
    dbo_input_customer_detail(["dbo.input_customer_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_customer_detail |

## View Code

```sql
CREATE VIEW dbo.dw_input_customer_detail AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       customer_role,
       customer_info_type,
       customer_info,
       lookup_pos_code,
       row_sequence_no FROM dbo.input_customer_detail
```

