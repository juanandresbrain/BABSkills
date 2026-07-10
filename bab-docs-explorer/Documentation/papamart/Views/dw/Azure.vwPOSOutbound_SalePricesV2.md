# Azure.vwPOSOutbound_SalePricesV2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_SalePricesV2"]
    Azure_vwPOSOutbound_Products(["Azure.vwPOSOutbound_Products"]) --> VIEW
    dbo_vwPOSOutbound_SalePrices_V2(["dbo.vwPOSOutbound_SalePrices_V2"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.vwPOSOutbound_Products |
| dbo.vwPOSOutbound_SalePrices_V2 |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_SalePricesV2] AS

	 
select
deal_discount_id, 
deal_id, 
deal_no, 
deal_name, 
deal_description, 
DealStartDate, 
DealEndDate, 
deal_discount_type, 
deal_discount_name, 
DealTierDef_DiscType, 
DealTierDef_DiscPct, 
DealTierDef_DiscAmt, 
DealTierDef_DiscAppliesTo, 
DealTierDef_DiscQty, 
DealTierDef_AddlInfo, 
DealTierDef_ThresholdType, 
DealTierDef_ThresholdQty, 
DealTierDef_ThresholdAmt, 
DealItemRequired_ItemGroup, 
DealItemReqQty, 
DealLocationJurisdictionCode, 
DealLocation, 
DealItemDiscSpec_IdentityType, 
DealItemDiscSpec_Qty, 
DealItemDiscSpec_DiscType, 
DealItemDiscSpec_DiscPct, 
DealItemDiscSpec_DiscAmt, 
DealItemDiscSpec_DiscAppliesTo

--from Bedrockdb02.me_01.dbo.vwPOSOutbound_SalePrices -- This has been wrong since last view modify_date 2023-10-17 16:14:00.317
from Bedrockdb02.me_01.dbo.vwPOSOutbound_SalePrices_V2 -- Updated to V2 on 9/9/2024 -- TimC


where DealItemRequired_ItemGroup  in
(select ProductNumber from [Azure].[vwPOSOutbound_Products] )
```

