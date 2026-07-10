# ExperianFootfall.CompanyHierarchyStoreMappingBAK20161104

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 1 |  |  |  |
| SiteIdentity | int | 4 | 1 |  |  |  |
| IsShopperTrak | bit | 1 | 1 |  |  |  |
| IsFootFall | bit | 1 | 1 |  |  |  |
| IsCurrentlyOffline | bit | 1 | 1 |  |  |  |
| CompanyID | int | 4 | 1 |  |  |  |
| HierarchyID | int | 4 | 1 |  |  |  |
| NodeName | varchar | 20 | 1 |  |  |  |
| CurrencyCode | varchar | 3 | 1 |  |  |  |
| Updt_dt | datetime | 8 | 1 |  |  |  |
