# dbo.giftcardmstr_status

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StatusID | int | 4 | 1 |  |  |  |
| StatusDescription | varchar | 8000 | 1 |  |  |  |
| StatusTypeID | int | 4 | 1 |  |  |  |
| StatusOrder | int | 4 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_DT | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_DT | datetime2 | 8 | 1 |  |  |  |
