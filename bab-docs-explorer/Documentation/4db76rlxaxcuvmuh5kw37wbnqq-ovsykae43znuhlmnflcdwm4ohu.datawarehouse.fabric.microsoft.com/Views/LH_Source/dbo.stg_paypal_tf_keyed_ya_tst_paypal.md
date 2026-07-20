# dbo.stg_paypal_tf_keyed_ya_tst_paypal

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.stg_paypal_tf_keyed_ya_tst_paypal"]
    dbo_transaction_facts(["dbo.transaction_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_facts |

## View Code

```sql
/* =============================================================================    stg_paypal_tf_keyed.sql, transaction_facts -> OMS order number bridge    =============================================================================    Domain:   Reconciliation (Sales Audit)    Audience: rpt_sp_paypal_auth     PURPOSE      Parse LH_Mart.transaction_facts.webOrderNumber into a clean OMS      OrderNumber column ONCE, restricted to rows that actually carry an      OMS-allocated webOrderNumber. The downstream report then joins on      transaction_id with no per-row string manipulation.       The pre-fix inline CTE (paypal_oms_keyed) scanned every row of      LH_Mart.transaction_facts and applied          LEFT(webOrderNumber,               LEN(webOrderNumber) - CHARINDEX('_', REVERSE(webOrderNumber)))      on the per-row column. REVERSE() + CHARINDEX() are not pushdownable      in Fabric Warehouse; combined with the rest of the report's join shape      this produced Msg 65001 (non-scalable operation) on prod 2026-05-21.       This staged view performs the same parse but restricts to rows where      webOrderNumber LIKE '%[_]%', narrowing the working set by roughly two      orders of magnitude before the string ops fire.     SHAPE        transaction_id     bigint     LH_Mart.transaction_facts.transaction_id                                      (join key for the downstream report).        webOrderNumber     varchar    Raw column, kept for debug / traceability.        oms_order_number   varchar    webOrderNumber with the trailing '_N'                                      AW allocation suffix stripped, e.g.:                                          'W9376532_1' -> 'W9376532'                                          'W9336503_2' -> 'W9336503'                                          'W9336503_3' -> 'W9336503'     ROW SCOPE      Only rows where webOrderNumber matches '%[_]%' (contains an underscore).      Empirically that filters down to the OMS-origin subset that has a      parseable '_N' allocation suffix; every PayPal-tendered transaction      of interest sits inside this subset.     NOTE FOR FUTURE WRITERS      If the underlying mirror gains an `oms_order_number` column on      transaction_facts directly, retire this view and switch the report      to read that column. The parse here is correct but it is a parse, not      authoritative; an upstream column would be preferable.    ============================================================================= */  CREATE   VIEW dbo.stg_paypal_tf_keyed_ya_tst_paypal AS SELECT     tf.transaction_id,     tf.webOrderNumber,     LEFT(tf.webOrderNumber,          LEN(tf.webOrderNumber)          - CHARINDEX('_', REVERSE(tf.webOrderNumber))) AS oms_order_number   FROM LH_Mart.dbo.transaction_facts AS tf  WHERE tf.webOrderNumber IS NOT NULL    AND tf.webOrderNumber <> ''    AND tf.webOrderNumber LIKE '%[_]%';
```

