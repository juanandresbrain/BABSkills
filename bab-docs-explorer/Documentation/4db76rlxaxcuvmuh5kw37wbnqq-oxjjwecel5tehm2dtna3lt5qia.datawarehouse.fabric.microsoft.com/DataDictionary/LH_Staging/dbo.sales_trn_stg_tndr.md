# dbo.sales_trn_stg_tndr

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_Date | datetime2 | 8 | 1 |  |  |  |
| Store_No | int | 4 | 1 |  |  |  |
| Transaction_ID | decimal | 9 | 1 |  |  |  |
| Gross_Line_Amount | decimal | 9 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Reference_No | varchar | 8000 | 1 |  |  |  |
| Units | decimal | 9 | 1 |  |  |  |
| Transaction_Begin | varchar | 8000 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| tender_key | int | 4 | 1 |  |  |  |
