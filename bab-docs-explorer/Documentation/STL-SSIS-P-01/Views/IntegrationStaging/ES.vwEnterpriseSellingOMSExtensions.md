# ES.vwEnterpriseSellingOMSExtensions

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ES.vwEnterpriseSellingOMSExtensions"]
    WEB_ProductCatalogMasterAttributes(["WEB.ProductCatalogMasterAttributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.ProductCatalogMasterAttributes |

## View Code

```sql
CREATE view [ES].[vwEnterpriseSellingOMSExtensions]

as

--------------------------------------------------------------------------------------------------
-- vwEnterpriseSellingOMSExtensions - Lookup for OMS Extensions
--- 2017-08-04 - Ben Barud - Created View
--- ISNULL is necessary for Entity Framework
---------------------------------------------------------------------------------------------------

SELECT       ISNULL(ROW_NUMBER() OVER(ORDER BY Style_Code), -1) AS ID
             ,Style_Code
			 ,ColorCode
			 ,EyeColor
			 ,FriendHeight
			 ,FriendWeight
			 ,BirthCertificateRequired
			 ,CommodityCode
			 ,Department
			 ,ShippingClass
FROM            WEB.ProductCatalogMasterAttributes
```

