# dbo.sysalerts

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| event_source | nvarchar | 200 | 0 |  |  |  |
| event_category_id | int | 4 | 1 |  |  |  |
| event_id | int | 4 | 1 |  |  |  |
| message_id | int | 4 | 0 |  |  |  |
| severity | int | 4 | 0 |  |  |  |
| enabled | tinyint | 1 | 0 |  |  |  |
| delay_between_responses | int | 4 | 0 |  |  |  |
| last_occurrence_date | int | 4 | 0 |  |  |  |
| last_occurrence_time | int | 4 | 0 |  |  |  |
| last_response_date | int | 4 | 0 |  |  |  |
| last_response_time | int | 4 | 0 |  |  |  |
| notification_message | nvarchar | 1024 | 1 |  |  |  |
| include_event_description | tinyint | 1 | 0 |  |  |  |
| database_name | nvarchar | 1024 | 1 |  |  |  |
| event_description_keyword | nvarchar | 200 | 1 |  |  |  |
| occurrence_count | int | 4 | 0 |  |  |  |
| count_reset_date | int | 4 | 0 |  |  |  |
| count_reset_time | int | 4 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| has_notification | int | 4 | 0 |  |  |  |
| flags | int | 4 | 0 |  |  |  |
| performance_condition | nvarchar | 1024 | 1 |  |  |  |
| category_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)

