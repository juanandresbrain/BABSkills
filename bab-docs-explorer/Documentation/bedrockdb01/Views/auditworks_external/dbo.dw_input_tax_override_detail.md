# dbo.dw_input_tax_override_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_tax_override_detail"]
    dbo_input_tax_override_detail(["dbo.input_tax_override_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_tax_override_detail |

## View Code

```sql
CREATE VIEW dbo.dw_input_tax_override_detail AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       tax_level,
       tax_category,
       taxable,
       exception_tax_jurisdiction,
       tax_exempt_no,
       row_sequence_no FROM dbo.input_tax_override_detail
```

