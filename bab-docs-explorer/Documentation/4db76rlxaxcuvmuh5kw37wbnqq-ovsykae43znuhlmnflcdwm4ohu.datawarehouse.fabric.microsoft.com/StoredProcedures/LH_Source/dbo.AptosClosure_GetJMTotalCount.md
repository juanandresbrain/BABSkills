# dbo.AptosClosure_GetJMTotalCount

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetJMTotalCount"]
    dbo_jumpmind_sls_trans_summary(["dbo.jumpmind_sls_trans_summary"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.jumpmind_sls_trans_summary |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2026-01-20 -- Description: Returns total count of JumpMind transactions between dates -- Notes: --   - Counts rows from dbo.jumpmind_sls_trans_summary --   - Uses TRY_CONVERT on business_date to be resilient to string/date storage -- =============================================  CREATE PROCEDURE [dbo].[AptosClosure_GetJMTotalCount]     @StartDate DATE,     @EndDate   DATE AS BEGIN     SET NOCOUNT ON;      IF @StartDate IS NULL OR @EndDate IS NULL     BEGIN         RAISERROR('StartDate and EndDate are required.', 16, 1);         RETURN;     END;      IF @StartDate > @EndDate     BEGIN         RAISERROR('StartDate must be less than or equal to EndDate.', 16, 1);         RETURN;     END;      /* Safely convert YYYYMMDD → date */     ;WITH Converted AS     (         SELECT              TRY_CONVERT(date,                 STUFF(STUFF(RTRIM(business_date),5,0,'-'),8,0,'-')             ) AS BusinessDateFixed         FROM dbo.jumpmind_sls_trans_summary     )     SELECT COUNT_BIG(*) AS TotalCount     FROM Converted     WHERE BusinessDateFixed BETWEEN @StartDate AND @EndDate; END
```

