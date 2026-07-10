# DOMO.tmpMaSalesWeekly

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | varchar | 30 | 1 |  |  |  |
| StoreKey | varchar | 30 | 1 |  |  |  |
| ActualDate | date | 3 | 1 |  |  |  |
| PermMDretail | numeric | 9 | 0 |  |  |  |
| PermMUretail | numeric | 9 | 0 |  |  |  |
| PermMDCretail | numeric | 9 | 0 |  |  |  |
| PermMUCretail | numeric | 9 | 0 |  |  |  |
| PromoPCtotalRetail | numeric | 9 | 0 |  |  |  |
| ReceivedUnits | int | 4 | 0 |  |  |  |
| ReceivedRetail | numeric | 9 | 0 |  |  |  |
| ReturnToVendorUnits | int | 4 | 0 |  |  |  |
| ReturnToVendorRetail | numeric | 9 | 0 |  |  |  |
| DistributionUnits | int | 4 | 0 |  |  |  |
| DistributionRetail | numeric | 9 | 0 |  |  |  |
| TransferInUnits | int | 4 | 0 |  |  |  |
| TransferInRetail | numeric | 9 | 0 |  |  |  |
| TransferOutUnits | int | 4 | 0 |  |  |  |
| TransferOutRetail | numeric | 9 | 0 |  |  |  |
| SalesTotalUnits | int | 4 | 0 |  |  |  |
| SalesTotalRetail | money | 8 | 1 |  |  |  |
| SalesTotalRetailUSte | numeric | 9 | 0 |  |  |  |
| SalesTotalRetailNativeTe | money | 8 | 1 |  |  |  |
| SalesTotalCost | money | 8 | 1 |  |  |  |
| ReturnUnits | int | 4 | 0 |  |  |  |
| ReturnRetail | money | 8 | 1 |  |  |  |
| ReturnRetailUSte | numeric | 9 | 0 |  |  |  |
| ReturnRetailNativeTe | money | 8 | 1 |  |  |  |
| ReturnCost | money | 8 | 1 |  |  |  |
| ShrinkActualUnits | int | 4 | 0 |  |  |  |
| ShrinkActualRetail | numeric | 9 | 0 |  |  |  |
| AdjustmentsTotalUnits | int | 4 | 0 |  |  |  |
| AdjustmentsTotalRetail | numeric | 9 | 0 |  |  |  |
| SalesTotalCostNative | money | 8 | 1 |  |  |  |
| ReturnCostNative | money | 8 | 1 |  |  |  |
