# dbo.MSreplication_monitordata

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| lastrefresh | datetime | 8 | 1 |  |  |  |
| computetime | int | 4 | 1 |  |  |  |
| publication_id | int | 4 | 1 |  |  |  |
| publisher | sysname | 256 | 0 |  |  |  |
| publisher_srvid | int | 4 | 1 |  |  |  |
| publisher_db | sysname | 256 | 0 |  |  |  |
| publication | sysname | 256 | 0 |  |  |  |
| publication_type | int | 4 | 1 |  |  |  |
| agent_type | int | 4 | 1 |  |  |  |
| agent_id | int | 4 | 1 |  |  |  |
| agent_name | sysname | 256 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 1 |  |  |  |
| status | int | 4 | 1 |  |  |  |
| isagentrunningnow | bit | 1 | 1 |  |  |  |
| warning | int | 4 | 1 |  |  |  |
| last_distsync | datetime | 8 | 1 |  |  |  |
| agentstoptime | datetime | 8 | 1 |  |  |  |
| distdb | sysname | 256 | 1 |  |  |  |
| retention | int | 4 | 1 |  |  |  |
| time_stamp | datetime | 8 | 1 |  |  |  |
| worst_latency | int | 4 | 1 |  |  |  |
| best_latency | int | 4 | 1 |  |  |  |
| avg_latency | int | 4 | 1 |  |  |  |
| cur_latency | int | 4 | 1 |  |  |  |
| worst_runspeedPerf | int | 4 | 1 |  |  |  |
| best_runspeedPerf | int | 4 | 1 |  |  |  |
| average_runspeedPerf | int | 4 | 1 |  |  |  |
| mergePerformance | int | 4 | 1 |  |  |  |
| mergelatestsessionrunduration | int | 4 | 1 |  |  |  |
| mergelatestsessionrunspeed | float | 8 | 1 |  |  |  |
| mergelatestsessionconnectiontype | int | 4 | 1 |  |  |  |
| retention_period_unit | tinyint | 1 | 1 |  |  |  |
