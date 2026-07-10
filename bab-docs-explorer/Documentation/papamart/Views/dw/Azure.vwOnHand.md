# Azure.vwOnHand

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwOnHand"]
    azure_OnHand(["azure.OnHand"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| azure.OnHand |

## View Code

```sql
CREATE view [Azure].[vwOnHand]

as
-- =============================================================================================================
-- Name: [Azure].[vwOnHande]
--
-- Description: Product Dimension
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		John Eck			12/19/2018		Initial Creation

--											
-- =============================================================================================================

--select StoreKey,ProductKey, SUM(on_hand_units) as OnHand ,Left(Merch_year_wk,4) as workYear ,Right(Merch_year_wk,2) as workweek
--from bedrockdb02.ma_01.dbo.hist_oh_style_loc_wk  d
--inner join bedrockdb02.ma_01.dbo.style a on d.style_ID = a.style_id
--inner join Azure.vwStyleToProdKey p on a.style_code = p.style
--inner join Azure.vwLocationToStoreKey S on d.location_id = s.Locationid
--where Left(Merch_year_wk,4) in ('2017' , '2018') and right(Merch_year_wk,2) in (44,45,46,47,48)
--group by StoreKey,ProductKey,Left(Merch_year_wk,4) ,Right(Merch_year_wk,2) 
--having sum(on_hand_units) <> 0



select
	StoreKey,
	ProductKey,
	OnHand,
	workYear,
	workweek
from azure.OnHand
```

