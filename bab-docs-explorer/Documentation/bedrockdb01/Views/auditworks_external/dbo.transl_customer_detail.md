# dbo.transl_customer_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transl_customer_detail"]
    dbo_ext_customer_detail(["dbo.ext_customer_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ext_customer_detail |

## View Code

```sql
CREATE VIEW dbo.transl_customer_detail AS
   SELECT store_no,
          register_no,
          entry_date_time,
          transaction_series,
          transaction_no,
          line_id,
          customer_role,
          customer_info_type,
          customer_info,
          lookup_pos_code,
          row_sequence_no,
          auto_config_verified
     FROM auditworks_work.dbo.ext_customer_detail
```

