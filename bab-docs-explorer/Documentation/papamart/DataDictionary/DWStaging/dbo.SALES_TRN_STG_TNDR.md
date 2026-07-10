# dbo.SALES_TRN_STG_TNDR

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_Date | smalldatetime | 4 | 1 |  |  |  |
| Store_No | int | 4 | 1 |  |  |  |
| Transaction_ID | numeric | 9 | 1 |  |  |  |
| Gross_Line_Amount | numeric | 9 | 1 |  |  |  |
| Line_Object | smallint | 2 | 1 |  |  |  |
| Reference_No | varchar | 80 | 1 |  |  |  |
| Units | numeric | 9 | 1 |  |  |  |
| Transaction_Begin | varchar | 50 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| tender_key | int | 4 | 1 |  |  |  |
