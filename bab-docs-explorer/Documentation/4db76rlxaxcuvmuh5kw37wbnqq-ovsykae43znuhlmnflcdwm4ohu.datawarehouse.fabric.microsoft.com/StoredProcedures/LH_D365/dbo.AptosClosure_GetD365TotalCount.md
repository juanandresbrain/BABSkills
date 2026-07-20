# dbo.AptosClosure_GetD365TotalCount

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetD365TotalCount"]
    dbo_retailtransactiontable(["dbo.retailtransactiontable"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.retailtransactiontable |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2026-01-20 -- Description: Returns total count of D365 POS transactions between dates -- Notes: --   - Counts rows from dbo.RetailTransactionTable (header-level POS transactions) --   - Uses BusinessDate when present; falls back to TransactionDate --   - If your env always uses BusinessDate, you can simplify the COALESCE -- ============================================= CREATE   PROCEDURE [dbo].[AptosClosure_GetD365TotalCount]     @StartDate DATE,     @EndDate   DATE AS BEGIN     SET NOCOUNT ON;      /* Basic parameter validation */     IF @StartDate IS NULL OR @EndDate IS NULL     BEGIN         RAISERROR('StartDate and EndDate are required.', 16, 1);         RETURN;     END;      IF @StartDate > @EndDate     BEGIN         RAISERROR('StartDate must be less than or equal to EndDate.', 16, 1);         RETURN;     END;      /* Normalize date (some AXDBs carry 0001-01-01 for not-set BusinessDate) */     SELECT COUNT_BIG(*) AS TotalCount     FROM dbo.retailtransactiontable      WHERE CAST(             COALESCE(                 NULLIF(businessdate, '0001-01-01'),                 transdate             ) AS date           ) BETWEEN @StartDate AND @EndDate; END
```

