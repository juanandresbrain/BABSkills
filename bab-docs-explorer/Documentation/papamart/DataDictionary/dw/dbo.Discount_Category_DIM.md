# dbo.Discount_Category_DIM

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| categoryTypeID | int | 4 | 0 |  |  | Surrogate Key assigned to this Category Type assigned by Discount Manager |
| categoryType | varchar | 50 | 0 |  |  | Name for the Category Type |
| categoryTypeRelSeq | int | 4 | 0 |  |  | Relative sort sequence of the Category Type |
| channelType | varchar | 50 | 0 |  |  | Name of this Marketing Channel |
| channelTypeRelSeq | int | 4 | 0 |  |  | Relative sequence of this Channel Type within Financial Groups |
| financialGroup | varchar | 50 | 0 |  |  |  |
| financialGroupRelSeq | int | 4 | 0 |  |  | Relative sort sequence of this Financial Group |
