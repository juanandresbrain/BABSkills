# dbo.giftcardmstr_stylecode

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleID | int | 4 | 1 |  |  |  |
| Style_Code | varchar | 8000 | 1 |  |  |  |
| StyleDescription | varchar | 8000 | 1 |  |  |  |
| DefaultValue | decimal | 5 | 1 |  |  |  |
| PackQuantity | int | 4 | 1 |  |  |  |
| StyleQtyPerVendorQty | int | 4 | 1 |  |  |  |
| isGiftCard | bit | 1 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_DT | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_DT | datetime2 | 8 | 1 |  |  |  |
