# dbo.aw_load_statistics

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Interval_Start | datetime2 | 8 | 1 |  |  |  |
| Interval_End | datetime2 | 8 | 1 |  |  |  |
| Input_ED_Rows_Received | int | 4 | 1 |  |  |  |
| Input_SM_Rows_Received | int | 4 | 1 |  |  |  |
| Input_SS_Rows_Received | int | 4 | 1 |  |  |  |
| Cache_ED_Rows | int | 4 | 1 |  |  |  |
| Cache_SM_Rows | int | 4 | 1 |  |  |  |
| Cache_SS_Rows | int | 4 | 1 |  |  |  |
| Output_Unchanged_Rows_Sent | int | 4 | 1 |  |  |  |
| Output_New_Rows_Sent | int | 4 | 1 |  |  |  |
| Output_Deleted_Rows_Sent | int | 4 | 1 |  |  |  |
| Output_Updated_SCD1_Rows_Sent | int | 4 | 1 |  |  |  |
| Output_Expired_SCD2_Rows_Sent | int | 4 | 1 |  |  |  |
| Output_New_SCD2_Rows_Sent | int | 4 | 1 |  |  |  |
| Match_Prep_Work_Units_Built | int | 4 | 1 |  |  |  |
| Match_Prep_Rows_Built_Into_Work_Units | int | 4 | 1 |  |  |  |
| Match_Prep_Bulk_Matched_Rows | int | 4 | 1 |  |  |  |
| Match_Prep_Work_Unit_Count | int | 4 | 1 |  |  |  |
| Matching_Matched_Key_Queue_Length | int | 4 | 1 |  |  |  |
| Matching_Skipped_Rows | int | 4 | 1 |  |  |  |
| Matching_Regular_Determination | int | 4 | 1 |  |  |  |
| Matching_Sort_Optimization_Determination | int | 4 | 1 |  |  |  |
| Matching_Undetermined | int | 4 | 1 |  |  |  |
| Thread_Delay_Waiting_For_Input | int | 4 | 1 |  |  |  |
| Thread_Delay_Matching_Waiting_On_Caching | int | 4 | 1 |  |  |  |
| Thread_Delay_Processing_Waiting_On_Matching | int | 4 | 1 |  |  |  |
| Thread_Delay_Input_Waiting_On_Row_Processing | int | 4 | 1 |  |  |  |
