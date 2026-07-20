# dbo.AptosClosure_GetAllJMTransCounts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetAllJMTransCounts"]
    dbo_jumpmind_sls_trans_summary(["dbo.jumpmind_sls_trans_summary"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.jumpmind_sls_trans_summary |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2025-11-04 -- Description: Returns transaction counts by category from Aptos -- Notes: --   - PAY_IN and PAY_OUT are counted under SALE --   - CONTROL is everything else -- =============================================  CREATE   PROCEDURE [dbo].[AptosClosure_GetAllJMTransCounts]     @StartDate DATE,     @EndDate   DATE AS BEGIN     SET NOCOUNT ON;      /* Basic parameter validation */     IF @StartDate IS NULL OR @EndDate IS NULL     BEGIN         RAISERROR('StartDate and EndDate are required.', 16, 1);         RETURN;     END;      IF @StartDate > @EndDate     BEGIN         RAISERROR('StartDate must be less than or equal to EndDate.', 16, 1);         RETURN;     END;      ;WITH Base AS     (         SELECT             s.business_unit_id,             s.business_date,             s.device_id,             s.sequence_number,             s.trans_type_code,             CASE                 WHEN s.trans_type_code IN ('PAY_IN','PAY_OUT') THEN 'SALE'                 ELSE s.trans_type_code             END AS trans_typeMapped,             CASE                 WHEN s.trans_type_code IN ('PAY_IN','PAY_OUT','SALE') THEN 'SALE'                 ELSE 'CONTROL'             END AS TransCategory         FROM dbo.jumpmind_sls_trans_summary AS s         -- If business_date is already DATE, TRY_CONVERT is harmless; if it's NVARCHAR, this safely filters invalids out         WHERE TRY_CONVERT(DATE, s.business_date) BETWEEN @StartDate AND @EndDate     )     SELECT [Type], [TransCount]     FROM     (         SELECT 'Total'   AS [Type], COUNT(*) AS [TransCount] FROM Base         UNION ALL         SELECT 'Sales'   AS [Type], COUNT(*) AS [TransCount] FROM Base WHERE TransCategory = 'SALE'         UNION ALL         SELECT 'Control' AS [Type], COUNT(*) AS [TransCount] FROM Base WHERE TransCategory = 'CONTROL'     ) x     ORDER BY CASE x.[Type]                  WHEN 'Total'   THEN 1                  WHEN 'Sales'   THEN 2                  WHEN 'Control' THEN 3                  ELSE 99              END; END
```

