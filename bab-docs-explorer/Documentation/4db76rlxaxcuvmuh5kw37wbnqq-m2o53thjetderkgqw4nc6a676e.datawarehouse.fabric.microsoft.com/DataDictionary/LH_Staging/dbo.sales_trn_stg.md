# dbo.sales_trn_stg

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_Date | datetime2 | 8 | 1 |  |  |  |
| Store_No | int | 4 | 1 |  |  |  |
| Register_No | int | 4 | 1 |  |  |  |
| Transaction_ID | decimal | 9 | 1 |  |  |  |
| Transaction_No | int | 4 | 1 |  |  |  |
| Line_ID | decimal | 5 | 1 |  |  |  |
| Line_Sequence | decimal | 5 | 1 |  |  |  |
| Cashier_No | int | 4 | 1 |  |  |  |
| Gross_Line_Amount | decimal | 9 | 1 |  |  |  |
| POS_Discount_Amount | decimal | 9 | 1 |  |  |  |
| POS_Discount_Type | int | 4 | 1 |  |  |  |
| Entry_Date_Time | datetime2 | 8 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Line_Object_Type | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 8000 | 1 |  |  |  |
| Reference_No | varchar | 8000 | 1 |  |  |  |
| Line_Action | int | 4 | 1 |  |  |  |
| Units | decimal | 9 | 1 |  |  |  |
| Transaction_Category | int | 4 | 1 |  |  |  |
| Transaction_Begin | varchar | 8000 | 1 |  |  |  |
| Vat_Tax_Amt | decimal | 5 | 1 |  |  |  |
| VirtualWorld_SerialNumber | varchar | 8000 | 1 |  |  |  |
| bear_id | varchar | 8000 | 1 |  |  |  |
