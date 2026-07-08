# dbo.transl_transaction_line_link

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transl_transaction_line_link"]
    dbo_awl_transaction_line_link(["dbo.awl_transaction_line_link"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.awl_transaction_line_link |

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
     FROM auditworks_work.dbo.awl_transaction_line_link
```

