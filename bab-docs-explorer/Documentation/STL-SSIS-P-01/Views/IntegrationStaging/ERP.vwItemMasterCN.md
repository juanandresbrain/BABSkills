# ERP.vwItemMasterCN

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwItemMasterCN"]
    ERP_ItemMasterToWM(["ERP.ItemMasterToWM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.ItemMasterToWM |

## View Code

```sql
CREATE view [ERP].[vwItemMasterCN]

as

select  Style as style_code,
		isnull(replace(SKU_DESC, ',','' ), '') as short_desc,
		
		std_pack_qty as distribution_multiple
from ERP.ItemMasterToWM with (nolock)
where entity = 3001
and datediff(dd, isnull(UpdateDate, InsertDate), getdate()) =  0
and left(style, 1) = '8'
```

