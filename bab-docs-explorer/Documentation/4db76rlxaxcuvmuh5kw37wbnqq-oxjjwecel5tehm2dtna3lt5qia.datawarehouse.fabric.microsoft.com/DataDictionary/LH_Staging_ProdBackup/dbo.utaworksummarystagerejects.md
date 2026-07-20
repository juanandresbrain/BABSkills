# dbo.utaworksummarystagerejects

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| wrks_id | varchar | 8000 | 1 |  |  |  |
| emp_id | varchar | 8000 | 1 |  |  |  |
| wrks_work_date | varchar | 8000 | 1 |  |  |  |
| paygrp_id | varchar | 8000 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime2 | 8 | 1 |  |  |  |
