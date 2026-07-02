# ERP.ItemMasterToWMStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CO | varchar | 3 | 0 |  |  |  |
| DIV | varchar | 3 | 0 |  |  |  |
| STYLE | varchar | 6 | 1 |  |  |  |
| SKU_DESC | varchar | 8000 | 1 |  |  |  |
| CARTON_TYPE | varchar | 1 | 0 |  |  |  |
| UNIT_PRICE | numeric | 9 | 1 |  |  |  |
| RETAIL_PRICE | decimal | 9 | 1 |  |  |  |
| STD_PACK_QTY | int | 4 | 0 |  |  |  |
| STD_CASE_QTY | int | 4 | 0 |  |  |  |
| MAX_CASE_QTY | int | 4 | 0 |  |  |  |
| STD_CASE_LEN | int | 4 | 0 |  |  |  |
| STD_CASE_WIDTH | int | 4 | 0 |  |  |  |
| STD_CASE_HT | int | 4 | 0 |  |  |  |
| UNIT_WT | int | 4 | 0 |  |  |  |
| UNIT_VOL | int | 4 | 0 |  |  |  |
| STD_PACK_WT | int | 4 | 0 |  |  |  |
| STD_PACK_VOL | int | 4 | 0 |  |  |  |
| STD_CASE_WT | int | 4 | 0 |  |  |  |
| STD_CASE_VOL | int | 4 | 0 |  |  |  |
| CRITCL_DIM_1 | int | 4 | 0 |  |  |  |
| CRITCL_DIM_2 | int | 4 | 0 |  |  |  |
| CRITCL_DIM_3 | int | 4 | 0 |  |  |  |
| STAT_CODE | int | 4 | 0 |  |  |  |
| SKU_BRCD | varchar | 6 | 1 |  |  |  |
| STD_PACK_WIDTH | int | 4 | 0 |  |  |  |
| STD_PACK_LEN | int | 4 | 0 |  |  |  |
| STD_PACK_HT | int | 4 | 0 |  |  |  |
| UNIT_WIDTH | int | 4 | 0 |  |  |  |
| UNIT_LEN | int | 4 | 0 |  |  |  |
| UNIT_HT | int | 4 | 0 |  |  |  |
| SKU_PROFILE_ID | varchar | 3 | 0 |  |  |  |
| ECCN_NBR | varchar | 5 | 0 |  |  |  |
| EXP_LICN_NBR | varchar | 3 | 0 |  |  |  |
| COMMODITY_CODE | varchar | 11 | 0 |  |  |  |
| nmfc_code | varchar | 10 | 1 |  |  |  |
| frt_class | varchar | 10 | 1 |  |  |  |
| COMMODITY_LEVEL_DESC | varchar | 100 | 1 |  |  |  |
| WHSE | varchar | 3 | 0 |  |  |  |
| STORE_DEPT | varchar | 3 | 0 |  |  |  |
| ORGN_CERT_CODE | varchar | 10 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| InWM | int | 4 | 1 |  |  |  |
| HTS | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeItemMasterToWM](../../StoredProcedures/IntegrationStaging/ERP.spMergeItemMasterToWM.md)

