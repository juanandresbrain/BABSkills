# dbo.interface_directory

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| interface_description | nvarchar | 510 | 0 |  |  |  |
| update_timing | smallint | 2 | 0 |  |  |  |
| move_updates | tinyint | 1 | 0 |  |  |  |
| live_date | smalldatetime | 4 | 1 |  |  |  |
| ascii_export | tinyint | 1 | 0 |  |  |  |
| interface_voided_transactions | tinyint | 1 | 0 |  |  |  |
| all_modifications_relevant | tinyint | 1 | 0 |  |  |  |
| archive_correction_method | tinyint | 1 | 0 |  |  |  |
| edit_mass_update_flag | tinyint | 1 | 0 |  |  |  |
| applicability_method | tinyint | 1 | 0 |  |  |  |
| basic_dtlmr_subsystem | tinyint | 1 | 1 |  |  |  |
| object_id | int | 4 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| min_compatible_exe | nvarchar | 40 | 1 |  |  |  |
| dayend_subject_to_posting | tinyint | 1 | 0 |  |  |  |
| disallow_modification | tinyint | 1 | 0 |  |  |  |
| history_days | tinyint | 1 | 1 |  |  |  |
| scaleout_posting_method | tinyint | 1 | 1 |  |  |  |
| include_all_trans_with_cust | tinyint | 1 | 1 |  |  |  |
