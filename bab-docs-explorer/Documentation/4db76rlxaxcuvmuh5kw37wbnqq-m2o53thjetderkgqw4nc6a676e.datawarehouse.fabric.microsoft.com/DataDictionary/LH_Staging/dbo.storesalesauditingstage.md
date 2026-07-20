# dbo.storesalesauditingstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| RTL_TRN_ID | int | 4 | 1 |  |  |  |
| TRANS_COUNT | int | 4 | 1 |  |  |  |
| NET_UNITS | decimal | 9 | 1 |  |  |  |
| NET_SALES | decimal | 9 | 1 |  |  |  |
| End_DateTime | datetime2 | 8 | 1 |  |  |  |
| REDEEMED_AMOUNT | decimal | 9 | 1 |  |  |  |
| Excluded_Items | int | 4 | 1 |  |  |  |
| Tran_Units | int | 4 | 1 |  |  |  |
| ITEM_NO | varchar | 8000 | 1 |  |  |  |
| SkuDescription | varchar | 8000 | 1 |  |  |  |
| line_item_no | int | 4 | 1 |  |  |  |
| RETURN_FLG | int | 4 | 1 |  |  |  |
