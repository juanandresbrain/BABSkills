# dbo.SALES_TRN_STG_DSC_TimCTesting

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_Date | smalldatetime | 4 | 1 |  |  |  |
| Store_No | int | 4 | 1 |  |  |  |
| Transaction_ID | numeric | 9 | 1 |  |  |  |
| Line_Sequence | numeric | 5 | 1 |  |  |  |
| Cashier_No | int | 4 | 1 |  |  |  |
| Gross_Line_Amount | numeric | 9 | 1 |  |  |  |
| Line_Object | smallint | 2 | 1 |  |  |  |
| Reference_No | varchar | 20 | 1 |  |  |  |
| Line_Action | tinyint | 1 | 1 |  |  |  |
| Transaction_No | int | 4 | 1 |  |  |  |
| Units | numeric | 9 | 1 |  |  |  |
| Coupon_Flag | tinyint | 1 | 1 |  |  |  |
| recID | int | 4 | 0 | YES |  |  |
| coupon_key | int | 4 | 1 |  |  |  |
| origReference_no | varchar | 80 | 1 |  |  |  |
| categoryTypeID | int | 4 | 1 |  |  |  |
| isExpired | bit | 1 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| Lift_Amount | money | 8 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
