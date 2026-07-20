# dbo.utaemployeejobstagerejects

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Emp_ID | varchar | 8000 | 1 |  |  |  |
| Empjob_Start_Date | varchar | 8000 | 1 |  |  |  |
| Empjob_End_Date | varchar | 8000 | 1 |  |  |  |
| Job_ID | varchar | 8000 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime2 | 8 | 1 |  |  |  |
