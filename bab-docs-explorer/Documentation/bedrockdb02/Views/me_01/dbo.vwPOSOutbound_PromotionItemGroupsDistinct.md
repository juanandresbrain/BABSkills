# dbo.vwPOSOutbound_PromotionItemGroupsDistinct

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSOutbound_PromotionItemGroupsDistinct"]
    dbo_vwPOSOutbound_PromotionItemGroups(["dbo.vwPOSOutbound_PromotionItemGroups"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwPOSOutbound_PromotionItemGroups |

## View Code

```sql
CREATE view [dbo].[vwPOSOutbound_PromotionItemGroupsDistinct]

--------------------------------------------------------------------------------------------------------------------------------------
--Tim Callahan --					Created view for Eligible Styles View
--Tim Callahan --	2023-10-20		Added additional filter to ensure we are only capturing active promotion item groups 
--------------------------------------------------------------------------------------------------------------------------------------
as

select distinct style_code 
from vwPOSOutbound_PromotionItemGroups ig
where 1=1
--and ig.item_group_id in (select distinct DealItemRequired_ItemGroup from [dbo].[vwPOSOutbound_Promotions_V2] (nolock)) -- Added 10/20/2023
```

