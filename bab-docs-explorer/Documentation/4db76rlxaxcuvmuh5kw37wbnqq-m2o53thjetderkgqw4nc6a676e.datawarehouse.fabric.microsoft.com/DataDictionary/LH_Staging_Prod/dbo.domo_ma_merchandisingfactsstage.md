# dbo.domo_ma_merchandisingfactsstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductStoreDateKey | varchar | 8000 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| ActualDate | date | 3 | 1 |  |  |  |
| PermRetailTe | decimal | 17 | 1 |  |  |  |
| PromoPcTotalRetailTe | decimal | 17 | 1 |  |  |  |
| ReceivedUnits | int | 4 | 1 |  |  |  |
| ReceivedRetailTe | decimal | 17 | 1 |  |  |  |
| ReceivedCost | decimal | 17 | 1 |  |  |  |
| NetSalesUnits | int | 4 | 1 |  |  |  |
| NetSalesRetailTe | decimal | 17 | 1 |  |  |  |
| NetSalesRetailNativeTe | decimal | 17 | 1 |  |  |  |
| NetSalesCost | decimal | 17 | 1 |  |  |  |
| ShrinkActualUnits | int | 4 | 1 |  |  |  |
| ShrinkActualRetailTe | decimal | 17 | 1 |  |  |  |
| OnOrderUnits | int | 4 | 1 |  |  |  |
| OnOrderRetailTe | decimal | 17 | 1 |  |  |  |
| OnOrderCost | decimal | 17 | 1 |  |  |  |
| OnHandUnits | int | 4 | 1 |  |  |  |
| OnHandRetailTe | decimal | 17 | 1 |  |  |  |
| OnHandCost | decimal | 17 | 1 |  |  |  |
