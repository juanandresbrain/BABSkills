# dbo.spt_fallback_dev

**Database:** master  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| xserver_name | varchar | 30 | 0 |  |  |  |
| xdttm_ins | datetime | 8 | 0 |  |  |  |
| xdttm_last_ins_upd | datetime | 8 | 0 |  |  |  |
| xfallback_low | int | 4 | 1 |  |  |  |
| xfallback_drive | char | 2 | 1 |  |  |  |
| low | int | 4 | 0 |  |  |  |
| high | int | 4 | 0 |  |  |  |
| status | smallint | 2 | 0 |  |  |  |
| name | varchar | 30 | 0 |  |  |  |
| phyname | varchar | 127 | 0 |  |  |  |

