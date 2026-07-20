# dbo.AptosClosure_GetJMTransCounts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetJMTransCounts"]
    jumpmind_sls_trans_summary(["jumpmind_sls_trans_summary"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| jumpmind_sls_trans_summary |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2025-11-04 -- Description: Returns transaction counts by category from Aptos -- =============================================  CREATE PROCEDURE AptosClosure_GetJMTransCounts     @BusinessUnitIds NVARCHAR(MAX), -- comma-separated list of IDs     @StartDate DATE,     @EndDate DATE AS BEGIN     SET NOCOUNT ON;      -- Split the comma-separated string into a table of INTs     ;WITH BusinessUnitList AS (         SELECT TRY_CAST(TRIM(value) AS INT) AS business_unit_id         FROM STRING_SPLIT(@BusinessUnitIds, ',')         WHERE TRY_CAST(TRIM(value) AS INT) IS NOT NULL     ),     Base AS (         SELECT               s.business_unit_id,             s.business_date,             s.device_id,             s.sequence_number,             s.trans_type_code,             CASE                 WHEN s.trans_type_code IN ('PAY_IN','PAY_OUT') THEN 'SALE'                 ELSE s.trans_type_code             END AS trans_typeMapped,             CASE                  WHEN s.trans_type_code IN ('PAY_IN','PAY_OUT','SALE') THEN 'SALE'                 ELSE 'CONTROL'             END AS TransCategory         FROM jumpmind_sls_trans_summary s         INNER JOIN BusinessUnitList b ON s.business_unit_id = b.business_unit_id         WHERE TRY_CONVERT(DATE, s.business_date) BETWEEN @StartDate AND @EndDate     )     SELECT 'Total' AS [Type], COUNT(*) AS [TransCount]     FROM Base     UNION     SELECT 'Sales' AS [Type], COUNT(*) AS [TransCount]     FROM Base      WHERE TransCategory = 'SALE'     UNION     SELECT 'Control' AS [Type], COUNT(*) AS [TransCount]     FROM Base      WHERE TransCategory = 'CONTROL' END
```

