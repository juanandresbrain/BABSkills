# dbo.SALES_TRN_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_Date | smalldatetime | 4 | 1 |  |  |  |
| Store_No | int | 4 | 1 |  |  |  |
| Register_No | smallint | 2 | 1 |  |  |  |
| Transaction_ID | numeric | 9 | 1 |  |  |  |
| Transaction_No | int | 4 | 1 |  |  |  |
| Line_ID | numeric | 5 | 1 |  |  |  |
| Line_Sequence | numeric | 5 | 1 |  |  |  |
| Cashier_No | int | 4 | 1 |  |  |  |
| Gross_Line_Amount | numeric | 9 | 1 |  |  |  |
| POS_Discount_Amount | numeric | 9 | 1 |  |  |  |
| POS_Discount_Type | smallint | 2 | 1 |  |  |  |
| Entry_Date_Time | datetime | 8 | 1 |  |  |  |
| Line_Object | smallint | 2 | 1 |  |  |  |
| Line_Object_Type | tinyint | 1 | 1 |  |  |  |
| Line_Object_Description | varchar | 255 | 1 |  |  |  |
| Reference_No | varchar | 80 | 1 |  |  |  |
| Line_Action | tinyint | 1 | 1 |  |  |  |
| Units | numeric | 9 | 1 |  |  |  |
| Transaction_Category | tinyint | 1 | 1 |  |  |  |
| Transaction_Begin | varchar | 50 | 1 |  |  |  |
| Vat_Tax_Amt | decimal | 5 | 1 |  |  |  |
| VirtualWorld_SerialNumber | varchar | 100 | 1 |  |  |  |
| bear_id | varchar | 100 | 1 |  |  |  |
