# dbo.operators_snapshot

**Database:** master  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| enabled | tinyint | 1 | 0 |  |  |  |
| email_address | nvarchar | 200 | 1 |  |  |  |
| last_email_date | int | 4 | 0 |  |  |  |
| last_email_time | int | 4 | 0 |  |  |  |
| pager_address | nvarchar | 200 | 1 |  |  |  |
| last_pager_date | int | 4 | 0 |  |  |  |
| last_pager_time | int | 4 | 0 |  |  |  |
| weekday_pager_start_time | int | 4 | 0 |  |  |  |
| weekday_pager_end_time | int | 4 | 0 |  |  |  |
| saturday_pager_start_time | int | 4 | 0 |  |  |  |
| saturday_pager_end_time | int | 4 | 0 |  |  |  |
| sunday_pager_start_time | int | 4 | 0 |  |  |  |
| sunday_pager_end_time | int | 4 | 0 |  |  |  |
| pager_days | tinyint | 1 | 0 |  |  |  |
| netsend_address | nvarchar | 200 | 1 |  |  |  |
| last_netsend_date | int | 4 | 0 |  |  |  |
| last_netsend_time | int | 4 | 0 |  |  |  |
| category_id | int | 4 | 0 |  |  |  |

