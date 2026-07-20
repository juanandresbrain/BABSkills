# dbo.rpt_receivable_authorizations_vjuan

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.rpt_receivable_authorizations_vjuan"]
    dbo_jumpmind_sls_tender_line_item(["dbo.jumpmind_sls_tender_line_item"]) --> VIEW
    dbo_jumpmind_sls_trans(["dbo.jumpmind_sls_trans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.jumpmind_sls_tender_line_item |
| dbo.jumpmind_sls_trans |

## View Code

```sql
CREATE VIEW dbo.rpt_receivable_authorizations_vjuan AS /*   ROOT CAUSE ANALYSIS (Deep Investigation — May 2026)   =====================================================   The original rpt_receivable_authorizations returns 0 rows because it joins   fact_transaction_line (merchandise-only codes 100-500) filtered on payment   codes 609/630/637/638 — those codes NEVER exist in fact_transaction_line.    This view fixes the join path to use the correct local JumpMind tables:     dbo.jumpmind_sls_trans          — POS transaction headers (local, joins tender)     dbo.jumpmind_sls_tender_line_item — POS payment tender lines (local, same device_ids)    WHY IT STILL RETURNS 0 ROWS FOR Q1 2026:   Receivable tender types (STORE_CREDIT/HOUSE_ORDER=609, BAB_CHARGE=630,   Klarna=637, Global-E=638) do NOT flow through JumpMind POS tender_line_item.   They are recorded directly in SmartLock/AuditWorks from payment processors.   The AuditWorks SQL import (auditworks_transaction_header) stops at 2025-08-19.   Q1 2026 data exists only in SmartLock — not yet loaded into this database.    TO FIX: Extend the SmartLock → SQL import pipeline beyond Aug 2025, OR   load receivable auth data from payment processors (Klarna, Global-E, internal   charge accounts) into a dedicated SQL table joined here. */ WITH tender_mapped AS (     SELECT         tl.device_id,         tl.business_date,         CAST(tl.sequence_number AS varchar(50)) AS sequence_number,         tl.tender_account_number                AS reference_no,         tl.tender_amount,         CASE tl.tender_type_code             WHEN 'STORE_CREDIT' THEN 609             WHEN 'HOUSE_ORDER'  THEN 609             WHEN 'HouseOrder'   THEN 609             WHEN 'Klarna'       THEN 637             WHEN 'KLARNA'       THEN 637             WHEN 'Globale'      THEN 638             WHEN 'GLOBALE'      THEN 638             WHEN 'Amazon'       THEN 631             WHEN 'AMAZON'       THEN 631             WHEN 'PayPal'       THEN 632             WHEN 'PAYPAL'       THEN 632         END AS line_object     FROM dbo.jumpmind_sls_tender_line_item AS tl     WHERE tl.voided = 0       AND tl.tender_type_code IN (             'STORE_CREDIT','HOUSE_ORDER','HouseOrder',             'Klarna','KLARNA','Globale','GLOBALE',             'Amazon','AMAZON','PayPal','PAYPAL'           ) ) SELECT     TRY_CONVERT(int, t.business_unit_id)                                         AS store_no,     TRY_CONVERT(date, t.business_date, 112)                                      AS transaction_date,     TRY_CONVERT(bigint, t.sequence_number)                                       AS transaction_no,     SUBSTRING(t.device_id, CHARINDEX('-', t.device_id) + 1, LEN(t.device_id))  AS register_no,     CAST(NULL AS decimal(18,2))                                                  AS tender_total,     p.reference_no,     SUM(p.tender_amount)                                                         AS [Auth Amount],     p.line_object FROM dbo.jumpmind_sls_trans         AS t JOIN tender_mapped                  AS p     ON  p.device_id       = t.device_id     AND p.business_date   = t.business_date     AND p.sequence_number = t.sequence_number WHERE t.trans_type   IN ('SALE', 'RETURN', 'REDEEM')   AND t.trans_status = 'COMPLETED'   AND p.line_object  IN (609, 630, 631, 637, 638) GROUP BY     t.business_unit_id, t.business_date, t.sequence_number,     t.device_id, p.reference_no, p.line_object;
```

