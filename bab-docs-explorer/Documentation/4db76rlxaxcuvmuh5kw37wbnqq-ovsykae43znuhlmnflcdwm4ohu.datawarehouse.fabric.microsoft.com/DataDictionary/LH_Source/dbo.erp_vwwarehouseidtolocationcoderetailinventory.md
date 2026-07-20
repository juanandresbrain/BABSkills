# dbo.erp_vwwarehouseidtolocationcoderetailinventory

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WarehouseID | varchar | 8000 | 1 |  |  |  |
| LocationCode | varchar | 8000 | 1 |  |  |  |
| PrimaryAddressDescription | varchar | 8000 | 1 |  |  |  |
| OperationalSiteID | int | 4 | 1 |  |  |  |
| OperationalSiteCode | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| AreAdvancedWarehouseManagementProcessesEnabled | varchar | 8000 | 1 |  |  |  |
| IsRetailStoreWarehouse | varchar | 8000 | 1 |  |  |  |
