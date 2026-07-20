# dbo.giftcard_ftp_status_international_stage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| GroupCode | varchar | 8000 | 1 |  |  |  |
| pulled_date | datetime2 | 8 | 1 |  |  |  |
| period_start_date | datetime2 | 8 | 1 |  |  |  |
| sequence_number | int | 4 | 1 |  |  |  |
| ptd_pulled_date | datetime2 | 8 | 1 |  |  |  |
| mposx_pulled_date | datetime2 | 8 | 1 |  |  |  |
| dact_pulled_date | datetime2 | 8 | 1 |  |  |  |
| hdsk_pulled_date | datetime2 | 8 | 1 |  |  |  |
| wg_dact_pulled_date | datetime2 | 8 | 1 |  |  |  |
| wg_hdsk_pulled_date | datetime2 | 8 | 1 |  |  |  |
| ErrorFlag | bit | 1 | 1 |  |  |  |
| ErrorMessage | varchar | 8000 | 1 |  |  |  |
