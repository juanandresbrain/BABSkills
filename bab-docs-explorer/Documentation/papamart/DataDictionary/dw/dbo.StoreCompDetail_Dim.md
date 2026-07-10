# dbo.StoreCompDetail_Dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| isCompTY | bit | 1 | 0 |  |  |  |
| isCompNY | bit | 1 | 0 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
| isShopperTrak | bit | 1 | 0 |  |  | Is this a ShopperTrak Store on this date? |
| isShopperTrakCompTY | bit | 1 | 0 |  |  | Is this a ShopperTrak Comp Store for this date? |
| isShopperTrakCompNY | bit | 1 | 0 |  |  | Is this a ShopperTrak Comp Store Next Year for this date? |
| isSOTF | bit | 1 | 0 |  |  | Is this a Store of the Future (SOTF) store on this date? |
| ShopperTrakStartHour | int | 4 | 0 |  |  | This is the hour before which the record is not considered a ShopperTrak record |
| ShopperTrakEndHour | int | 4 | 0 |  |  | This is the hour after which the record is not considered a ShopperTrak record |
