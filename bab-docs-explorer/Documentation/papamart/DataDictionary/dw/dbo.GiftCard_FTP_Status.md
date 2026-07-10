# dbo.GiftCard_FTP_Status

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| GroupCode | varchar | 20 | 1 |  |  |  |
| pulled_date | datetime | 8 | 1 |  |  |  |
| period_start_date | datetime | 8 | 1 |  |  |  |
| sequence_number | int | 4 | 1 |  |  |  |
| ptd_pulled_date | datetime | 8 | 1 |  |  |  |
| mposx_pulled_date | datetime | 8 | 1 |  |  |  |
| dact_pulled_date | datetime | 8 | 1 |  |  |  |
| hdsk_pulled_date | datetime | 8 | 1 |  |  |  |
| wg_dact_pulled_date | datetime | 8 | 1 |  |  |  |
| wg_hdsk_pulled_date | datetime | 8 | 1 |  |  |  |
| ErrorFlag | bit | 1 | 1 |  |  |  |
| ErrorMessage | varchar | 400 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
