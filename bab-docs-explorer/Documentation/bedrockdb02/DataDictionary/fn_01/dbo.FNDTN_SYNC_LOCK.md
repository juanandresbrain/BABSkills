# dbo.FNDTN_SYNC_LOCK

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SYNC_LOCK_ID | T_ID | 16 | 0 |  |  |  |
| TKN | varchar | 50 | 0 |  |  |  |
| FMLY_ID | int | 4 | 0 |  |  |  |
| SRVC_NAME | varchar | 50 | 1 |  |  |  |
| SGMNT_ID | numeric | 9 | 1 |  |  |  |
| JOB_ID | int | 4 | 1 |  |  |  |
| EXCTN_ID | int | 4 | 1 |  |  |  |
| PRCS_ID | int | 4 | 1 |  |  |  |
| MCHN_NAME | varchar | 50 | 1 |  |  |  |
| STRT_DATE | datetime | 8 | 0 |  |  |  |
| EXPRY_DATE | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.FNDTN_SYNC_LOCK_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_LOCK_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_LOCK_EXTND_TIME_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_LOCK_EXTND_TIME_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_MASS_LOCK_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_MASS_LOCK_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_RLS_GUID_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_RLS_GUID_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_RLS_JOB_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_RLS_JOB_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_RLS_SRV_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_RLS_SRV_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_RLS_SRV_ND_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_RLS_SRV_ND_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_RLS_SRV_SGMNT_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_RLS_SRV_SGMNT_$SP.md)
- [fn_01: dbo.FNDTN_SYNC_RLS_SRV_SGMT_ND_$SP](../../StoredProcedures/fn_01/dbo.FNDTN_SYNC_RLS_SRV_SGMT_ND_$SP.md)

