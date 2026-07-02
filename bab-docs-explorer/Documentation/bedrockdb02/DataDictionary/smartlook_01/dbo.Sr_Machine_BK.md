# dbo.Sr_Machine_BK

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| machine_id | int | 4 | 0 |  |  |  |
| machine_name | varchar | 30 | 1 |  |  |  |
| status | int | 4 | 0 |  |  |  |
| execution_id | int | 4 | 0 |  |  |  |
| any_job | bit | 1 | 0 |  |  |  |
| hostname | varchar | 255 | 1 |  |  |  |
| install_path | varchar | 255 | 1 |  |  |  |
| daemon_tcp_port | int | 4 | 1 |  |  |  |
| requested_status | int | 4 | 1 |  |  |  |
| machine_version | varchar | 20 | 1 |  |  |  |
| host_id | varchar | 50 | 1 |  |  |  |
| shared_path | varchar | 255 | 1 |  |  |  |
| cluster_name | varchar | 255 | 1 |  |  |  |
| resource_name | varchar | 255 | 1 |  |  |  |

