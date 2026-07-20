# dbo.integrationstaging_wms_shippednotreceived_storereportstage

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| LicensePlate | varchar | 8000 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| Name | varchar | 8000 | 1 |  |  |  |
| FromWarehouse | varchar | 8000 | 1 |  |  |  |
| ToWarehouse | varchar | 8000 | 1 |  |  |  |
| ProductHierarchy | varchar | 8000 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ItemQty | int | 4 | 1 |  |  |  |
| CartonQty | int | 4 | 1 |  |  |  |
| MiscCartonDetails | varchar | 8000 | 1 |  |  |  |
| isMiscCarton | bit | 1 | 1 |  |  |  |
| ShipConfirmUTCDateTime | datetime2 | 8 | 1 |  |  |  |
