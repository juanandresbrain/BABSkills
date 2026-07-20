# dbo.AptosClosure_ReportPayInOut

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_ReportPayInOut"]
    dbo_v_payinout_core(["dbo.v_payinout_core"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.v_payinout_core |

## Stored Procedure Code

```sql
CREATE   PROCEDURE dbo.AptosClosure_ReportPayInOut    @startDate        DATE,    @endDate          DATE,    @businessUnitIDs  VARCHAR(MAX),    @delimiter        CHAR(1),    @eurExchangeRate  DECIMAL(12, 6) AS BEGIN     SET NOCOUNT ON;      -- Business unit list via CTE (no temp tables / constraints)     WITH bu AS (         SELECT LTRIM(value) AS business_unit_id         FROM STRING_SPLIT(@businessUnitIDs, @delimiter)     )     SELECT         p.business_unit_id,         p.business_date,         p.sequence_number,         p.device_id,         p.reason_code,         CASE             WHEN p.country_id = 'IE' THEN @eurExchangeRate * p.tender_amount             ELSE p.tender_amount         END AS tender_amount     FROM dbo.v_payinout_core AS p     INNER JOIN bu         ON p.business_unit_id = bu.business_unit_id     WHERE         -- Sargable date range (no CAST on column; enables segment pruning)         p.create_time >= @startDate         AND p.create_time < DATEADD(day, 1, @endDate); END
```

