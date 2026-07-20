# dbo.bridge_transaction_customer

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.bridge_transaction_customer"]
    dbo_stg_canonical_customers(["dbo.stg_canonical_customers"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.stg_canonical_customers |

## View Code

```sql
CREATE   VIEW dbo.bridge_transaction_customer AS SELECT     c.transaction_id,     c.line_id,     CAST(c.customer_no AS bigint)                                  AS customer_no,     CASE c.customer_role         WHEN 1   THEN 'BILL_TO'         WHEN 2   THEN 'SHIP_TO'         WHEN 3   THEN 'MAIL_TO'         WHEN 4   THEN 'LIABILITY'         WHEN 5   THEN 'MISC'         WHEN 200 THEN 'PICKUP'         WHEN 201 THEN 'RAIN_CHECK'         WHEN 202 THEN 'TENDER_VERIFY'         WHEN 203 THEN 'RESTRICTED'         WHEN 204 THEN 'BILL_TO_LEGACY'         ELSE CONCAT('ROLE_', CAST(c.customer_role AS varchar(10)))     END                                                            AS customer_role,     c.customer_role                                                AS customer_role_code,     c.source_system   FROM dbo.stg_canonical_customers AS c  WHERE c.customer_no IS NOT NULL    AND c.customer_no <> ''    AND TRY_CAST(c.customer_no AS bigint) IS NOT NULL;
```

