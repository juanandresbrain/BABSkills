# dbo.audit_del_animal_activity_summary

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Animal_key | int | 4 | 1 |  |  |  |
| Customer_Key | int | 4 | 1 |  |  |  |
| Original_Store_Key | int | 4 | 1 |  |  |  |
| Product_Key | int | 4 | 1 |  |  |  |
| Original_Purpose_key | int | 4 | 1 |  |  |  |
| Number_of_Visits | int | 4 | 1 |  |  |  |
| First_Visit_Date_Key | int | 4 | 1 |  |  |  |
| Last_Visit_Date_Key | int | 4 | 1 |  |  |  |
| Recency_in_Months | int | 4 | 1 |  |  |  |
| WEB_First_Visit_Date_Key | int | 4 | 1 |  |  |  |
| WEB_Last_Visit_Date_Key | int | 4 | 1 |  |  |  |
| WEB_Recency_In_Months | int | 4 | 1 |  |  |  |
| WEB_Number_Of_Visits | int | 4 | 1 |  |  |  |
| Process_name | varchar | 8000 | 1 |  |  |  |
| Process_DateTime | datetime2 | 8 | 1 |  |  |  |
| Reason_Key | int | 4 | 1 |  |  |  |
| Original_Guest_Type_Key | int | 4 | 1 |  |  |  |
| deleted_dt | datetime2 | 8 | 1 |  |  |  |
