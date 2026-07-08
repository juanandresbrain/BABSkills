# dbo.MSqreader_agents

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| name | nvarchar | 200 | 1 |  |  |  |
| job_id | binary | 16 | 1 |  |  |  |
| profile_id | int | 4 | 1 |  |  |  |
| job_step_uid | uniqueidentifier | 16 | 1 |  |  |  |
