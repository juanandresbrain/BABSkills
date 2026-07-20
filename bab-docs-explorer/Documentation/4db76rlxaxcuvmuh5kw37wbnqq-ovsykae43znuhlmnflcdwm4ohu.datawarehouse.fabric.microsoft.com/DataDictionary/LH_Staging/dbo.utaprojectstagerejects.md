# dbo.utaprojectstagerejects

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Proj_ID | bigint | 8 | 1 |  |  |  |
| Proj_Name | varchar | 8000 | 1 |  |  |  |
| Proj_Desc | varchar | 8000 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime2 | 8 | 1 |  |  |  |
