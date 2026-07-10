# dbo.Line_Object_Tender_Lift_Factors

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object | int | 4 | 0 |  |  | Line Object Number |
| factorGiftcardLift | smallint | 2 | 1 |  |  | Factor for calculating Giftcard Lift |
| factorDiscountLift | smallint | 2 | 1 |  |  | Factor for calculating Discount Lift |
