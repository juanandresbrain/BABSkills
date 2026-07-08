# dbo.dw_input_post_void_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_post_void_detail"]
    dbo_input_post_void_detail(["dbo.input_post_void_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_post_void_detail |

## View Code

```sql
CREATE VIEW dbo.dw_input_post_void_detail AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       post_voided_register,
       post_voided_trans_no,
       post_void_successful,
       post_void_reason_code,
       lookup_pos_code,
       pos_description,
       row_sequence_no FROM dbo.input_post_void_detail
```

