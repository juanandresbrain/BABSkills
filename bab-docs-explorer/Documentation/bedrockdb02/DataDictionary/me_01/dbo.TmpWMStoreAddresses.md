# dbo.TmpWMStoreAddresses

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WHSE | varchar | 3 | 0 |  |  |  |
| STORE_NBR | varchar | 20 | 0 |  |  |  |
| NAME | varchar | 43 | 0 |  |  |  |
| ADDR_LINE_1 | varchar | 8000 | 1 |  |  |  |
| ADDR_LINE_2 | varchar | 50 | 0 |  |  |  |
| ADDR_LINE_3 | int | 4 | 1 |  |  |  |
| CITY | varchar | 20 | 1 |  |  |  |
| STATE | varchar | 2 | 1 |  |  |  |
| ZIP | varchar | 15 | 1 |  |  |  |
| CNTRY | varchar | 3 | 1 |  |  |  |
| CONTACT | int | 4 | 1 |  |  |  |
| PHONE | varchar | 15 | 0 |  |  |  |
| FAX | varchar | 50 | 1 |  |  |  |
| EMAIL | varchar | 60 | 1 |  |  |  |
| DFLT_CO | varchar | 3 | 0 |  |  |  |
| DFLT_DIV | varchar | 3 | 0 |  |  |  |
| STAT_CODE | int | 4 | 0 |  |  |  |
| OPEN_DATE | smalldatetime | 4 | 1 |  |  |  |
| CLOSED_DATE | smalldatetime | 4 | 1 |  |  |  |
| HOLD_DATE | int | 4 | 1 |  |  |  |
| GRP | int | 4 | 1 |  |  |  |
| CHAIN | int | 4 | 1 |  |  |  |
| ZONE | int | 4 | 1 |  |  |  |
| TERRITORY | int | 4 | 1 |  |  |  |
| REGION | int | 4 | 1 |  |  |  |
| DISTRICT | int | 4 | 1 |  |  |  |
| SHIP_MON | int | 4 | 1 |  |  |  |
| SHIP_TUE | int | 4 | 1 |  |  |  |
| SHIP_WED | int | 4 | 1 |  |  |  |
| SHIP_THU | int | 4 | 1 |  |  |  |
| SHIP_FRI | int | 4 | 1 |  |  |  |
| SHIP_SAT | int | 4 | 1 |  |  |  |
| SHIP_SU | int | 4 | 1 |  |  |  |
| ACCEPT_IRREG | int | 4 | 1 |  |  |  |
| WAVE_LABEL_TYPE | int | 4 | 1 |  |  |  |
| PKG_SLIP_TYPE | int | 4 | 1 |  |  |  |
| PRINT_CODE | int | 4 | 1 |  |  |  |
| CARTON_CNT_TYPE | varchar | 3 | 0 |  |  |  |
| STORE_TYPE | int | 4 | 1 |  |  |  |
| SHIP_VIA | int | 4 | 1 |  |  |  |
| RTE_NBR | int | 4 | 1 |  |  |  |
| RTE_ATTR | int | 4 | 1 |  |  |  |
| RTE_TO | int | 4 | 1 |  |  |  |
| RTE_TYPE_1 | int | 4 | 1 |  |  |  |
| RTE_TYPE_2 | int | 4 | 1 |  |  |  |
| RTE_ZIP | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_1 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_2 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_3 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_4 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_5 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_6 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_7 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_8 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_9 | int | 4 | 1 |  |  |  |
| SPL_INSTR_CODE_10 | int | 4 | 1 |  |  |  |
| ASSIGN_MERCH_TYPE | int | 4 | 1 |  |  |  |
| ASSIGN_MERCH_GROUP | int | 4 | 1 |  |  |  |
| ASSIGN_STORE_DEPT | int | 4 | 1 |  |  |  |
| PROC_STAT_CODE | int | 4 | 0 |  |  |  |
| ERROR_SEQ_NBR | int | 4 | 0 |  |  |  |
| CARTON_LABEL_TYPE | varchar | 1 | 0 |  |  |  |
| CARTON_CUBNG_INDIC | int | 4 | 0 |  |  |  |
| MAX_CTN | varchar | 1 | 0 |  |  |  |
| MAX_PLT | varchar | 1 | 0 |  |  |  |
| BUSN_UNIT_CODE | int | 4 | 1 |  |  |  |
| USE_INBD_LPN_AS_OUT_BD_LPN | varchar | 1 | 0 |  |  |  |
| CREATE_DATE_TIME | datetime | 8 | 0 |  |  |  |
| MOD_DATE_TIME | datetime | 8 | 0 |  |  |  |
| USER_ID | varchar | 5 | 0 |  |  |  |

