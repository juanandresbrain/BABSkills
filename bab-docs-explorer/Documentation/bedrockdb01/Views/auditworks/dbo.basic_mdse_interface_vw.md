# dbo.basic_mdse_interface_vw

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.basic_mdse_interface_vw"]
    basic_mdse_interface(["basic_mdse_interface"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| basic_mdse_interface |

## View Code

```sql
create view dbo.basic_mdse_interface_vw  AS
SELECT upc_lookup_division, store_no, register_no, transaction_date, transaction_no,
       upc_no, units, gross_sales_amount, pos_discount_amount, employee_discount_amount,
       salesperson
FROM basic_mdse_interface
```

