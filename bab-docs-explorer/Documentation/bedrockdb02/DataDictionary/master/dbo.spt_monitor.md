# dbo.spt_monitor

**Database:** master  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| lastrun | datetime | 8 | 0 |  |  |  |
| cpu_busy | int | 4 | 0 |  |  |  |
| io_busy | int | 4 | 0 |  |  |  |
| idle | int | 4 | 0 |  |  |  |
| pack_received | int | 4 | 0 |  |  |  |
| pack_sent | int | 4 | 0 |  |  |  |
| connections | int | 4 | 0 |  |  |  |
| pack_errors | int | 4 | 0 |  |  |  |
| total_read | int | 4 | 0 |  |  |  |
| total_write | int | 4 | 0 |  |  |  |
| total_errors | int | 4 | 0 |  |  |  |

