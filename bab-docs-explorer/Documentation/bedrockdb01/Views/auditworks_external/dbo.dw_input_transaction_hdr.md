# dbo.dw_input_transaction_hdr

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_transaction_hdr"]
    dbo_input_transaction_hdr(["dbo.input_transaction_hdr"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_transaction_hdr |

## View Code

```sql
CREATE VIEW dbo.dw_input_transaction_hdr AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       cashier_no,
       transaction_category,
       deposit_declaration_flag,
       tax_jurisdiction_store,
       pos_tax_jurisdiction,
       trans_void_flag,
       pos_tender_total,
       pos_tender_total_sign,
       employee_no,
       closeout_flag,
       tax_override_flag,
       transaction_remark,
       till_no,
       pos_transaction_series,
       row_sequence_no FROM dbo.input_transaction_hdr
```

