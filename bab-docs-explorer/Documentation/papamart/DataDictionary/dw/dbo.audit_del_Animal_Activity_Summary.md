# dbo.audit_del_Animal_Activity_Summary

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Animal_key | int | 4 | 0 |  |  |  |
| Customer_Key | int | 4 | 0 |  |  |  |
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
| Process_name | varchar | 25 | 1 |  |  |  |
| Process_DateTime | datetime | 8 | 1 |  |  |  |
| Reason_Key | int | 4 | 1 |  |  |  |
| Original_Guest_Type_Key | int | 4 | 1 |  |  |  |
| deleted_dt | datetime | 8 | 1 |  |  |  |
