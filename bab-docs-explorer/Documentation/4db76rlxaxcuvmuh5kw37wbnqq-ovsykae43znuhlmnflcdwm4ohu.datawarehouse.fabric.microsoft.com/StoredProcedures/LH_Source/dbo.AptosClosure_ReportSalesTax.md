# dbo.AptosClosure_ReportSalesTax

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_ReportSalesTax"]
    dbo_v_sales_tax_core(["dbo.v_sales_tax_core"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.v_sales_tax_core |

## Stored Procedure Code

```sql
CREATE   PROCEDURE dbo.AptosClosure_ReportSalesTax    @startDate        DATE,    @endDate          DATE,    @businessUnitIDs  VARCHAR(MAX),    @delimiter        CHAR(1),    @eurExchangeRate  DECIMAL(12, 6) AS BEGIN     SET NOCOUNT ON;      -- Business unit list via CTE (no temp tables / constraints)     WITH bu AS (         SELECT LTRIM(value) AS business_unit_id         FROM STRING_SPLIT(@businessUnitIDs, @delimiter)     )     SELECT         st.business_unit_id,         st.business_date,         st.sequence_number,         st.device_id,         st.item_id,         st.item_description,         CASE             WHEN st.country_id = 'IE' THEN @eurExchangeRate * st.money_tax_amount             ELSE st.money_tax_amount         END AS money_tax_amount     FROM dbo.v_sales_tax_core AS st     INNER JOIN bu         ON st.business_unit_id = bu.business_unit_id     WHERE         -- Sargable date range (no CAST on column; allows segment pruning)         st.create_time >= @startDate         AND st.create_time < DATEADD(day, 1, @endDate); END
```

