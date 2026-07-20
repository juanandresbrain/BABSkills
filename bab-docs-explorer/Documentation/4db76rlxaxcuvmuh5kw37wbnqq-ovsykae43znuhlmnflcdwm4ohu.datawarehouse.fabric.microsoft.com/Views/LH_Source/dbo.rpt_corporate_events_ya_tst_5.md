# dbo.rpt_corporate_events_ya_tst_5

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.rpt_corporate_events_ya_tst_5"]
    dbo_dim_store(["dbo.dim_store"]) --> VIEW
    dbo_jumpmind_sls_retail_trans(["dbo.jumpmind_sls_retail_trans"]) --> VIEW
    dbo_jumpmind_sls_tax_retail_line_item(["dbo.jumpmind_sls_tax_retail_line_item"]) --> VIEW
    dbo_jumpmind_sls_trans(["dbo.jumpmind_sls_trans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dim_store |
| dbo.jumpmind_sls_retail_trans |
| dbo.jumpmind_sls_tax_retail_line_item |
| dbo.jumpmind_sls_trans |

## View Code

```sql
CREATE   VIEW dbo.rpt_corporate_events_ya_tst_5 AS WITH ds_dedup AS (     SELECT business_unit_id,            store_name,            country_code       FROM (           SELECT business_unit_id,                  store_name,                  country_code,                  ROW_NUMBER() OVER (                      PARTITION BY business_unit_id                      ORDER BY store_id                  ) AS rn             FROM dbo.dim_store       ) x      WHERE rn = 1 ), tax_per_txn AS (     SELECT device_id,            business_date,            sequence_number,            rule_name,            tax_percentage,            SUM(tax_amount) AS tax_amount_sum       FROM LH_Source.dbo.jumpmind_sls_tax_retail_line_item      WHERE voided = 0      GROUP BY device_id,               business_date,               sequence_number,               rule_name,               tax_percentage ), tax_pick AS (     SELECT device_id,            business_date,            sequence_number,            rule_name,            tax_amount_sum,            tax_percentage       FROM (           SELECT device_id,                  business_date,                  sequence_number,                  rule_name,                  tax_amount_sum,                  tax_percentage,                  ROW_NUMBER() OVER (                      PARTITION BY device_id, business_date, sequence_number                      ORDER BY tax_amount_sum DESC,                               tax_percentage  DESC,                               rule_name       ASC                  ) AS rn             FROM tax_per_txn       ) y      WHERE rn = 1 ) SELECT     CONCAT(         rt.device_id, '-',         rt.business_date, '-',         CAST(rt.sequence_number AS varchar(20))     )                                              AS [TransactionKey],     TRY_CAST(SUBSTRING(rt.device_id, 1,              CHARINDEX('-', rt.device_id) - 1) AS int) AS [Store Number],     ds.store_name                                  AS [StoreName],     CONVERT(date, rt.business_date, 112)           AS [Transaction Date],     TRY_CAST(rt.business_date AS int)              AS [PosBusiness Date],     rt.event_id                                    AS [EventId],     rt.subtotal                                    AS [Sales Before SalesTax],     rt.tax_total                                   AS [Total SalesTax],     rt.total                                       AS [TotalSales Include SalesTax],     CAST(0 AS decimal(18,2))                       AS [Amount Already Paid],     rt.total                                       AS [Amount Owed],     tp.rule_name                                   AS [TaxName],     CASE         WHEN tp.tax_percentage IS NULL THEN NULL         ELSE CAST(rt.subtotal * tp.tax_percentage / 100.0 AS decimal(18,2))     END                                            AS [SalesTaxAmount],     tp.tax_percentage                              AS [SalesTax Percentage] FROM LH_Source.dbo.jumpmind_sls_retail_trans AS rt INNER JOIN LH_Source.dbo.jumpmind_sls_trans  AS t        ON  rt.device_id       = t.device_id        AND rt.business_date   = t.business_date        AND rt.sequence_number = t.sequence_number INNER JOIN ds_dedup                AS ds        ON  ds.business_unit_id =            SUBSTRING(rt.device_id, 1, CHARINDEX('-', rt.device_id) - 1) LEFT  JOIN tax_pick                AS tp        ON  tp.device_id       = rt.device_id        AND tp.business_date   = rt.business_date        AND tp.sequence_number = rt.sequence_number WHERE rt.event_id IS NOT NULL   AND rt.event_id NOT IN ('', '0')   AND t.trans_status       = 'COMPLETED'   AND rt.tender_type_codes = 'EVENT_INVOICE'   AND ds.country_code      = 'US';
```

