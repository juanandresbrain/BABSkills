# dbo.stg_paypal_tf_keyed

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.stg_paypal_tf_keyed"]
    dbo_transaction_facts(["dbo.transaction_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_facts |

## View Code

```sql
CREATE   VIEW dbo.stg_paypal_tf_keyed AS SELECT     tf.transaction_id,     tf.webOrderNumber,     LEFT(tf.webOrderNumber,          LEN(tf.webOrderNumber)          - CHARINDEX('_', REVERSE(tf.webOrderNumber))) AS oms_order_number   FROM LH_Mart.dbo.transaction_facts AS tf  WHERE tf.webOrderNumber IS NOT NULL    AND tf.webOrderNumber <> ''    AND tf.webOrderNumber LIKE '%[_]%';
```

