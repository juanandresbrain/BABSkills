# dbo.Z_FNDTN_RPRT_ITEM_07162015

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RPRT_ITEM_ID | T_ID | 16 | 0 |  |  |  |
| FLY_QLFD_NAME | varchar | 255 | 0 |  |  |  |
| RPRT_SRVR_ID | smallint | 2 | 0 |  |  |  |
| PRNT_FLDR_ID | T_ID | 16 | 1 |  |  |  |
| NAME_RSRC_KEY | varchar | 255 | 0 |  |  |  |
| DESC_RSRC_KEY | varchar | 255 | 1 |  |  |  |
| TYPE | smallint | 2 | 0 |  |  |  |
| SCRTY_APP_ID | smallint | 2 | 1 |  |  |  |
| SCRTY_ACS_KEY | nvarchar | 20 | 1 |  |  |  |
| ENBL_PRFRNCS | bit | 1 | 0 |  |  |  |
| OPTNS | varchar | 500 | 1 |  |  |  |
| PRNT_RPRT_ITEM_ID | T_ID | 16 | 1 |  |  |  |
| RPRT_ITEM_STS | smallint | 2 | 0 |  |  |  |
| OVRRD | bit | 1 | 1 |  |  |  |
| HSTRY_DAYS | smallint | 2 | 1 |  |  |  |
| CAN_SCHDL | bit | 1 | 1 |  |  |  |
| CAN_PRNT | bit | 1 | 1 |  |  |  |
| CAN_SCHDL_PRNT | bit | 1 | 1 |  |  |  |
| CAN_EXPRT | bit | 1 | 1 |  |  |  |
| CAN_SCHDL_EXPRT | bit | 1 | 1 |  |  |  |
| EXPRT_DAYS | smallint | 2 | 1 |  |  |  |
| EXPRT_FLDR | nvarchar | 510 | 1 |  |  |  |
| USE_CRTR_SETS | bit | 1 | 1 |  |  |  |
| CAN_SCHDL_SNPSHT | bit | 1 | 1 |  |  |  |
| IS_SNAPSHOT | bit | 1 | 0 |  |  |  |
| COMPANY_ID | smallint | 2 | 0 |  |  |  |
| SNAPSHOT_GROUP_NAME | varchar | 255 | 1 |  |  |  |
