# dbo.dw_input_discount_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_discount_detail"]
    dbo_input_discount_detail(["dbo.input_discount_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_discount_detail |

## View Code

```sql
CREATE VIEW dbo.dw_input_discount_detail AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       line_id_adj,
       pos_discount_level,
       pos_discount_type,
       pos_discount_amount,
       pos_discount_amount_adj,
       discount_amount_sign,
       discount_applied_flag,
       applied_by_line_id,
       pos_discount_serial_no,
       row_sequence_no FROM dbo.input_discount_detail
```

