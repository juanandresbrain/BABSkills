# dbo.spSoxBalance

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSoxBalance"]
    dbo_GiftCardBalance(["dbo.GiftCardBalance"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GiftCardBalance |

## Stored Procedure Code

```sql
CREATE PROCEDURE [spSoxBalance]
@Fiscal_Year int,
@AuditQuarter int,
@AuditQuarterKey int
AS

-- =============================================================================================================
-- Name: [DOMO].[spSoxBalance]
--
-- Description: Sox StagingGiftCard Balance Reporting to DOMO.
-- 
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Brian Byas			9/8/2016		Initial creation
-- =============================================================================================================




WITH SOXBalance (Fiscal_Year,AuditQuarter,ActivationMid,NumCards,OutstandingBalance) AS (
		
		/*
		-- Sox Staging GiftCard Balance Reporting
		*/
	
	
		SELECT
		@Fiscal_year AS Fiscal_Year,
		@AuditQuarter AS AuditQuarter,				
		ActivationMid,	
		COUNT(*) AS NumCards,	
		SUM(OutstandingBalance) AS OutstandingBalance	
	FROM		
		SOX.dbo.GiftCardBalance WITH (NOLOCK)	
	WHERE AuditQuarterKey=@AuditQuarterKey		
	GROUP BY ActivationMid		

		)


		SELECT * FROM SOXBalance
		ORDER BY ActivationMid
```

