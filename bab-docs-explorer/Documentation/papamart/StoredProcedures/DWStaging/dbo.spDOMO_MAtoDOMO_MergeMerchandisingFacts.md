# dbo.spDOMO_MAtoDOMO_MergeMerchandisingFacts

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDOMO_MAtoDOMO_MergeMerchandisingFacts"]
    dbo_DOMO_MA_MerchandisingFactsStage(["dbo.DOMO_MA_MerchandisingFactsStage"]) --> SP
    DOMO_MerchandisingFacts(["DOMO.MerchandisingFacts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DOMO_MA_MerchandisingFactsStage |
| DOMO.MerchandisingFacts |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spDOMO_MAtoDOMO_MergeMerchandisingFacts]

as

-- =====================================================================================================
-- Name: spDOMO_MAtoDOMO_MergeMerchandisingFacts
--
-- Description:	Merges from dwstaging.dbo.DOMO_MA_MerchandisingFactsStage to DW.dbo.MerchandisingFacts
--				
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		08/29/2016		Created proc
-- =====================================================================================================

set nocount on

MERGE into dw.DOMO.MerchandisingFacts as target
USING 
	(
		SELECT 
			ProductStoreDateKey, 
			ProductKey,
			StoreKey,
			DateKey,
			ActualDate,
			PermRetailTe,
			PromoPcTotalRetailTe,
			ReceivedUnits,
			ReceivedRetailTe,
			ReceivedCost,
			NetSalesUnits,
			NetSalesRetailTe,
			NetSalesRetailNativeTe,
			NetSalesCost,
			ShrinkActualUnits,
			ShrinkActualRetailTe,
			OnOrderUnits,
			OnOrderRetailTe,
			OnOrderCost,
			OnHandUnits,
			OnHandRetailTe,
			OnHandCost
		from dwstaging.dbo.DOMO_MA_MerchandisingFactsStage 
	) as source
ON
	(
		target.ProductStoreDateKey = source.ProductStoreDateKey
	)
when matched
	and
		(
			target.PermRetailTe <> source.PermRetailTe OR
			target.PromoPcTotalRetailTe <> source.PromoPcTotalRetailTe OR
			target.ReceivedUnits <> source.ReceivedUnits OR
			target.ReceivedRetailTe <> source.ReceivedRetailTe OR
			target.ReceivedCost <> source.ReceivedCost OR 
			target.NetSalesUnits <> source.NetSalesUnits OR
			target.NetSalesRetailTe <> source.NetSalesRetailTe OR
			target.NetSalesRetailNativeTe <> source.NetSalesRetailNativeTe OR
			target.NetSalesCost <> source.NetSalesCost OR
			target.ShrinkActualUnits <> source.ShrinkActualUnits OR
			target.ShrinkActualRetailTe <> source.ShrinkActualRetailTe OR
			target.OnOrderUnits <> source.OnOrderUnits OR
			target.OnOrderRetailTe <> source.OnOrderRetailTe OR
			target.OnOrderCost <> source.OnOrderCost OR
			target.OnHandUnits <> source.OnHandUnits OR
			target.OnHandRetailTe <> source.OnHandRetailTe OR
			target.OnHandCost <> source.OnHandCost	
					)
THEN UPDATE 
	SET
			target.PermRetailTe = source.PermRetailTe,
			target.PromoPcTotalRetailTe = source.PromoPcTotalRetailTe,
			target.ReceivedUnits = source.ReceivedUnits,
			target.ReceivedRetailTe = source.ReceivedRetailTe,
			target.ReceivedCost = source.ReceivedCost,
			target.NetSalesUnits = source.NetSalesUnits,
			target.NetSalesRetailTe = source.NetSalesRetailTe,
			target.NetSalesRetailNativeTe = source.NetSalesRetailNativeTe,
			target.NetSalesCost = source.NetSalesCost,
			target.ShrinkActualUnits = source.ShrinkActualUnits,
			target.ShrinkActualRetailTe = source.ShrinkActualRetailTe,
			target.OnOrderUnits = source.OnOrderUnits,
			target.OnOrderRetailTe = source.OnOrderRetailTe,
			target.OnOrderCost = source.OnOrderCost,
			target.OnHandUnits = source.OnHandUnits,
			target.OnHandRetailTe = source.OnHandRetailTe,
			target.OnHandCost = source.OnHandCost,	
			target.UPDT_DT = getdate()	

When Not Matched By Target 
	Then Insert 
		(
			ProductStoreDateKey, 
			ProductKey,
			StoreKey,
			DateKey,
			ActualDate,
			PermRetailTe,
			PromoPcTotalRetailTe,
			ReceivedUnits,
			ReceivedRetailTe,
			ReceivedCost,
			NetSalesUnits,
			NetSalesRetailTe,
			NetSalesRetailNativeTe,
			NetSalesCost,
			ShrinkActualUnits,
			ShrinkActualRetailTe,
			OnOrderUnits,
			OnOrderRetailTe,
			OnOrderCost,
			OnHandUnits,
			OnHandRetailTe,
			OnHandCost,
			INS_DT,
			UPDT_DT
		)
	VALUES
		(
			source.ProductStoreDateKey, 
			source.ProductKey,
			source.StoreKey,
			source.DateKey,
			source.ActualDate,
			source.PermRetailTe,
			source.PromoPcTotalRetailTe,
			source.ReceivedUnits,
			source.ReceivedRetailTe,
			source.ReceivedCost,
			source.NetSalesUnits,
			source.NetSalesRetailTe,
			source.NetSalesRetailNativeTe,
			source.NetSalesCost,
			source.ShrinkActualUnits,
			source.ShrinkActualRetailTe,
			source.OnOrderUnits,
			source.OnOrderRetailTe,
			source.OnOrderCost,
			source.OnHandUnits,
			source.OnHandRetailTe,
			source.OnHandCost,
			getdate(),
			getdate()
		)
; -- merge must end with semicolon
```

