# DOMO.spSoxGCFinalBalance

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["DOMO.spSoxGCFinalBalance"]
    dbo_FinalBalance(["dbo.FinalBalance"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FinalBalance |

## Stored Procedure Code

```sql
CREATE PROCEDURE [DOMO].[spSoxGCFinalBalance]
@Fiscal_Year int,
@AuditQuarter int

AS

-- =============================================================================================================
-- Name: [DOMO].[spSoxGCFinalBalance]
--
-- Description: Sox GiftCard Balance Reporting to DOMO.
-- 
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Brian Byas			9/8/2016		Initial creation
-- =============================================================================================================




WITH FinalBalance (Fiscal_Year,AuditQuarter,MID,NumCards,Balance,discountBalance) AS (
		
		/*
		-- Sox GiftCard Balance Reporting
		*/

		SELECT
			@Fiscal_year AS Fiscal_Year,
			@AuditQuarter AS AuditQuarter,			
			b.MID,		
			COUNT(*) AS numCards,		
			SUM(b.balance) AS balance,		
			SUM(b.activation_discount_balance) AS discountBalance		
		FROM			
			SOX.dbo.FinalBalance b WITH (NOLOCK)	
		GROUP BY b.MID			
	

		)


		SELECT * FROM FinalBalance
		ORDER BY MID
```

