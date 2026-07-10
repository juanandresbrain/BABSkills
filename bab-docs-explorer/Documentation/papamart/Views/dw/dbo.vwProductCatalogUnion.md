# dbo.vwProductCatalogUnion

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwProductCatalogUnion"]
    POS_PBIProductCatalogMasterAttributesStage(["POS.PBIProductCatalogMasterAttributesStage"]) --> VIEW
    POS_ProductCatalogMasterAttributesStage(["POS.ProductCatalogMasterAttributesStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| POS.PBIProductCatalogMasterAttributesStage |
| POS.ProductCatalogMasterAttributesStage |

## View Code

```sql
create view vwProductCatalogUnion 

as

select *
from [stl-ssis-p-01].IntegrationStaging.POS.ProductCatalogMasterAttributesStage
UNION
select *
from [stl-ssis-p-01].IntegrationStaging.POS.PBIProductCatalogMasterAttributesStage
```

