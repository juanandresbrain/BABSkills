# dbo.AptosClosure_ReportMerchDiscounts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_ReportMerchDiscounts"]
    dbo_v_merch_discounts_core(["dbo.v_merch_discounts_core"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.v_merch_discounts_core |

## Stored Procedure Code

```sql
CREATE   PROCEDURE dbo.AptosClosure_ReportMerchDiscounts    @startDate        DATE,    @endDate          DATE,    @businessUnitIDs  VARCHAR(MAX),    @delimiter        CHAR(1),    @eurExchangeRate  DECIMAL(12, 6) AS BEGIN     SET NOCOUNT ON;      -- Build BU list as a CTE – no CREATE/DECLARE table, no constraints     WITH bu AS (         SELECT LTRIM(value) AS business_unit_id         FROM STRING_SPLIT(@businessUnitIDs, @delimiter)     )     SELECT         md.business_unit_id,         md.business_date,         md.sequence_number,         md.description,         CASE             WHEN md.country_id = 'IE' THEN @eurExchangeRate * md.modification_total             ELSE md.modification_total         END AS modification_total     FROM dbo.v_merch_discounts_core AS md     INNER JOIN bu         ON md.business_unit_id = bu.business_unit_id     WHERE         md.create_time >= @startDate         AND md.create_time < DATEADD(day, 1, @endDate); END
```

