# dbo.sales_trn_stg_dsc_timctesting

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_Date | datetime2 | 8 | 1 |  |  |  |
| Store_No | int | 4 | 1 |  |  |  |
| Transaction_ID | decimal | 9 | 1 |  |  |  |
| Line_Sequence | decimal | 5 | 1 |  |  |  |
| Cashier_No | int | 4 | 1 |  |  |  |
| Gross_Line_Amount | decimal | 9 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Reference_No | varchar | 8000 | 1 |  |  |  |
| Line_Action | int | 4 | 1 |  |  |  |
| Transaction_No | int | 4 | 1 |  |  |  |
| Units | decimal | 9 | 1 |  |  |  |
| Coupon_Flag | int | 4 | 1 |  |  |  |
| recID | int | 4 | 1 |  |  |  |
| coupon_key | int | 4 | 1 |  |  |  |
| origReference_no | varchar | 8000 | 1 |  |  |  |
| categoryTypeID | int | 4 | 1 |  |  |  |
| isExpired | bit | 1 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| Lift_Amount | decimal | 9 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
