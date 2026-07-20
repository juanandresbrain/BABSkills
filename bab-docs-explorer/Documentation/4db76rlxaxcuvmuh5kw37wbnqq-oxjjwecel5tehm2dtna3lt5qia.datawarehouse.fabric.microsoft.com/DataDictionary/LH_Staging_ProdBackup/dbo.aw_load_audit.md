# dbo.aw_load_audit

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Package_Name | varchar | 8000 | 1 |  |  |  |
| Execution_Instance | varchar | 8000 | 1 |  |  |  |
| Machine_Name | varchar | 8000 | 1 |  |  |  |
| Start_Time | datetime2 | 8 | 1 |  |  |  |
| Existing_Dimension_Input_Row_Count | int | 4 | 1 |  |  |  |
| Special_Members_Input_Row_Count | int | 4 | 1 |  |  |  |
| Source_System_Input_Row_Count | int | 4 | 1 |  |  |  |
| Unchanged_Output_Row_Count | int | 4 | 1 |  |  |  |
| New_Output_Row_Count | int | 4 | 1 |  |  |  |
| Deleted_Output_Row_Count | int | 4 | 1 |  |  |  |
| SCD2_Expired_Output_Row_Count | int | 4 | 1 |  |  |  |
| SCD2_New_Output_Row_Count | int | 4 | 1 |  |  |  |
| SCD1_Updated_Output_Row_Count | int | 4 | 1 |  |  |  |
| Invalid_Input_Output_Row_Count | int | 4 | 1 |  |  |  |
| Time_First_Existing_Dimension_Row_Received | datetime2 | 8 | 1 |  |  |  |
| Time_Last_Existing_Dimension_Row_Received | datetime2 | 8 | 1 |  |  |  |
| Time_First_Special_Members_Row_Received | datetime2 | 8 | 1 |  |  |  |
| Time_Last_Special_Members_Row_Received | datetime2 | 8 | 1 |  |  |  |
| Time_First_Source_System_Row_Received | datetime2 | 8 | 1 |  |  |  |
| Time_Last_Source_System_Row_Received | datetime2 | 8 | 1 |  |  |  |
| Milliseconds_until_first_key_match | int | 4 | 1 |  |  |  |
| Number_of_rows_held_in_cache_on_first_key_match | int | 4 | 1 |  |  |  |
| Maximum_number_of_rows_held_in_cache | int | 4 | 1 |  |  |  |
| Average_number_of_rows_held_in_cache | int | 4 | 1 |  |  |  |
| Milliseconds_of_Upstream_Backpressure_Generated | int | 4 | 1 |  |  |  |
| Sort_Optimization_Cache_Hit_Percentage | decimal | 5 | 1 |  |  |  |
| Time_First_Output_Row_Produced | datetime2 | 8 | 1 |  |  |  |
| Time_Last_Output_Row_Produced | datetime2 | 8 | 1 |  |  |  |
| Milliseconds_of_Downstream_Backpressure_Experienced | int | 4 | 1 |  |  |  |
| Maximum_Output_Rows_per_Second | int | 4 | 1 |  |  |  |
