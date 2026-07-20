# dbo.AptosClosure_ReportNonMerchDiscounts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_ReportNonMerchDiscounts"]
    dbo_v_nonmerch_discounts_core(["dbo.v_nonmerch_discounts_core"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.v_nonmerch_discounts_core |

## Stored Procedure Code

```sql
CREATE   PROCEDURE dbo.AptosClosure_ReportNonMerchDiscounts    @startDate        DATE,    @endDate          DATE,    @businessUnitIDs  VARCHAR(MAX),    @delimiter        CHAR(1),    @eurExchangeRate  DECIMAL(12, 6) AS BEGIN     SET NOCOUNT ON;      -- Business unit list via CTE (no temp tables, no constraints)     WITH bu AS (         SELECT LTRIM(value) AS business_unit_id         FROM STRING_SPLIT(@businessUnitIDs, @delimiter)     )     SELECT         nd.business_unit_id,         nd.business_date,         nd.sequence_number,         nd.description,         CASE             WHEN nd.country_id = 'IE' THEN @eurExchangeRate * nd.modification_total             ELSE nd.modification_total         END AS modification_total,         nd.item_type     FROM dbo.v_nonmerch_discounts_core AS nd     INNER JOIN bu         ON nd.business_unit_id = bu.business_unit_id     WHERE         -- Sargable date range (no CAST on column)         nd.create_time >= @startDate         AND nd.create_time < DATEADD(day, 1, @endDate); END
```

