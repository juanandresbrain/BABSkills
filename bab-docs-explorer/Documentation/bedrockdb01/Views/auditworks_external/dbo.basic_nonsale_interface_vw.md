# dbo.basic_nonsale_interface_vw

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.basic_nonsale_interface_vw"]
    basic_nonsale_interface(["basic_nonsale_interface"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| basic_nonsale_interface |

## View Code

```sql
create view dbo.basic_nonsale_interface_vw  AS
SELECT register_no, cashier_no, transaction_no, store_no, transaction_date, entry_time,
       identifier, amount, subcode, quantity
FROM basic_nonsale_interface
```

