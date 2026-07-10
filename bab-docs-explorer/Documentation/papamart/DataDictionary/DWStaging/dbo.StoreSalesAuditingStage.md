# dbo.StoreSalesAuditingStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreNumber | varchar | 4 | 1 |  |  |  |
| RTL_TRN_ID | int | 4 | 1 |  |  |  |
| TRANS_COUNT | int | 4 | 1 |  |  |  |
| NET_UNITS | decimal | 9 | 1 |  |  |  |
| NET_SALES | money | 8 | 1 |  |  |  |
| End_DateTime | datetime | 8 | 1 |  |  |  |
| REDEEMED_AMOUNT | money | 8 | 1 |  |  |  |
| Excluded_Items | int | 4 | 1 |  |  |  |
| Tran_Units | int | 4 | 1 |  |  |  |
| ITEM_NO | varchar | 20 | 1 |  |  |  |
| SkuDescription | varchar | 100 | 1 |  |  |  |
| line_item_no | int | 4 | 1 |  |  |  |
| RETURN_FLG | int | 4 | 1 |  |  |  |
