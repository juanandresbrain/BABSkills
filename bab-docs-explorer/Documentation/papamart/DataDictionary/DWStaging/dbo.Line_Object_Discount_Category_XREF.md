# dbo.Line_Object_Discount_Category_XREF

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Line_Object | smallint | 2 | 0 |  |  | Auditworks Line Object Code (dw.Line_Object_dim) |
| categoryType | varchar | 50 | 0 |  |  |  |
| channelType | varchar | 50 | 0 |  |  | Discount Manager Category Type (dw.Discount_Category_DIM) |
| needsReview | bit | 1 | 0 |  |  |  |
