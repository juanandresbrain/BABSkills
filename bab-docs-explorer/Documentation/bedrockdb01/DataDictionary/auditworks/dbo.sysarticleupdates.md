# dbo.sysarticleupdates

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| artid | int | 4 | 0 |  |  |  |
| pubid | int | 4 | 0 |  |  |  |
| sync_ins_proc | int | 4 | 0 |  |  |  |
| sync_upd_proc | int | 4 | 0 |  |  |  |
| sync_del_proc | int | 4 | 0 |  |  |  |
| autogen | bit | 1 | 0 |  |  |  |
| sync_upd_trig | int | 4 | 0 |  |  |  |
| conflict_tableid | int | 4 | 1 |  |  |  |
| ins_conflict_proc | int | 4 | 1 |  |  |  |
| identity_support | bit | 1 | 0 |  |  |  |
