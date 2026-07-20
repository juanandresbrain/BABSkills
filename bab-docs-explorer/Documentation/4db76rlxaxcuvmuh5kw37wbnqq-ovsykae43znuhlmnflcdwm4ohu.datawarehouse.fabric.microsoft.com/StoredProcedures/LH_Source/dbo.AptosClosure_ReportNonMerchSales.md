# dbo.AptosClosure_ReportNonMerchSales

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_ReportNonMerchSales"]
    dbo_v_nonmerch_sales_core(["dbo.v_nonmerch_sales_core"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.v_nonmerch_sales_core |

## Stored Procedure Code

```sql
CREATE   PROCEDURE dbo.AptosClosure_ReportNonMerchSales    @startDate        DATE,    @endDate          DATE,    @businessUnitIDs  VARCHAR(MAX),    @delimiter        CHAR(1),    @eurExchangeRate  DECIMAL(12, 6) AS BEGIN     SET NOCOUNT ON;      -- Business unit list via CTE (no temp tables or constraints)     WITH bu AS (         SELECT LTRIM(value) AS business_unit_id         FROM STRING_SPLIT(@businessUnitIDs, @delimiter)     )     SELECT         ms.business_unit_id,         ms.business_date,         ms.sequence_number,         ms.device_id,         ms.item_description,          -- Final item_id after card-number mapping         ci.computed_item_id AS item_id,          -- Final item_type after special handling for '098088'         CASE             WHEN (ms.business_unit_id IN ('1031','1047','1088','1100','1207','1210','1216','1309','1332','1363','1384','1417','1476')                   AND ci.computed_item_id = '098088')               THEN 'SALES_TAX'             WHEN ci.computed_item_id = '098088'               THEN 'SALES_SUPPLY'             ELSE ms.item_type         END AS item_type,          -- Extended amount after per-country tax/FX rules         CASE             WHEN ms.country_id = 'UK'               THEN ms.extended_amount - ms.tax_amount             WHEN ms.country_id = 'IE'               THEN ROUND(@eurExchangeRate * ms.extended_amount, 4)                  - ROUND(@eurExchangeRate * ms.tax_amount,   4)             ELSE               ms.extended_amount         END AS extended_amount     FROM dbo.v_nonmerch_sales_core AS ms     INNER JOIN bu         ON ms.business_unit_id = bu.business_unit_id      -- Compute remapped item_id once, reuse in SELECT above     CROSS APPLY (         SELECT CASE             WHEN CAST(LEFT(ISNULL(ms.card_number, '0'), 12) AS BIGINT) BETWEEN 634431830110 AND 634431863609               THEN '034524'             WHEN CAST(LEFT(ISNULL(ms.card_number, '0'), 12) AS BIGINT) BETWEEN 634431863610 AND 634431872109               THEN '034524'             ELSE ms.item_id         END AS computed_item_id     ) AS ci      WHERE         -- Sargable date range (no CAST on ms.create_time)         ms.create_time >= @startDate         AND ms.create_time < DATEADD(day, 1, @endDate); END
```

