# dbo.MSmerge_subscriptions

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_id | smallint | 2 | 0 |  |  |  |
| publisher_db | sysname | 256 | 1 |  |  |  |
| publication_id | int | 4 | 0 |  |  |  |
| subscriber_id | smallint | 2 | 1 |  |  |  |
| subscriber_db | sysname | 256 | 1 |  |  |  |
| subscription_type | int | 4 | 1 |  |  |  |
| sync_type | tinyint | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| subscription_time | datetime | 8 | 0 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| publisher | sysname | 256 | 1 |  |  |  |
| subscriber | sysname | 256 | 1 |  |  |  |
| subid | uniqueidentifier | 16 | 0 |  |  |  |
| subscriber_version | int | 4 | 1 |  |  |  |
