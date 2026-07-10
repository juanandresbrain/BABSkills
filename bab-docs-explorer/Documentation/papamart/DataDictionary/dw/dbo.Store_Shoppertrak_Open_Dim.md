# dbo.Store_Shoppertrak_Open_Dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 0 | YES |  |  |
| store_key | int | 4 | 0 |  |  | Store (FK to Store_Dim) |
| date_key_from | int | 4 | 0 |  |  | Date the store becomes a Shopper Trak Store (FK to Date_Dim) |
| date_key_thru | int | 4 | 0 |  |  | Date the store stops being a shoppertrak store (999999 is forever) |
| hour_day_start | int | 4 | 0 |  |  | Starting Hour for shopper trak traffic |
| hour_day_end | int | 4 | 0 |  |  | Ending Hour for ShopperTrak Traffic |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
