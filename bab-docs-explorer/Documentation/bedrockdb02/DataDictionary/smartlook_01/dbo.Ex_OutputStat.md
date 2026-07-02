# dbo.Ex_OutputStat

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | int | 4 | 0 | YES |  |  |
| sequence_no | int | 4 | 0 | YES |  |  |
| output_type | int | 4 | 0 |  |  |  |
| record_count | int | 4 | 0 |  |  |  |
| work_file_name | varchar | 255 | 1 |  |  |  |
| work_file_size | int | 4 | 1 |  |  |  |
| work_return_code | int | 4 | 1 |  |  |  |
| work_date_time | datetime | 8 | 1 |  |  |  |
| backup_file_name | varchar | 255 | 1 |  |  |  |
| backup_file_size | int | 4 | 1 |  |  |  |
| backup_return_code | int | 4 | 1 |  |  |  |
| backup_date_time | datetime | 8 | 1 |  |  |  |
| merge_file_name | varchar | 255 | 1 |  |  |  |
| merge_file_size | int | 4 | 1 |  |  |  |
| merge_return_code | int | 4 | 1 |  |  |  |
| merge_date_time | datetime | 8 | 1 |  |  |  |
| final_file_name | varchar | 255 | 1 |  |  |  |
| final_file_size1 | int | 4 | 1 |  |  |  |
| final_file_size2 | int | 4 | 1 |  |  |  |
| final_return_code | int | 4 | 1 |  |  |  |
| final_date_time | datetime | 8 | 1 |  |  |  |
| append_flag | bit | 1 | 0 |  |  |  |
| flag_file_code | int | 4 | 1 |  |  |  |
| file_number | numeric | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Cs_TransmissionStart](../../StoredProcedures/fn_01/dbo.Cs_TransmissionStart.md)
- [fn_01: dbo.Ex_OutputStat_Backup](../../StoredProcedures/fn_01/dbo.Ex_OutputStat_Backup.md)
- [fn_01: dbo.Ex_OutputStat_ByJob](../../StoredProcedures/fn_01/dbo.Ex_OutputStat_ByJob.md)
- [fn_01: dbo.Ex_OutputStat_Final](../../StoredProcedures/fn_01/dbo.Ex_OutputStat_Final.md)
- [fn_01: dbo.Ex_OutputStat_Merge](../../StoredProcedures/fn_01/dbo.Ex_OutputStat_Merge.md)
- [fn_01: dbo.Ex_OutputStat_Work](../../StoredProcedures/fn_01/dbo.Ex_OutputStat_Work.md)
- [fn_01: dbo.Ex_OutputStat_Work_40](../../StoredProcedures/fn_01/dbo.Ex_OutputStat_Work_40.md)
- [smartlook_01: dbo.Cs_TransmissionStart](../../StoredProcedures/smartlook_01/dbo.Cs_TransmissionStart.md)

