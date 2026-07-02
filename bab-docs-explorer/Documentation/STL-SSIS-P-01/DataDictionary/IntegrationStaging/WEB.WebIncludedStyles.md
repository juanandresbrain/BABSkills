# WEB.WebIncludedStyles

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BaseID | varchar | 5 | 1 |  |  |  |
| StyleCode | varchar | 6 | 1 |  |  |  |
| SKUDescription | varchar | 150 | 1 |  |  |  |
| SubClassHierarchyGroupID | int | 4 | 1 |  |  |  |
| Department | varchar | 50 | 1 |  |  |  |
| Class | varchar | 50 | 1 |  |  |  |
| SubClass | varchar | 50 | 1 |  |  |  |
| DepartmentCode | varchar | 50 | 1 |  |  |  |
| ClassCode | varchar | 50 | 1 |  |  |  |
| SubClassCode | varchar | 50 | 1 |  |  |  |
| UPC | varchar | 20 | 1 |  |  |  |
| Color | varchar | 20 | 1 |  |  |  |
| SellingGeography | varchar | 5 | 1 |  |  |  |
| StoreFrontEligible | int | 4 | 1 |  |  |  |
| OnOrderFlag | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spSelectProductCatalogMasterAttributes](../../StoredProcedures/IntegrationStaging/WEB.spSelectProductCatalogMasterAttributes.md)

