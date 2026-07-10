# Azure.vwMerchandisingFacts

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwMerchandisingFacts"]
    DOMO_MerchandisingFacts(["DOMO.MerchandisingFacts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| DOMO.MerchandisingFacts |

## View Code

```sql
Create view [Azure].[vwMerchandisingFacts]

AS
-- =============================================================================================================
-- Name: [Azure].[vwMerchandisingFacts]
--
-- Description: This view is filtered to only show current and two previous fiscal years it is used to limit the data that shows up in Power BI views.
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		John Eck			8/9/2018		Initial creation
--
-- =============================================================================================================

SELECT [ProductStoreDateKey]      ,[ProductKey]
      ,[StoreKey]
      ,[DateKey]      ,[ActualDate]      ,[PermRetailTe]
      ,[PromoPcTotalRetailTe]      ,[ReceivedUnits]
      ,[ReceivedRetailTe]      ,[ReceivedCost]
      ,[NetSalesUnits]      ,[NetSalesRetailTe]
      ,[NetSalesRetailNativeTe]      ,[NetSalesCost]
      ,[ShrinkActualUnits]      ,[ShrinkActualRetailTe]
      ,[OnOrderUnits]      ,[OnOrderRetailTe]
      ,[OnOrderCost]      ,[OnHandUnits]
      ,[OnHandRetailTe]      ,[OnHandCost]
      ,[INS_DT]      ,[UPDT_DT]
  FROM [dw].[DOMO].[MerchandisingFacts]
  where dateKey >= 7330
```

