# dbo.application_servicelogginggeneralusage

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| logid | bigint | 8 | 1 |  |  |  |
| logcreateddate | datetime2 | 8 | 1 |  |  |  |
| message | varchar | 8000 | 1 |  |  |  |
| isanexception | bit | 1 | 1 |  |  |  |
| exceptionmessage | varchar | 8000 | 1 |  |  |  |
| exceptionstacktrace | varchar | 8000 | 1 |  |  |  |
| app_serviceid | int | 4 | 1 |  |  |  |
| functionname | varchar | 8000 | 1 |  |  |  |
