# dbo.transl_transaction_line_link

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transl_transaction_line_link"]
    dbo_ext_transaction_line_link(["dbo.ext_transaction_line_link"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ext_transaction_line_link |

## View Code

```sql
CREATE VIEW dbo.transl_transaction_line_link AS
   SELECT store_no,
          register_no,
          entry_date_time,
          transaction_series,
          transaction_no,
          line_id,
          linked_line_id,
          row_sequence_no,
          transaction_id 
     FROM auditworks_work.dbo.ext_transaction_line_link
```

