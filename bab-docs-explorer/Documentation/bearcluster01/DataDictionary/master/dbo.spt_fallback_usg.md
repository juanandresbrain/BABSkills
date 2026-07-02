# dbo.spt_fallback_usg

**Database:** master  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| xserver_name | varchar | 30 | 0 |  |  |  |
| xdttm_ins | datetime | 8 | 0 |  |  |  |
| xdttm_last_ins_upd | datetime | 8 | 0 |  |  |  |
| xfallback_vstart | int | 4 | 1 |  |  |  |
| dbid | smallint | 2 | 0 |  |  |  |
| segmap | int | 4 | 0 |  |  |  |
| lstart | int | 4 | 0 |  |  |  |
| sizepg | int | 4 | 0 |  |  |  |
| vstart | int | 4 | 0 |  |  |  |

