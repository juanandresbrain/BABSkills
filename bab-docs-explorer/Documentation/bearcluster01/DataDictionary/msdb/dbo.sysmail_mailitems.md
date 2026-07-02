# dbo.sysmail_mailitems

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mailitem_id | int | 4 | 0 | YES |  |  |
| profile_id | int | 4 | 0 |  |  |  |
| recipients | varchar | -1 | 1 |  |  |  |
| copy_recipients | varchar | -1 | 1 |  |  |  |
| blind_copy_recipients | varchar | -1 | 1 |  |  |  |
| subject | nvarchar | 510 | 1 |  |  |  |
| from_address | varchar | -1 | 1 |  |  |  |
| reply_to | varchar | -1 | 1 |  |  |  |
| body | nvarchar | -1 | 1 |  |  |  |
| body_format | varchar | 20 | 1 |  |  |  |
| importance | varchar | 6 | 1 |  |  |  |
| sensitivity | varchar | 12 | 1 |  |  |  |
| file_attachments | nvarchar | -1 | 1 |  |  |  |
| attachment_encoding | varchar | 20 | 1 |  |  |  |
| query | nvarchar | -1 | 1 |  |  |  |
| execute_query_database | sysname | 256 | 1 |  |  |  |
| attach_query_result_as_file | bit | 1 | 1 |  |  |  |
| query_result_header | bit | 1 | 1 |  |  |  |
| query_result_width | int | 4 | 1 |  |  |  |
| query_result_separator | char | 1 | 1 |  |  |  |
| exclude_query_output | bit | 1 | 1 |  |  |  |
| append_query_error | bit | 1 | 1 |  |  |  |
| send_request_date | datetime | 8 | 0 |  |  |  |
| send_request_user | sysname | 256 | 0 |  |  |  |
| sent_account_id | int | 4 | 1 |  |  |  |
| sent_status | tinyint | 1 | 1 |  |  |  |
| sent_date | datetime | 8 | 1 |  |  |  |
| last_mod_date | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_readrequest](../../StoredProcedures/msdb/dbo.sp_readrequest.md)
- [msdb: dbo.sysmail_delete_profile_sp](../../StoredProcedures/msdb/dbo.sysmail_delete_profile_sp.md)

