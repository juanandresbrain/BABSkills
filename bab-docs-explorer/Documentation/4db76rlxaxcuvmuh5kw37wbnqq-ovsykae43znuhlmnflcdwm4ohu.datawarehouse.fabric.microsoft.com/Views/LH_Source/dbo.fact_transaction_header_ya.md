# dbo.fact_transaction_header_ya

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.fact_transaction_header_ya"]
    dbo_stg_deck_transactions_ya(["dbo.stg_deck_transactions_ya"]) --> VIEW
    dbo_stg_jumpmind_transactions_ya(["dbo.stg_jumpmind_transactions_ya"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.stg_deck_transactions_ya |
| dbo.stg_jumpmind_transactions_ya |

## View Code

```sql
CREATE   VIEW dbo.fact_transaction_header_ya AS WITH unified_headers AS (     /* POS side — from stg_jumpmind_transactions_ya (overlay) */     SELECT         t.transaction_id,         t.store_id,         t.store_no,         CAST(t.register_no AS varchar(50))                         AS register_no,         CAST(t.transaction_no AS varchar(50))                      AS transaction_no,         t.transaction_series,         t.transaction_category,         t.entry_date_time,         t.business_date,         t.cashier_no,         t.purchasing_employee_no,         t.transaction_void_flag                                     AS stage_b_void_flag,         t.tax_override_flag,         t.send_tax_exception_jurisdiction,         CAST(t.till_no AS varchar(50))                             AS till_no,         t.closeout_flag,         t.party_id,         t.event_id,         t.event_invoice,         t.gsr_flag,         t.order_status,         t.has_stock_order_line_items,         t.gross_total,         CAST(t.voided_device_id AS varchar(50))                    AS voided_device_id,         CAST(t.voided_sequence_number AS varchar(50))              AS voided_sequence_number,         t.void_enriched_flag,         t.source_system       FROM dbo.stg_jumpmind_transactions_ya AS t      UNION ALL      /* OMS side — from stg_deck_transactions_ya (overlay, iter 9):        strip-leading-1 on store_no, register_no = 2 (web), cashier_no        = legacy store_no (13 / 2013), entry_date_time UTC → CST. */     SELECT         t.transaction_id,         t.store_id,         t.store_no,         CAST(t.register_no AS varchar(50))                         AS register_no,         CAST(t.transaction_no AS varchar(50))                      AS transaction_no,         t.transaction_series,         t.transaction_category,         t.entry_date_time,         t.business_date,         t.cashier_no,         t.purchasing_employee_no,         t.transaction_void_flag                                     AS stage_b_void_flag,         t.tax_override_flag,         t.send_tax_exception_jurisdiction,         CAST(t.till_no AS varchar(50))                             AS till_no,         t.closeout_flag,         t.party_id,         t.event_id,         t.event_invoice,         t.gsr_flag,         t.order_status,         t.has_stock_order_line_items,         CAST(t.oms_order_total AS decimal(18,2))                     AS gross_total,         CAST(NULL AS varchar(20))                                    AS voided_device_id,         CAST(NULL AS bigint)                                         AS voided_sequence_number,         t.void_enriched_flag,         t.source_system       FROM dbo.stg_deck_transactions_ya AS t ), derive_void_flag AS (     SELECT         u.*,         u.stage_b_void_flag                                          AS transaction_void_flag       FROM unified_headers AS u ), derive_date_reject AS (     SELECT         v.*,         CASE             WHEN v.business_date IS NULL                              THEN 1             WHEN v.business_date > GETDATE()                           THEN 1             WHEN v.business_date < DATEADD(year, -7, GETDATE())        THEN 1             ELSE                                                              0         END                                                       AS date_reject_id       FROM derive_void_flag AS v ) SELECT     d.transaction_id,     d.source_system,     d.store_no,     d.register_no,     d.business_date                                     AS transaction_date,     d.date_reject_id,     d.transaction_series,     d.transaction_no,     d.entry_date_time,     d.cashier_no                                        AS cashier_no,     d.transaction_category,     d.transaction_void_flag,     d.tax_override_flag,     d.send_tax_exception_jurisdiction,     d.till_no,     d.closeout_flag,     d.purchasing_employee_no,     d.gross_total                                       AS tender_total,     d.store_id,     d.party_id,     d.event_id,     d.event_invoice,     d.gsr_flag,     d.order_status,     d.has_stock_order_line_items,     d.voided_device_id,     d.voided_sequence_number,     d.void_enriched_flag,     d.stage_b_void_flag   FROM derive_date_reject AS d;
```

