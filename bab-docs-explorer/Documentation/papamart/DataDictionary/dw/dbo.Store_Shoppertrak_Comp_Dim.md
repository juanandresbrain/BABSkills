# dbo.Store_Shoppertrak_Comp_Dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 0 | YES |  |  |
| store_key | int | 4 | 0 |  |  | Store (FK to Store_dim) |
| date_key_from | int | 4 | 0 |  |  | Date the store becomes comp (FK to Date_Dim) |
| date_key_thru | int | 4 | 0 |  |  | Date the store quits being comp for shopperTrak (FK to Date_Dim) Forever is 999999 |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
