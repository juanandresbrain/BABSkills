# ERP.vwPurchaseOrderHeaderDynamicsExtract

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwPurchaseOrderHeaderDynamicsExtract"]
    ERP_PurchaseOrderHeaderStage(["ERP.PurchaseOrderHeaderStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.PurchaseOrderHeaderStage |

## View Code

```sql
CREATE view [ERP].[vwPurchaseOrderHeaderDynamicsExtract]

---------------------------------------------------------------------------------------------------------------------------
--	Tim Callahan -	2021-01-16	-	Created view - Stages data for Merge into ERP.PurchaseOrderHeader 
--	Tim Callahan -	2021-09-29	-	Modified view - Removed emptyItemId filter as we now want to maintain POs that contain service items
---------------------------------------------------------------------------------------------------------------------------

as

with MaxConfirmationNumberHeader as (

select distinct PurchaseOrderNumber, Entity, max (ConfirmationNumber) as MaxConfirmationNumber
from ERP.PurchaseOrderHeaderStage 
group by PurchaseOrderNumber, Entity


) 

select h.PurchaseOrderNumber, 
ConfirmationNumber, 
TransportMethodDesc,
FOBDesc,
ShipFromId, 
'BAB Purchasing' as Rep2id, -- Hard Coding this as Cannot Find Function Data Entity Surce for Personnell Number Lookup 
CurrencyDesc, 
OrderCreateDate, 
PaymentTerms, 
h.Entity, 
1 as IsCurrent -- Hardcoding to 1 as we are leveraging max entry in CTE above for merge source 
from ERP.PurchaseOrderHeaderStage  H
join MaxConfirmationNumberHeader M on h.PurchaseOrderNumber=m.PurchaseOrderNumber
								  and h.Entity=m.Entity
								  and h.ConfirmationNumber=m.MaxConfirmationNumber
--where h.PurchaseOrderNumber not in ( select distinct PurchaseOrderNumber from erp.PurchaseOrderLinesStage (nolock) where ItemID = '') -- Exclude POs with empty item numbers, likely maintenance
```

