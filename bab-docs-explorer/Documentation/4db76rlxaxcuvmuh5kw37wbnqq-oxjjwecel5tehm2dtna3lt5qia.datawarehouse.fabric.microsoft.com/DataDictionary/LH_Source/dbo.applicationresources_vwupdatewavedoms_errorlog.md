# dbo.applicationresources_vwupdatewavedoms_errorlog

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| LogDateTime | datetime2 | 8 | 1 |  |  |  |
| ErrorMessage | varchar | 8000 | 1 |  |  |  |
| Attempts | int | 4 | 1 |  |  |  |
