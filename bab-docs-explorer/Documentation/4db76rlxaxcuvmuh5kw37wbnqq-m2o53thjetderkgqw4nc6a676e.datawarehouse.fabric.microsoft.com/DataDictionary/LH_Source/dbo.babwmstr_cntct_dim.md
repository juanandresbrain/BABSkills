# dbo.babwmstr_cntct_dim

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CNTCT_ID | int | 4 | 1 |  |  |  |
| ROLE_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 1 |  |  |  |
| FRST_NM | varchar | 8000 | 1 |  |  |  |
| LAST_NM | varchar | 8000 | 1 |  |  |  |
| PHN_NBR | varchar | 8000 | 1 |  |  |  |
| PHN_EXTNSN | varchar | 8000 | 1 |  |  |  |
| CELL_NBR | varchar | 8000 | 1 |  |  |  |
| FAX_NBR | varchar | 8000 | 1 |  |  |  |
| EMAIL | varchar | 8000 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_ON | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_ON | datetime2 | 8 | 1 |  |  |  |
| LWSN_CD | varchar | 8000 | 1 |  |  |  |
| isSystemMAINT | bit | 1 | 1 |  |  |  |
| END_DATE | datetime2 | 8 | 1 |  |  |  |
