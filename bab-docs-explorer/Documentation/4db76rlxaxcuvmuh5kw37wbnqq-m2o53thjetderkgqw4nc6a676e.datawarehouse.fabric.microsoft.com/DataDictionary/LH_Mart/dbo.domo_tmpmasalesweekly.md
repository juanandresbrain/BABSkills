# dbo.domo_tmpmasalesweekly

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | varchar | 8000 | 1 |  |  |  |
| StoreKey | varchar | 8000 | 1 |  |  |  |
| ActualDate | date | 3 | 1 |  |  |  |
| PermMDretail | decimal | 9 | 1 |  |  |  |
| PermMUretail | decimal | 9 | 1 |  |  |  |
| PermMDCretail | decimal | 9 | 1 |  |  |  |
| PermMUCretail | decimal | 9 | 1 |  |  |  |
| PromoPCtotalRetail | decimal | 9 | 1 |  |  |  |
| ReceivedUnits | int | 4 | 1 |  |  |  |
| ReceivedRetail | decimal | 9 | 1 |  |  |  |
| ReturnToVendorUnits | int | 4 | 1 |  |  |  |
| ReturnToVendorRetail | decimal | 9 | 1 |  |  |  |
| DistributionUnits | int | 4 | 1 |  |  |  |
| DistributionRetail | decimal | 9 | 1 |  |  |  |
| TransferInUnits | int | 4 | 1 |  |  |  |
| TransferInRetail | decimal | 9 | 1 |  |  |  |
| TransferOutUnits | int | 4 | 1 |  |  |  |
| TransferOutRetail | decimal | 9 | 1 |  |  |  |
| SalesTotalUnits | int | 4 | 1 |  |  |  |
| SalesTotalRetail | decimal | 9 | 1 |  |  |  |
| SalesTotalRetailUSte | decimal | 9 | 1 |  |  |  |
| SalesTotalRetailNativeTe | decimal | 9 | 1 |  |  |  |
| SalesTotalCost | decimal | 9 | 1 |  |  |  |
| ReturnUnits | int | 4 | 1 |  |  |  |
| ReturnRetail | decimal | 9 | 1 |  |  |  |
| ReturnRetailUSte | decimal | 9 | 1 |  |  |  |
| ReturnRetailNativeTe | decimal | 9 | 1 |  |  |  |
| ReturnCost | decimal | 9 | 1 |  |  |  |
| ShrinkActualUnits | int | 4 | 1 |  |  |  |
| ShrinkActualRetail | decimal | 9 | 1 |  |  |  |
| AdjustmentsTotalUnits | int | 4 | 1 |  |  |  |
| AdjustmentsTotalRetail | decimal | 9 | 1 |  |  |  |
| SalesTotalCostNative | decimal | 9 | 1 |  |  |  |
| ReturnCostNative | decimal | 9 | 1 |  |  |  |
