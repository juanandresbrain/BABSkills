# dbo.drives

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server | varchar | 8000 | 1 |  |  |  |
| drive | varchar | 8000 | 1 |  |  |  |
| FreeSpace | int | 4 | 1 |  |  |  |
| TotalSize | bigint | 8 | 1 |  |  |  |
| PercentFree | int | 4 | 1 |  |  |  |
| DateStamp | datetime2 | 8 | 1 |  |  |  |
| emailsent | bit | 1 | 1 |  |  |  |
