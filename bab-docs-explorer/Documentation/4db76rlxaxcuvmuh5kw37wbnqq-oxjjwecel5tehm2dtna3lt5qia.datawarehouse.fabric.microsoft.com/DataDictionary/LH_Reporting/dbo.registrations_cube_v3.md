# dbo.registrations_cube_v3

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RecepientAgeID | decimal | 5 | 1 |  |  |  |
| RecepientID | int | 4 | 1 |  |  |  |
| AddressID | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| product_key | varchar | 8000 | 1 |  |  |  |
| GST_VST_RECUR_CD | varchar | 8000 | 1 |  |  |  |
| ADDR_VST_RECUR_CD | varchar | 8000 | 1 |  |  |  |
| GIFT_IND | varchar | 8000 | 1 |  |  |  |
| GNDR_CD | varchar | 8000 | 1 |  |  |  |
| ReceipientAge | decimal | 5 | 1 |  |  |  |
| hasRecipientAge | int | 4 | 1 |  |  |  |
| PurchaserAge | decimal | 5 | 1 |  |  |  |
| hasPurchaserAge | int | 4 | 1 |  |  |  |
| DistanceToStore | int | 4 | 1 |  |  |  |
| hasDistanceToStore | int | 4 | 1 |  |  |  |
| isForeign | int | 4 | 1 |  |  |  |
| TourismBand | int | 4 | 1 |  |  |  |
| 5to25_MileBand | int | 4 | 1 |  |  |  |
| isComp | int | 4 | 1 |  |  |  |
| isCompNextYear | int | 4 | 1 |  |  |  |
| calc | int | 4 | 1 |  |  |  |
| isNearBirthday | int | 4 | 1 |  |  |  |
| isTourist | int | 4 | 1 |  |  |  |
| GuestID | int | 4 | 1 |  |  |  |
| isSOTF | int | 4 | 1 |  |  |  |
| isShopperTrak | int | 4 | 1 |  |  |  |
| isShopperTrakCompTY | int | 4 | 1 |  |  |  |
| isShopperTrakCompNY | int | 4 | 1 |  |  |  |
| TKF_ID | int | 4 | 1 |  |  |  |
