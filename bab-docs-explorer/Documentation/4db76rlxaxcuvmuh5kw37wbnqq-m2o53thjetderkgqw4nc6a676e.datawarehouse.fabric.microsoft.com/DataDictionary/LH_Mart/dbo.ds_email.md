# dbo.ds_email

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sendid_key | int | 4 | 1 |  |  |  |
| senddate | datetime2 | 8 | 1 |  |  |  |
| bouncedate | datetime2 | 8 | 1 |  |  |  |
| clickdate | datetime2 | 8 | 1 |  |  |  |
| unsubdate | datetime2 | 8 | 1 |  |  |  |
| opendate | datetime2 | 8 | 1 |  |  |  |
| clickcount | int | 4 | 1 |  |  |  |
| HashedEmail | varchar | 8000 | 1 |  |  |  |
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| Subject | varchar | 8000 | 1 |  |  |  |
| EmailName | varchar | 8000 | 1 |  |  |  |
| EventDate | datetime2 | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| actual_date | date | 3 | 1 |  |  |  |
