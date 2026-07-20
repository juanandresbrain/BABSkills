# dbo.experianfootfall_companyhierarchystoremapping

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
| NodeName | varchar | 8000 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| Updt_dt | datetime2 | 8 | 1 |  |  |  |
