# dbo.azure_daily_inventory

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 1 |  |  |  |
| DateKey | date | 3 | 1 |  |  |  |
| StyleCode | varchar | 8000 | 1 |  |  |  |
| EffectiveInv | int | 4 | 1 |  |  |  |
| AvailToDist | int | 4 | 1 |  |  |  |
| OnHand | int | 4 | 1 |  |  |  |
| Purchased | int | 4 | 1 |  |  |  |
| Allocated | int | 4 | 1 |  |  |  |
| OrderMultiple | int | 4 | 1 |  |  |  |
| InventoryBuffer | int | 4 | 1 |  |  |  |
| InTransit | int | 4 | 1 |  |  |  |
