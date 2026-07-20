# dbo.utaworkdetailadjuststagerejects

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Wbt_ID | varchar | 8000 | 1 |  |  |  |
| Wrkda_Work_Date | varchar | 8000 | 1 |  |  |  |
| Htype_ID | varchar | 8000 | 1 |  |  |  |
| WRKDA_ID | varchar | 8000 | 1 |  |  |  |
| wrkda_minutes | varchar | 8000 | 1 |  |  |  |
| tcode_id | varchar | 8000 | 1 |  |  |  |
| wrkda_adjust_date | varchar | 8000 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime2 | 8 | 1 |  |  |  |
| proj_id | bigint | 8 | 1 |  |  |  |
