# dbo.dw_input_customer

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_customer"]
    dbo_input_customer(["dbo.input_customer"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_customer |

## View Code

```sql
CREATE VIEW dbo.dw_input_customer AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       customer_role,
       title,
       first_name,
       last_name,
       address_1,
       address_2,
       city,
       county,
       state,
       country,
       post_code,
       telephone_no1,
       telephone_no2,
       customer_no,
       row_sequence_no,
       pos_tax_jurisdiction_code,
       fax,
       email_address FROM dbo.input_customer
```

