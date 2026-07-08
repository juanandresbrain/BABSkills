# dbo.dw_input_transaction_line_link

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_transaction_line_link"]
    dbo_input_transaction_line_link(["dbo.input_transaction_line_link"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_transaction_line_link |

## View Code

```sql
CREATE VIEW dbo.dw_input_transaction_line_link AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       linked_line_id,
       row_sequence_no FROM dbo.input_transaction_line_link
```

