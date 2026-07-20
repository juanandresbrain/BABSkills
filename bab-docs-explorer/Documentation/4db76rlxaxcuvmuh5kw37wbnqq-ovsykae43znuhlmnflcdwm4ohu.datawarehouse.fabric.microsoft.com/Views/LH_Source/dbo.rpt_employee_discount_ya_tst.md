# dbo.rpt_employee_discount_ya_tst

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.rpt_employee_discount_ya_tst"]
    dbo_jumpmind_sls_retail_line_item_price_mod(["dbo.jumpmind_sls_retail_line_item_price_mod"]) --> VIEW
    dbo_jumpmind_sls_retail_trans(["dbo.jumpmind_sls_retail_trans"]) --> VIEW
    dbo_jumpmind_sls_trans(["dbo.jumpmind_sls_trans"]) --> VIEW
    dbo_mulesoft_dynamicsheader(["dbo.mulesoft_dynamicsheader"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.jumpmind_sls_retail_line_item_price_mod |
| dbo.jumpmind_sls_retail_trans |
| dbo.jumpmind_sls_trans |
| dbo.mulesoft_dynamicsheader |

## View Code

```sql
CREATE   VIEW dbo.rpt_employee_discount_ya_tst AS WITH pos_rows AS (     SELECT         /* country derived from iso_currency_code (USD/CAD/GBP/EUR) */         CASE st.iso_currency_code             WHEN 'USD' THEN 'US'             WHEN 'CAD' THEN 'CA'             WHEN 'GBP' THEN 'UK'             WHEN 'EUR' THEN 'IE'             ELSE NULL         END                                                           AS country,         /* store_id: BBW-padded form (4-digit NA = 1001-1999, UK/CA/IE = 2000+) */         TRY_CONVERT(int, LTRIM(RTRIM(t.business_unit_id)))            AS store_id,         /* actual_date: see column-derivation note R-IE/UK in header */         COALESCE(             CAST(st.last_update_time AS date),             TRY_CONVERT(date, st.business_date, 112)         )                                                              AS actual_date,         CAST(st.sequence_number AS bigint)                            AS transaction_no,         /* register_no: see column-derivation note in header */         TRY_CONVERT(int,             CASE                 WHEN LEN(RIGHT(st.device_id, 3)) = 3                   AND LEFT(RIGHT(st.device_id, 3), 1) = '1'                     THEN SUBSTRING(RIGHT(st.device_id, 3), 2, 2)                 ELSE RIGHT(st.device_id, 3)             END         )                                                             AS register_no,         /* unit_gross_amount: emitted as negative (consumer sign convention) */         SUM(-1 * CAST(pm.modification_total AS decimal(18,2)))        AS unit_gross_amount,         MAX(CAST(pm.promotion_type AS varchar(64)))                   AS promotion_type,         /* promotion_name: country prefix + price_mod.description */         MAX(           CASE st.iso_currency_code             WHEN 'USD' THEN 'US'             WHEN 'CAD' THEN 'CA'             WHEN 'GBP' THEN 'UK'             WHEN 'EUR' THEN 'IE'             ELSE NULL           END           + ' - ' + CAST(pm.description AS varchar(256))         )                                                             AS promotion_name,         CAST(pm.promotion_id AS varchar(64))                          AS reference_no,         /* transaction_id from Dynamics header (already INNER-joined below) */         TRY_CONVERT(bigint, MAX(CAST(dh.RetailTransactionId AS varchar(64)))) AS transaction_id,         /* OrderNumber NULL for POS rows */         CAST(NULL AS varchar(64))                                     AS OrderNumber       FROM LH_Source.dbo.jumpmind_sls_retail_trans               st       JOIN LH_Source.dbo.jumpmind_sls_retail_line_item_price_mod pm             ON st.device_id       = pm.device_id            AND st.business_date   = pm.business_date            AND st.sequence_number = pm.sequence_number       JOIN LH_Source.dbo.jumpmind_sls_trans                       t             ON st.device_id       = t.device_id            AND st.business_date   = t.business_date            AND st.sequence_number = t.sequence_number       /* INNER (not LEFT) join — R3 requires merchandise discount > 0 */       JOIN LH_Source.dbo.mulesoft_dynamicsheader                  dh             ON dh.TransactionKey = CONCAT(t.device_id, '-', t.business_date, '-', t.sequence_number)      WHERE pm.promotion_type = 'EMPLOYEE_DISCOUNT'                -- R1        AND ISNULL(pm.voided, 0) = 0        AND ISNULL(t.training_mode, 0) = 0                         -- R5        AND UPPER(t.trans_status) = 'COMPLETED'                    -- R5        AND st.employee_id_for_discount IS NOT NULL                -- R6        AND pm.promotion_id IN (                                   -- R2 (Marketing-curated)             'PRM0c8Pb00000000a8IAA',   /* CA - 30% Off Purchase - Employee Discount */             'PRM0c8Pb00000000aNIAQ',   /* UK - 30% Off Purchase - Employee Discount */             'PRM0c8Pb000000015lIAA',   /* IE - 30% Off Purchase - Employee Discount */             'PRM0c8Pb0000000hL7IAI',   /* US - April spring campaign 1 */             'PRM0c8Pb0000000hJVIAY',   /* US - April spring campaign 2 */             'PRM0c8Pb0000000hD3IAI'    /* US - April spring campaign 3 */        )        AND dh.TotalDiscAmount > 0                                 -- R3        AND ISNULL(st.total, 0) > 0                                -- R4      /* GROUP BY pm.promotion_id — one row per (transaction, promotion). */      GROUP BY         st.iso_currency_code,         t.business_unit_id,         st.business_date,         st.sequence_number,         st.device_id,         pm.promotion_id,         CAST(st.last_update_time AS date) ) SELECT * FROM pos_rows;
```

